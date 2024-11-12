USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport9]    Script Date: 11/12/2024 3:23:53 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[USPCC_AnnaulReport9] 
@tableNameCCInitialReferralsR19 varchar(100) = ''
--@tableNameINTStudentDemographics_0630 varchar(100) = ''
	
AS
/************************************************************************************************************************
Program				       : AnnualReport.sas
Purpose				       : 1.To create an Initial City council tri-annuals report and generate redacted output.(Note: Run till Part:1 , 
Project				       : City council
Programmer			       : Charlotte Wang
Creation /Finalized Date   : Finalized on 11/01/2023
Created		               : 11/9/2023  Created Stored Procedure using Existing SAS Scripts: 
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi			06/25/2024		Replaced TempResFlag with STHFlag to identify students in temporary housing 
Charlotte Wang            10/08/2024      Made changes in the order of the columns HousingType and STHFlag in Temptable for the story MIS-12124
************************************************************************************************************************/

BEGIN

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCInitialReferralsR19, '') = ''
	begin
		set @tableNameCCInitialReferralsR19 = 'CC_InitialReferralsR19_SY' + @currYear_YY
	end 

	--if isnull(@tableNameINTStudentDemographics_0630, '') = ''
--	begin
--		set @tableNameINTStudentDemographics_0630 = 'INT_StudentDemographics_0630' + @currYear_YY
--	end 

if object_id('tempdb..##Report_Plac') is not null
	drop table ##Report_Plac

CREATE TABLE ##Report_Plac(
	[StudentID] [int] NOT NULL,
	[ProfileIDT] [int] NULL,
	[FirstName] [varchar](50) NULL,
	[LastName] [varchar](50) NULL,
	[AdminDistrict] [varchar](2) NULL,
	[ReportingDistrict] [varchar](7) NULL,
	[MealStatusGrouping] [varchar](50) NULL,
	[Gender] [varchar](50) NULL,
	[EthnicityGroupCC] [varchar](50) NULL,
	[GradeLevel] [varchar](25) NULL,
	[BirthYear] [int] NULL,
	[AgeSchoolStart] [int] NULL,
	[ELLStatus] [varchar](50) NULL,
	[OutcomeLanguage] [varchar](50) NULL,
	[OutcomeLanguageCC] [varchar](50) NULL,
	[HomeDistrict] [varchar](7) NULL,
	[EnrolledSchoolDBN] [varchar](10) NULL,
	[EnrolledSchoolType] [varchar](15) NULL,
	[ComplianceSchoolDBN] [varchar](10) NULL,
	[ComplianceSchoolType] [varchar](7) NULL,
	[ReferralSchoolDBN] [varchar](10) NULL,
	[ReferralSchoolType] [varchar](7) NULL,
	[OutcomeSchoolDBN] [varchar](10) NULL,
	[OutcomeSchoolType] [varchar](7) NULL,
	[PlacementSchoolDBN] [varchar](10) NULL,
	[PlacementSchoolType] [varchar](7) NULL,
	[SchoolYear] [varchar](9) NULL,
	[ReferralDocumentIDT] [int] NULL,
	[ReferralTypeCode] [int] NULL,
	[ReferralTypeCC] [varchar](7) NULL,
	[ConsentDocumentIDT] [int] NULL,
	[OutcomeDocumentIDT] [int] NULL,
	[OutcomeTypeCode] [int] NULL,
	[OutcomeTypeDesc] [varchar](50) NULL,
	[PlacementDocumentIDT] [int] NULL,
	[ReportOutcomeCC] [varchar](25) NULL,
	[ReportOutcome] [varchar](25) NULL,
	[InactiveDate] [date] NULL,
	[ReferralDate] [date] NULL,
	[ConsentDate] [date] NULL,
	[AssessmentDate] [date] NULL,
	[OutcomeDate] [date] NULL,
	[ProjectedIEPImplementationDate] [date] NULL,
	[ImplementationSchoolDays] [int] NULL,
	[IEPConferenceStatus] [varchar](20) NULL,
	[EffectiveDate] [date] NULL,
	[PlacementDate] [date] NULL,
	[OutcomePlacementSchoolDays] [int] NULL,
	[LocationLetterDate] [date] NULL,
	[ConsentProvisionServiceDate] [date] NULL,
	[ComplianceStartDate] [date] NULL,
	[ComplianceEndDateCC] [date] NULL,
	[IEPMeetingComplianceCC] [int] NULL,
	[IEPComplianceMetricCC] [varchar](15) NULL,
	[IsPWNDeferred] [bit] NULL,
	[ReferralSchoolYear] [varchar](9) NULL,
	[OutcomeSchoolYear] [varchar](9) NULL,
	[ReasonForRecommendPlacement] [int] NULL,
	[RecommendPlacementDesc] [varchar](70) NULL,
	[PriorNoticeSelectionDesc] [varchar](60) NULL,
	[IsRevision] [bit] NULL,
	[IsAmendIEP] [bit] NULL,
	[IsReconveneIEP] [bit] NULL,
	[IsFirstReeval] [bit] NULL,
	[ReferralSource] [int] NULL,
	[ReferralSourceDesc] [varchar](150) NULL,
	[LanguageofAssessment] [varchar](50) NULL,
	[ReasonForDelayDesc] [varchar](169) NULL,
	[DisabilityCode] [int] NULL,
	[ClassificationDesc] [varchar](50) NULL,
	[Is12MonthYesView] [bit] NULL,
	[ReferralCreatedDate] [datetime] NULL,
	[ReferralFinalizedDate] [datetime] NULL,
	[ConsentCreatedDate] [datetime] NULL,
	[ConsentFinalizedDate] [datetime] NULL,
	[AssessmentCreatedDate] [datetime] NULL,
	[AssessmentFinalizedDate] [datetime] NULL,
	[OutcomeCreatedDate] [datetime] NULL,
	[OutcomeFinalizedDate] [datetime] NULL,
	[PlacementCreatedDate] [datetime] NULL,
	[PlacementFinalizedDate] [datetime] NULL,
	[ProcessedDateTime] [datetime] NULL,
	[ProcessedDate] [date] NULL,
	[TempResFlag] [varchar](1) NULL,
	HousingType varchar(50) null,
	STHFlag char(1) NULL,
	[FosterCareFlag] [varchar](1) NOT NULL
)

