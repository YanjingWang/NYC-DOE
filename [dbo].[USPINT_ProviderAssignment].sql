USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPINT_ProviderAssignment]    Script Date: 12/9/2024 9:34:22 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE  PROCEDURE [dbo].[USPINT_ProviderAssignment]
AS
     BEGIN
         SET XACT_ABORT ON;
         SET NOCOUNT ON;

/**************************************************************************************************************************************************
Object Name: USP_INTProviderAssignment
Purpose: Populate Provider Assignment reporting data in SEO_MART database
Date Created: 06/13/2020

Modification Details:

Author				ModifiedDate	Comments
Phani Marupaka		10/27/2020		Populate all PA records created after 01-August-2020
Phani Marupaka		06/23/2021		Rename DocumentCreatedDate to DocumentCreatedDateTime
Phani Marupaka		06/23/2021	    Add DocumentCreatedDate column to INT_ProviderAssignment
Phani Marupaka		06/23/2021	    Modify MandateStartDate,MandateEndDate,ServiceStartDate,ServiceEndDate columns from DateTime to date
Christopher Agwu	08/19/2022		Added columns (LoadedSchoolSetting, CreatedBy) per Raja script
Sergey G			04/11/2023		replaced prior year demographics SEO_MART.snap.YOY_StudentDemographics_0701 with current dbo.INT_StudentDemographics
***************************************************************************************************************************************************/

DECLARE @PriorSchoolYear varchar(9) -- PriorSchoolYear added by SG on 04/11/2023, for clarity
DECLARE @COUNT INT, @Date Int, @Month Int, @SchoolYear Varchar(9)
DECLARE @DateCreated DATETIME;
DECLARE @FirstAttend DATETIME;
SET @DateCreated = '8/1/2018';
SET @FirstAttend = '9/1/2018';
Set @Date = 15
Set @Month = 7
Set @SchoolYear = SEO_MART.dbo.fn_DynamicSY(@Month, @Date)	-- current Schoo Year
--Set @SchoolYear = Convert(Varchar,LEFT(@SchoolYear,4)-1) + '-' + Convert(Varchar,RIGHT(@SchoolYear,4)-1) 
Set @PriorSchoolYear = Convert(Varchar,LEFT(@SchoolYear,4)-1) + '-' + Convert(Varchar,RIGHT(@SchoolYear,4)-1) -- renamed to PriorSchoolYear by SergeyG for clarity

SET @COUNT = (SELECT COUNT(*) FROM dbo.INT_ProviderAssignment);

  IF(@COUNT <> 0)

    BEGIN

    TRUNCATE TABLE dbo.INT_ProviderAssignment;

    END;

BEGIN


If Object_ID('tempdb..#INT_ProviderAssignment') is not null
Drop Table #INT_ProviderAssignment

  SELECT *  INTO #INT_ProviderAssignment FROM
(
    SELECT StudentID,
			MandateID,
			AssignmentID,
           MandateStatusID,
           MandatestatusName,
           serviceTypeCode,
           serviceTypeName serviceType,
           PALanguage PALanguageCode,  
           CASE WHEN  PALanguageDesc in ('FRENCH-HAITIAN CREOLE','Haitian-Creole') THEN 'Haitian Creole' ELSE PALanguageDesc END AS  PALanguageDesc,
           CASE WHEN  SESISLanguageDesc in ('FRENCH-HAITIAN CREOLE','Haitian-Creole') THEN 'Haitian Creole' ELSE SESISLanguageDesc END AS SESISLanguageDesc,
           MandateCreatedDate,
           MandateStartDate,
           MandateEndDate,
		   CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN ServiceStartDate		ELSE NULL	END ServiceStartDate,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN ServiceEndDate			ELSE NULL	END ServiceEndDate,
			SchoolYear,                
           RecommendedFrequency,
           RecommendedGroupSize,
           RecommendedDuration,
           AttendingAdminDBN,
           AuthorizedAdminDBN,
           AttendingPhysicalLocationDBN,           
           AuthPhysicalLocationDBN,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN FirstAttendDelayReason	ELSE NULL	END FirstAttendDelayReason,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN FirstAttendDelayFlag	ELSE NULL	END FirstAttendDelayFlag,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN AssignmentStatusID		ELSE NULL	END AssignmentStatusID,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN AssignmentStatusName	ELSE NULL	END AssignmentStatusName,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN FirstAttendDate		ELSE NULL	END FirstAttendDate,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN FirmName				ELSE NULL	END FirmName,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN HRHubID				ELSE NULL	END HRHubID,
		   CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN ADEmpID				ELSE NULL	END EmployeeID,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN ProviderLastName		ELSE NULL	END ProviderLastName,
           CASE WHEN isnull(FirstAttendDate, '8/1/1888') >= @FirstAttend	THEN ProviderFirstName		ELSE NULL	END ProviderFirstName,
           MatchKey,
		   MatchKeyNL,
           MatchKey+' '+isnull(Convert(varchar(10),RecommendedDuration),'') as MatchKeyDuration,
		   CreatedBy        
    
    FROM dbo.DWH_ProviderAssignment 
    WHERE MandateCreatedDate >= @DateCreated and IsDelete=0) PA  ;

