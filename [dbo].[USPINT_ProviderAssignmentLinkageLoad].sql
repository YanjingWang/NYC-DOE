USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPINT_ProviderAssignmentLinkageLoad]    Script Date: 12/9/2024 9:35:28 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[USPINT_ProviderAssignmentLinkageLoad]

AS
     BEGIN

         SET XACT_ABORT ON;
         SET NOCOUNT ON;

/**************************************************************************************************************************************************
Object Name: USPINT_ProviderAssignmentLinakgeLoad
Purpose: Populate Provider Assignment data in SEO_MART database from INT_RelatedServices and INT_ProviderAssignment tables
Date Created: 10/27/2020

Modification Details:

Author					ModifiedDate		Comments
Phani Marupaka			12/23/2020			Populated PAFirstFullAttendDate column for Assistive Technology Service
Phani Marupaka			06/23/2021          Modify MandateStartDate,MandateEndDate,ServiceStartDate,ServiceEndDate columns from DateTime to Date
Christopher Agwu		08/19/2022			Added business logic for FirstAttendDate. Replaced hardcoded values with data-driven SEOBusinessRules Lookups
											Added three columns (LoadedSchoolSetting, DocumentCreatedDate,CreatedBy) as from RAJA cod
Pratap Pasam            06/02/2023          commented filter condition RecommendedDurationNumeric>0
Raji Munnangi			09/13/2024			Bring documents created after PA Rollover (which is around August 1st week) even for non-Charter kids
											Earlier, we would bring Mandates created on/after Sept 1st for non-Charter kids
***************************************************************************************************************************************************/

--GET SEO Business Rules Lookup Values--------------------------
Declare @SQLCOL NVARCHAR(MAX),@SQLROW NVARCHAR(MAX), @LKCAT varchar(50)

--GET SEO Business Rules
SET @LKCAT='USP_INTProviderAssignmentLinakgeLoad'
EXEC dbo.USPSEO_GetSEOBusinessRules @LKCAT, @SQLCOL OUTPUT, @SQLROW OUTPUT

---CREATE TABLE--
IF Object_ID('Tempdb..#SEOLKValues') is not null
	Drop table #SEOLKValues
CREATE TABLE #SEOLKValues (ID int)
EXEC (@SQLCOL)
INSERT INTO #SEOLKValues
EXEC (@SQLROW)
--select * from #SEOLKValues
----------------------------------------------------------------


DECLARE @PADate DATETIME,@FADate DATETIME, @COUNT INT, @MandateCreatedDate0701 Date, @MandateCreatedDate0801 Date, @Date Int, @Month Int,@SchoolYear Varchar(9), @SchoolStartDate Date
SET @COUNT = (SELECT COUNT(*) FROM dbo.INT_ProviderAssignmentLinkage);
SET @PADate = (SELECT PADate FROM (
				SELECT  CASE WHEN SUBSTRING(replace(convert(varchar,getdate(),101),'/','') ,1,4)<'0715' THEN DATEFROMPARTS(Year(getdate())-1,08,1)
						ELSE DATEFROMPARTS(Year(getdate()),08,1) END AS PADate) A) ;
SET @FADate = (SELECT FADate FROM (
				SELECT  CASE WHEN SUBSTRING(replace(convert(varchar,getdate(),101),'/','') ,1,4)<'0715' THEN DATEFROMPARTS(Year(getdate())-1,09,1)
						ELSE DATEFROMPARTS(Year(getdate()),09,1) END AS FADate) A) ;

					
--SET @MandateCreatedDate0701 = '07/01/2022'	--automated
--SET @MandateCreatedDate0801 = '08/01/2022'	--automated
--Select  @PADate PADate, @FADate as FADate, @MandateCreatedDate0701 MandateCreatedDate0701, @MandateCreatedDate0801 MandateCreatedDate0801

Set @Date = 15
Set @Month = 7
Set @Schoolyear = SEO_MART.dbo.fn_DynamicSY(@Month, @Date)
--Select @SchoolYear as SchoolYear