Declare @SQL varchar(max) = 'INSERT INTO ##Report_Plac '+
' select a.* ' +
' from SEO_Mart.snap.'+@tableNameCCInitialReferralsR19 +' a' + --@CC_InitialReferralsR19_SY23_fix
--' left join SEO_Mart.snap.'+@tableNameINTStudentDemographics_0630 +' c '+
--' on a.studentid=c.studentid '+
' where a.GradeLevel <> '+'''PK'''+
' and a.GradeLevel <> '+'''99'''+
' and a.ReportingDistrict <> '+'''00'''

exec (@SQL)

update ##Report_Plac set GradeLevel = 'KG' where GradeLevel = '0K'

if object_id('tempdb..##Report9') is not null
	drop table ##Report9
Select  StudentID 
	   ,ReportingDistrict 
	   ,ReportOutcomeCC 
	   ,MealStatusGrouping 
	   ,EthnicityGroupCC 
	   ,STHFlag
	   ,case when FosterCareFlag = 'Y' then 'Yes' else 'No' end as FosterCareFlag
	   ,case when IsPWNDeferred  = 0 and  ReportOutcomeCC  = 'IEP' then 1 
	   else 0
	   end as PWN_FLG 
	   ,case when EthnicityGroupCC  = 'Asian' then 1
	   when EthnicityGroupCC   = 'Black' then 2
	   when EthnicityGroupCC   = 'Hispanic' then 3
	   when EthnicityGroupCC  = 'White' then 4
	   when EthnicityGroupCC  = 'Other' then 5
	   end as Ethnicity_sort
	   ,GradeLevel 
	   ,OutcomeLanguageCC 
	   ,GENDER 
	   ,case when  EllStatus  is null then 'NOT ELL'
	   else EllStatus 
	   end as EllStatus
	   , 1 AS   TOTAL_CLASSIFIED 
	   ,PlacementDate
	   ,OutcomePlacementSchoolDays
	   ,case when  OutcomeLanguageCC   = 'ENGLISH' then 1
	   when  OutcomeLanguageCC   = 'SPANISH' then 2
	   when  OutcomeLanguageCC   = 'CHINESE' then 3
	   when  OutcomeLanguageCC   = 'OTHER' then 4
	   when  OutcomeLanguageCC   = 'NOT APPLICABLE' then 5
	   end as Language_Sort
	   ,case when  GradeLevel  = 'KG' then 1 
	   when  GradeLevel  = '01' then 2
	   when  GradeLevel  = '02' then 3
	   when  GradeLevel  = '03' then 4
	   when  GradeLevel  = '04' then 5
	   when  GradeLevel  = '05' then 6
	   when  GradeLevel  = '06' then 7
	   when  GradeLevel  = '07' then 8
	   when  GradeLevel  = '08' then 9
	   when  GradeLevel  = '09' then 10
	   when  GradeLevel  = '10' then 11
	   when  GradeLevel  = '11' then 12
	   when  GradeLevel  = '12' then 13
	   end as Grade_Sort
	    ,case when STHFlag = 'Y' then 1
	   when STHFlag  = 'N' then 2
	    end as STHFlagSort
	   ,case when FosterCareFlag = 'Y' then 1
	   when FosterCareFlag  = 'N' then 2
	    end as FosterCareFlagSort
	into ##Report9
    From ##Report_Plac
	where  ReportingDistrict  not in ('98', '99','00')
	 and  IsPWNDeferred  = 0 and  ReportOutcomeCC  = 'IEP' 
	  and PlacementDate is not null
	 ;