END;

BEGIN

INSERT INTO dbo.INT_ProviderAssignment
(
StudentID,
MandateID,
AssignmentID,
MandateStatusID,
MandateStatusName,
ServiceTypeCode,
ServiceType,
PALanguageCode,
PALanguageDesc,
SESISLanguageDesc,
DocumentCreatedDateTime,
MandateStartDate,
MandateEndDate,
ServiceStartDate,
ServiceEndDate,
SchoolYear, 
RecommendedFrequencyNumeric,
RecommendedGroupSize,
RecommendedDurationMinutes,
AttendingAdminDBN,
AuthorizedAdminDBN,
AttendingPhysicalLocationDBN,
AuthPhysicalLocationDBN,
FirstAttendDelayReason,
FirstAttendDelayFlag,
AssignmentStatusID,
AssignmentStatusName,
FirstAttendDate,
FirmName,
HRHubID,
EmployeeID,
ProviderLastName,
ProviderFirstName,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
DocumentCreatedDate,
CreatedBy,
ProcessedDate,
ProcessedDateTime
)

SELECT
StudentID,
MandateID,
AssignmentID,
MandateStatusID,
MandateStatusName,
ServiceTypeCode,
ServiceType,
PALanguageCode,
PALanguageDesc,
SESISLanguageDesc,
MandateCreatedDate DocumentCreatedDate,
CAST(MandateStartDate as DATE) MandateStartDate,
CAST(MandateEndDate as DATE) MandateEndDate,
CAST(ServiceStartDate as DATE) ServiceStartDate,
CAST(ServiceEndDate as DATE) ServiceEndDate,
SchoolYear,
RecommendedFrequency,
RecommendedGroupSize,
RecommendedDuration,
AttendingAdminDBN,
AuthorizedAdminDBN,
AttendingPhysicalLocationDBN,
AuthPhysicalLocationDBN,
FirstAttendDelayReason,
FirstAttendDelayFlag,
AssignmentStatusID,
AssignmentStatusName,
FirstAttendDate,
FirmName,
HRHubID,
EmployeeID,
ProviderLastName,
ProviderFirstName,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
CAST(MandateCreatedDate as DATE) DocumentCreatedDate,
CreatedBy,
getdate() as ProcessedDate,
getdate() as ProcessedDateTime
 FROM #INT_ProviderAssignment

END;	 

/* Commented out on 4/5/2023 by SergeyG: switch from using Prior SchoolYear demographics 
--	to using current year data in dbo.INT_StudentDemographics:
Update PA
	Set LoadedSchoolSetting = SD.EnrolledSchoolSetting
from dbo.INT_ProviderAssignment PA with(nolock)
	join SEO_MART.snap.YOY_StudentDemographics_0701 SD with(nolock)
on PA.StudentID = SD.StudentID
	Where SD.SchoolYear = @PriorSchoolYear
*/
Update PA
	Set LoadedSchoolSetting = SD.EnrolledSchoolSetting
	from		  dbo.INT_ProviderAssignment	PA with(nolock)
	join SEO_Mart.dbo.INT_StudentDemographics	SD with(nolock)
	  on PA.StudentID = SD.StudentID
	Where SD.SchoolYear = @SchoolYear	-- "Where" is left for protection only, as current data table holds the latest SchoolYear (Sergey G, 04/11/2023)
;
END;


GO