Set @SchoolStartDate =	(Select MIN(CalendarDate) from SEO_MART.dbo.INT_SchoolCalendar with(nolock)
								Where SchoolYear = @SchoolYear)

--Select @SchoolStartDate as SchoolStartDate


  IF(@COUNT <> 0)

    BEGIN

    TRUNCATE TABLE dbo.INT_ProviderAssignmentLinkage;

    END;


BEGIN

If Object_id('tempdb..#RS') is not null
Drop Table #RS

SELECT * INTO #RS FROM (
Select Distinct StudentID,MatchKey,MatchKeyDuration,MatchKeyNL,RecommendedDurationNumeric,ServiceType
from dbo.INT_RelatedServices WITH(NOLOCK) where ActiveDocumentFlag='Y' and ActiveServiceFlag='Y' --and RecommendedDurationNumeric>0
) A


END;
------------------ Populate PAFirstFullAttendDate,FirmName,AssignmentStatusName,AgencyProvider columns -------------

BEGIN

If Object_id('tempdb..#RSPAMatchKey') is not null
Drop Table #RSPAMatchKey
 

Select  * into #RSPAMatchKey from (
			Select *,    ROW_NUMBER() OVER(PARTITION BY MatchKeyDuration ORDER BY   
								Case when FirstAttendDate is not null and FirstAttendDate > = (Case when LoadedSchoolSetting = A.LoadedSchoolSettingCharterLKV  then A.FirstAttendDateCharterLKV 
																														else A.FirstAttendDateNonCharterLKV --@SchoolStartDate	
																	 												End) 
																													Then FirstAttendDate 
									Else A.FirstAttendDateDefaultLKV 
								End ASC
								--CASE  WHEN FirstAttendDate <=@FADate OR FirstAttendDate IS NULL
--                                                  THEN '8/1/2999'ELSE FirstAttendDate END ASC
										,AssignmentID DESC ) RNK  
				from (
						Select  P.StudentID,P.MandateID,P.AssignmentID,P.ServiceType,P.MatchKey,R.MatchKeyDuration,PALanguageDesc,SESISLanguageDesc,P.RecommendedDurationMinutes,P.MandateStartDate,
						P.MandateEndDate,MandateStatusName,
						--Case when FirstAttendDate > = (Case when LoadedSchoolSetting = 'Charter' then @MandateCreatedDate0801 
						--								   else  @SchoolStartDate	
						--					 	        End) 
						--								Then FirstAttendDate 
						--	 else Null 
						--End as FirstAttendDate,
						FirstAttendDate,
						FirmName,AssignmentStatusName,
						Case when P.ProviderLastName is not null then SEO_MART.dbo.fn_INICap(P.ProviderLastName  ) +', '+ SEO_MART.dbo.fn_IniCap(P.ProviderFirstName) END AS AgencyProvider,P.ServiceStartDate,P.ServiceEndDate
						,P.SchoolYear,P.FirstAttendDelayFlag,P.FirstAttendDelayReason,P.MatchKeyNL, CASE WHEN R.RecommendedDurationNumeric-5<=P.RecommendedDurationMinutes THEN 1 ELSE 0 END PADuration,
						LoadedSchoolSetting, DocumentCreatedDate, CreatedBy, LK.*
							from #RS R
							CROSS APPLY #SEOLKValues LK
							LEFT JOIN dbo.INT_ProviderAssignment P 													
							on P.MatchKey=R.MatchKey 
							--Note on DocumentCreatedDateTime:
							--Raji: 9/13/2024 
							/*
							During PA rollover, new records are created with DocumentCreatedDateTime as that of the rollover date
							For rollover from SY24 to SY25, the PA rollover date was 8/8/2024
							CreatedDateNonCharterLKV is 8/1/2024 which is close to 8/8/2024. 
							So, use of CCreatedDateNonCharterLKV is acceptable in place of PARolloverDate
							*/
							and   DocumentCreatedDateTime >= LK.CreatedDateCharterLKV  
							and  (DocumentCreatedDateTime >= LK.CreatedDateNonCharterLKV or LK.CreatedByInitialLoadLKV LIKE '%'+CreatedBy+'%' OR LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
							and (
									FirstAttendDate is null 
									OR
									(
										( FirstAttendDate >= LK.FirstAttendDateCharterLKV and LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
										or
										(FirstAttendDate >= LK.FirstAttendDateNonCharterLKV and isnull(LoadedSchoolSetting, '') <> LK.LoadedSchoolSettingCharterLKV)
									)
								)
					) A 
				where  PADuration<>0
			) B Where RNK=1
		order by MatchKey

END;

------------------ Populate PAFirstPartialAttendDate column -------------

BEGIN

If Object_id('tempdb..#RSPAMatchKeyNL') is not null
Drop Table #RSPAMatchKeyNL

Select  * INTO #RSPAMatchKeyNL from (
Select *,    ROW_NUMBER() OVER(PARTITION BY MatchkeyNL ORDER BY  Case when FirstAttendDate is not null and FirstAttendDate > = (Case when LoadedSchoolSetting = A.LoadedSchoolSettingCharterLKV  then A.FirstAttendDateCharterLKV 
																																				else  A.FirstAttendDateNonCharterLKV--@SchoolStartDate	
																	 																		End) 
																																			Then FirstAttendDate 
															Else A.FirstAttendDateDefaultLKV
														End ASC,AssignmentID DESC, MatchKeyNL DESC) RNK  from (
Select P.MatchKeyNL,
--Case when FirstAttendDate > = (Case when LoadedSchoolSetting = 'Charter' then @MandateCreatedDate0801 
--																				   else  @SchoolStartDate	
--																	 	        End) 
--																				Then P.FirstAttendDate 
--													 else Null 
--												End as FirstAttendDate,
P.FirstAttendDate,
P.AssignmentID,
 CASE WHEN R.RecommendedDurationNumeric-5<=P.RecommendedDurationMinutes THEN 1 ELSE 0 END PADuration,LoadedSchoolSetting, DocumentCreatedDate, CreatedBy, LK.*
 from #RS R 
 CROSS APPLY #SEOLKValues LK
 LEFT JOIN dbo.INT_ProviderAssignment P on P.MatchKeyNL=R.MatchKeyNL 
 and   DocumentCreatedDateTime >= LK.CreatedDateCharterLKV 
 and  (DocumentCreatedDateTime >= LK.CreatedDateNonCharterLKV or LK.CreatedByInitialLoadLKV LIKE '%'+CreatedBy+'%' OR LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
	and (
			FirstAttendDate is null 
			OR
			(
				( FirstAttendDate >= LK.FirstAttendDateCharterLKV and LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
				or
				(FirstAttendDate >= LK.FirstAttendDateNonCharterLKV and isnull(LoadedSchoolSetting, '') <> LK.LoadedSchoolSettingCharterLKV)
			)
		)

) A where  PADuration<>0) B Where RNK=1
 order by MatchKeyNL

END;


------------------ Populate PAFirstAttendDateService column -------------


BEGIN

If Object_id('tempdb..#RSPAService') is not null
Drop Table #RSPAService

Select  * INTO #RSPAService 
from (
Select *,    ROW_NUMBER() OVER(PARTITION BY StudentID,ServiceType ORDER BY Case when FirstAttendDate is not null and FirstAttendDate > = (Case when LoadedSchoolSetting = A.LoadedSchoolSettingCharterLKV  then A.FirstAttendDateCharterLKV 
																																				else  A.FirstAttendDateNonCharterLKV--@SchoolStartDate	
																	 																		End) 
																																			Then FirstAttendDate 
															Else A.FirstAttendDateDefaultLKV
														End ASC,AssignmentID DESC) RNK  from (
Select P.StudentID,P.ServiceType,
--Case when FirstAttendDate > = (Case when LoadedSchoolSetting = 'Charter' then @MandateCreatedDate0801 
--																				   else  @SchoolStartDate	
--																	 	        End) 
--																				Then P.FirstAttendDate 
--													 else Null 
--												End as FirstAttendDate,
P.FirstAttendDate,
P.AssignmentID,
 CASE WHEN R.RecommendedDurationNumeric-5<=P.RecommendedDurationMinutes THEN 1 ELSE 0 END PADuration,LoadedSchoolSetting, DocumentCreatedDate, CreatedBy,LK.*
 from #RS R
  CROSS APPLY #SEOLKValues LK
 LEFT JOIN dbo.INT_ProviderAssignment P on P.StudentID=R.StudentID 
 and P.ServiceType=R.ServiceType 
 and DocumentCreatedDateTime >= LK.CreatedDateCharterLKV 
and  (DocumentCreatedDateTime >= LK.CreatedDateNonCharterLKV or LK.CreatedByInitialLoadLKV LIKE '%'+CreatedBy+'%' or LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
and (
		FirstAttendDate is null 
		OR
		(
			( FirstAttendDate >= LK.FirstAttendDateCharterLKV and LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
			or
			(FirstAttendDate >= LK.FirstAttendDateNonCharterLKV and isnull(LoadedSchoolSetting, '') <> LK.LoadedSchoolSettingCharterLKV)
		)
	)
) A where  PADuration<>0) B Where RNK=1
 order by StudentID,ServiceType

END;


----------------- Populate temporary table with RS calculated columns    ------


BEGIN

If Object_id('tempdb..#RSPA') is not null
Drop Table #RSPA

Select * INTO #RSPA from (
Select R.StudentID,MandateID,R.AssignmentID,R.ServiceType,MatchKey,R1.MatchKeyNL,MatchKeyDuration,R.FirstAttendDate PAFirstFullAttendDate ,
FirmName,AssignmentStatusName,AgencyProvider,R1.FirstAttendDate PAFirstPartialAttendDate,R2.FirstAttendDate PAFirstAttendDateService,PALanguageDesc,
SESISLanguageDesc,RecommendedDurationMinutes,MandateStartDate,MandateEndDate,MandateStatusName,ServiceStartDate,
ServiceEndDate,SchoolYear,FirstAttendDelayFlag,FirstAttendDelayReason,R.LoadedSchoolSetting, R.DocumentCreatedDate, R.CreatedBy
FROM #RSPAMatchKey R
LEFT JOIN #RSPAMatchKeyNL R1 on R.MatchKeyNL=R1.MatchKeyNL
LEFT JOIN #RSPAService R2 on R.StudentID=R2.StudentID  and R.ServiceType=R2.ServiceType) A 
END;

BEGIN
INSERT INTO dbo.INT_ProviderAssignmentLinkage
(
StudentID,
MandateID,
AssignmentID,
ServiceType,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
FirstAttendDate,
FirmName,
AssignmentStatusName,
AgencyProvider,
PALanguageDesc,
SESISLanguageDesc,
RecommendedDurationMinutes,
MandateStartDate,
MandateEndDate,
MandateStatusName,
ServiceStartDate,
ServiceEndDate,
SchoolYear,
FirstAttendDelayFlag,
FirstAttendDelayReason,
ProcessedDate,
ProcessedDateTime,
LoadedSchoolSetting, 
DocumentCreatedDate,
CreatedBy)


SELECT StudentID,
MandateID,
AssignmentID,
ServiceType,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
CASE WHEN ((LoadedSchoolSetting = LKI.LoadedSchoolSettingCharterLKV and FirstAttendDate >= LKI.FirstAttendDateCharterLKV) 
		OR 
		(LKI.LoadedSchoolSettingNonCharterLKV LIKE '%'+LoadedSchoolSetting+'%' and FirstAttendDate >= LKI.FirstAttendDateNonCharterLKV)) 
	THEN 
		FirstAttendDate ELSE NULL 
	END AS FirstAttendDate,
FirmName,
AssignmentStatusName,
AgencyProvider,
PALanguageDesc,
SESISLanguageDesc,
RecommendedDurationMinutes,
MandateStartDate,
MandateEndDate,
MandateStatusName,
ServiceStartDate,
ServiceEndDate,
SchoolYear,
FirstAttendDelayFlag,
FirstAttendDelayReason,
GetDate()  ProcessedDate,
GetDate() ProcessedDateTime, 
LoadedSchoolSetting, 
DocumentCreatedDate,
CreatedBy
FROM (
		Select  StudentID,
		MandateID,
		AssignmentID,
		ServiceType,
		MatchKey,
		MatchKeyNL,
		MatchKeyDuration,
		PAFirstFullAttendDate,
		PAFirstPartialAttendDate,
		PAFirstAttendDateService,
		CONVERT(DATE,NULL)FirstAttendDate,
		FirmName,
		AssignmentStatusName,
		AgencyProvider,
		PALanguageDesc,
		SESISLanguageDesc,
		RecommendedDurationMinutes,
		MandateStartDate,
		MandateEndDate,
		MandateStatusName,
		ServiceStartDate,
		ServiceEndDate,
		SchoolYear,
		FirstAttendDelayFlag,
		FirstAttendDelayReason,
		LoadedSchoolSetting, 
		DocumentCreatedDate,
		CreatedBy
		 from #RSPA 

 UNION ALL 

	 SELECT 
	 StudentID,
	MandateID,
	AssignmentID,
	ServiceType,
	MatchKey,
	MatchKeyNL,
	MatchKeyDuration,
	CASE WHEN ServiceType=ServiceTypeATLKV THEN FirstAttendDate ELSE CONVERT(DATE,NULL) END AS PAFirstFullAttendDate,
	CONVERT(DATE,NULL) PAFirstPartialAttendDate,
	CONVERT(DATE,NULL) PAFirstAttendDateService,
	--Case when FirstAttendDate > = (Case when LoadedSchoolSetting = 'Charter' then @MandateCreatedDate0801 
	--																			   else  @SchoolStartDate	
	--																 	        End) 
	--																			Then FirstAttendDate 
	--												 else Null 
	--											End as FirstAttendDate,
	FirstAttendDate,
	FirmName,
	AssignmentStatusName,
	Case when ProviderLastName is not null then SEO_MART.dbo.fn_INICap(ProviderLastName  ) +', '+ SEO_MART.dbo.fn_IniCap(ProviderFirstName) END AS AgencyProvider,
	PALanguageDesc,
	SESISLanguageDesc,
	RecommendedDurationMinutes,
	MandateStartDate,
	MandateEndDate,
	MandateStatusName,
	ServiceStartDate,
	ServiceEndDate,
	SchoolYear,
	FirstAttendDelayFlag,
	FirstAttendDelayReason,
	LoadedSchoolSetting, 
	DocumentCreatedDate,
	CreatedBy 
	FROM (
  
	SELECT *, ROW_NUMBER() OVER(PARTITION BY MatchKey,SchoolYear ORDER BY Case when FirstAttendDate > = (Case when LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV  then LK.FirstAttendDateCharterLKV else LK.FirstAttendDateNonCharterLKV--@SchoolStartDate	
	End) Then FirstAttendDate Else LK.FirstAttendDateDefaultLKV End ASC,AssignmentID DESC, MandateID DESC) RNK
	FROM dbo.INT_ProviderAssignment P
	CROSS APPLY #SEOLKValues LK
	WHERE DocumentCreatedDateTime >= LK.CreatedDateCharterLKV 
	and  (DocumentCreatedDateTime >= LK.CreatedDateNonCharterLKV or LK.CreatedByInitialLoadLKV LIKE '%'+CreatedBy+'%' or LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
	and (
			FirstAttendDate is null 
			OR
			(
				( FirstAttendDate >= LK.FirstAttendDateCharterLKV and LoadedSchoolSetting = LK.LoadedSchoolSettingCharterLKV)
				or
				(FirstAttendDate >= LK.FirstAttendDateNonCharterLKV and isnull(LoadedSchoolSetting, '') <> LK.LoadedSchoolSettingCharterLKV)
			)
		)

	and not exists (Select Distinct ServiceType from #RSPA R where R.ServiceType=P.ServiceType) 													
	) PA  WHERE RNK = 1 ) UN
	CROSS APPLY #SEOLKValues LKI
	;

END;

END;
GO