if object_Id('tempdb..##group_and_sort_fields') is not null
	drop table ##group_and_sort_fields
create table ##group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))

insert into ##group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'Gender'),
(5, 'ELLStatus')

insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
(6, 'OutcomeLanguageCC', 'Language_Sort'),
(7, 'GradeLevel', 'Grade_Sort'),
(8, 'STHFlag', 'STHFlagSort'),
(9, 'FostercareFlag', 'FosterCareFlagSort')


	if object_id('tempdb..##totalRow') is not null
	 drop table ##totalRow 
	 	    
	  select 
	  'Total' as 'Header',
	   FORMAT(count([StudentID]),'#,##0') as 'Students'
	  ,FORMAT(cast((sum(OutcomePlacementSchoolDays)*1.0)/count(StudentID)  as numeric(8,2)),'N') as Average_Days
	   into ##totalRow
	  from ##Report9
	 
	if object_id('tempdb..##totalRow_Sort') is not null
	drop table ##totalRow_Sort 
	 	    
	  select 
	  '99' as 'Sort',
	  'Total' as 'Header',
	   FORMAT(count([StudentID]),'#,##0') as 'Students'
	  ,FORMAT(cast((sum(OutcomePlacementSchoolDays)*1.0)/count(StudentID)  as numeric(8,2)),'N') as Average_Days
	  into ##totalRow_Sort
	  from ##Report9
	 


Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
select @rowCount = count(*) from ##group_and_sort_fields
declare @outputSQL nvarchar(max)
while @i <= @rowCount 
begin
	select @groupBy = '', @sortBy = '', @outputSQL = ''
	select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
	from ##group_and_sort_fields where outputOrderID = @i 

	select @outputSQL =  
	case when @sortBy != '' then 'select '+@groupBy+', TOTAL_PWN,Average_Days   from ( ' else ' ' end +
' select * from '+
' ( '+
' Select   ' + case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end  
+ case when @sortBy = ''
		then  @groupBy +' as sort '
		when  @i = 8 then ' case when '+@groupBy + ' = ' +'''Y'''+' then '+'''Yes'''+' else '+'''No'''+'  end as STHFlag'
		else  @groupBy  end  + 
	  ', FORMAT(count(StudentID) ,''#,##0'') as TOTAL_PWN ' +
	  -- ',FORMAT(cast((sum(OutcomePlacementSchoolDays)*1.0)/count(StudentID)  as numeric(8,2)),''#,##0'') as Average_Days ' +
       ' ,CAST(AVG( OutcomePlacementSchoolDays * 1.0 ) AS DECIMAL(10,2)) as Average_Days ' +
 ' FROM ##Report9' +
 case when @i =8 then ' where STHFlag in ('+'''Y'''+', '+'''N'''+') ' 
	 else ' ' end 
+' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow ' else '##TotalRow_Sort ' end +
case when @sortBy != '' then ' ) a order by sort ' else ' order by sort ' end



 print(@outputSQL)
	execute(@outputSQL)


	
	
	select @i = @i + 1
end

	select 'Checking records count in ###Report_Plac '
	select count(*) from ##Report_Plac

	select 'Checking records count in #Report '
	select count(*) from ##Report9

end
GO


