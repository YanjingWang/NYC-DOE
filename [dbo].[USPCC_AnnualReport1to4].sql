USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport1to4]    Script Date: 11/12/2024 10:36:09 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[USPCC_AnnaulReport1to4]
@tableNameCCInitialReferralsR19 varchar(100) = ''
--@tableNameINTStudentDemographics_0630 varchar(100) = ''
AS
/************************************************************************************************************************
Program				       : Initials.sas
Purpose				       : 1.To create an Initial City council report and generate redacted output.(Note: Run till Part:1 , commenting test_arrays to get unredacted outputs)
					         2.Generate an RTF document using Proc report
					         3.To load data(redacted/unredacted) into the Excel report
Project				       : City council

--exec USPCC_AnnaulReport1to4 'CC_InitialReferralsR19_SY23'

8/29/2019:  
Updated variable names. 
Updated source table
Switched references from Hema's personal drives to City Council folder on R drive. 
Updated year. 
Removed redaction logic.
Excluded District 00

Date Created: 11/02/2023
Modification Details:

Author			ModifiedDate		Comments
Charlotte Wang			01/02/2023			Initial version created this SQL script based on SAS code for Reports 1-4
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART
Charlotte Wang	06/25/2024			Replaced TempResFlag with STHFlag
Charlotte Wang        10/08/2024      Made changes in the order of the columns HousingType and STHFlag in Temptable for the story MIS-12124
************************************************************************************************************************/
BEGIN

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)

	
	if isnull(@tableNameCCInitialReferralsR19, '') = ''
	begin
		set @tableNameCCInitialReferralsR19 = 'CC_InitialReferralsR19_SY' + @currYear_YY
	end

	/*if isnull(@tableNameINTStudentDemographics_0630, '') = ''
	begin
		set @tableNameINTStudentDemographics_0630 = 'INT_StudentDemographics_0630' + @currYear_YY
	end
	*/

if object_id('tempdb..##Report_Ini') is not null
	drop table ##Report_Ini

CREATE TABLE ##Report_Ini(
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
	[TempResFlag] char(1) NULL,
	[HousingType] varchar(50) NULL,
	[STHFlag] char(1) NULL,
	[FosterCareFlag] [varchar](1) NOT NULL
)

DECLARE @SQL VARCHAR(MAX) =
' insert into ##Report_Ini '+
'select a.* '+
' from SEO_Mart.snap.'+@tableNameCCInitialReferralsR19 +' a '

 print(@SQL)
execute (@SQL)

update ##Report_Ini set GradeLevel = 'KG' where GradeLEvel = '0K'
/*
select top 10 * from ##Report_Ini
*/
if object_id('tempdb..##Report_Working') is not null
	drop table ##Report_Working
Select studentid,
	    ReportingDistrict
	   ,ReportOutcomeCC
	   ,1 as STUDENTS_WITH_REF
	   ,MealStatusGrouping
	   ,EthnicityGroupCC
	   	,STHFlag
  
	   ,case when EthnicityGroupCC = 'Asian' then 1
	   when EthnicityGroupCC  = 'Black' then 2
	   when EthnicityGroupCC  = 'Hispanic' then 3
	   when EthnicityGroupCC = 'White' then 4
	   when EthnicityGroupCC = 'Other' then 5
	   end as EthnicityGroupCC_sort
	   ,a.GradeLevel
	   ,OutcomeLanguageCC
	   ,a.GENDER
	   ,case when ELLStatus is null then 'NOT ELL'
	   else ELLStatus
	   end as ELLStatus
	   ,(case when ReportOutcomeCC = 'IEP' 
	   and IEPComplianceMetricCC = '<= 60 Days'
	   then 1
	   else 0
	   end + 
	   case when ReportOutcomeCC = 'IEP' 
	   and IEPComplianceMetricCC = '> 60 Days'
	   then 1
	   else 0
	   end)  as TOTAL_CLASSIFIED
	   ,case when ReportOutcomeCC = 'Open' then 1
	   else 0 
	   end as TOTAL_OPEN
	   ,case when ReportOutcomeCC = 'Awaiting' then 1
	   else 0 
	   end as TOTAL_AWAITING
	   ,case when ReportOutcomeCC = 'Caseclose' then 1
	   else 0 
	   end as CLOSED_WITHOUT_IEP
	   ,case when ReportOutcomeCC = 'Ineligible' then 1
	   else 0 
	   end as TOTAL_INELIGIBLE
	   ,case when ReportOutcomeCC = 'IEP' 
	   and IEPComplianceMetricCC = '<= 60 Days'
	   then 1
	   else 0
	   end as CLASSIFIED_LESS_60
	   ,case when ReportOutcomeCC = 'IEP' 
	   and IEPComplianceMetricCC = '> 60 Days'
	   then 1
	   else 0
	   end as CLASSIFIED_MORE_60
	   ,case when ReportOutcomeCC = 'Ineligible' 
	   and IEPComplianceMetricCC = '<= 60 Days'
	   then 1
	   else 0
	   end as INELIGIBLE_LESS_60
	   ,case when ReportOutcomeCC = 'Ineligible' 
	   and IEPComplianceMetricCC = '> 60 Days'
	   then 1
	   else 0
	   end as INELIGIBLE_MORE_60
	   ,case when a.GradeLevel = '0K' then 1 
	   when a.GradeLevel = '01' then 2
	   when a.GradeLevel = '02' then 3
	   when a.GradeLevel = '03' then 4
	   when a.GradeLevel = '04' then 5
	   when a.GradeLevel = '05' then 6
	   when a.GradeLevel = '06' then 7
	   when a.GradeLevel = '07' then 8
	   when a.GradeLevel = '08' then 9
	   when a.GradeLevel = '09' then 10
	   when a.GradeLevel = '10' then 11
	   when a.GradeLevel = '11' then 12
	   when a.GradeLevel = '12' then 13
	   end as GradeLevel_Sort
	    ,case when STHFlag = 'Y' then 1
	   when STHFlag  = 'N' then 2
	    end as STHFlagSort
	   ,FosterCareFlag
	    ,case when FosterCareFlag = 'Y' then 1
	   when FosterCareFlag  = 'N' then 2
	    end as FosterCareFlagSort
	into ##Report_Working 
	FROM ##Report_Ini  a
	WHERE ReportingDistrict <> '00' ;

if object_id('tempdb..##Report_Final14') is not null
	drop table ##Report_Final14;
with cteReport as 
(
	select *, case when CLOSED_WITHOUT_IEP=1 or INELIGIBLE_LESS_60=1 or INELIGIBLE_MORE_60=1 or TOTAL_OPEN=1 or TOTAL_AWAITING=1 then 'UNDETERMINED'
	when OutcomeLanguageCC = 'ENGLISH' then 'ENGLISH'
	   when OutcomeLanguageCC = 'SPANISH' then 'SPANISH'
	   when OutcomeLanguageCC = 'CHINESE' then 'CHINESE'
	   when OutcomeLanguageCC = 'OTHER' then 'OTHER'
	  end as LanguageOfInstructionCC2  
	from ##Report_Working 
) 
select *, case when LanguageOfInstructionCC2 = 'ENGLISH' then 1
	   when LanguageOfInstructionCC2 = 'SPANISH' then 2
	   when LanguageOfInstructionCC2 = 'CHINESE' then 3
	   when LanguageOfInstructionCC2 = 'OTHER' then 4
	   when LanguageOfInstructionCC2 = 'UNDETERMINED' then 5
	   end as Language_Sort
into ##Report_Final14
from cteReport 




if object_id('Tempdb..##totalRow') is not null
	drop table ##totalRow
Select  
    'Total' as 'Header'
	,FORMAT(sum(STUDENTS_WITH_REF), '#,##0') as c1 
    ,FORMAT(sum(CLOSED_WITHOUT_IEP), '#,##0') as c2
	,FORMAT(sum(INELIGIBLE_LESS_60), '#,##0') as c3
    ,FORMAT(sum(INELIGIBLE_MORE_60), '#,##0') as c4
	,FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)), '#,##0') as c5
    ,FORMAT(sum(CLASSIFIED_LESS_60), '#,##0') as c6
    ,FORMAT(sum(CLASSIFIED_MORE_60), '#,##0') as c7
    ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60), '#,##0') as C8 
	,FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)), '#,##0') as c9 
	,FORMAT(sum(TOTAL_AWAITING), '#,##0') as c10		
	,FORMAT(sum(TOTAL_OPEN), '#,##0') as c11 
into ##TotalRow
FROM ##Report_Final14

if object_id('Tempdb..##totalRow_Sort') is not null
	drop table ##totalRow_Sort 
Select  
    '99' as 'sort'
	,'Totals' as 'Header'
	,FORMAT(sum(STUDENTS_WITH_REF), '#,##0') as c1 
    ,FORMAT(sum(CLOSED_WITHOUT_IEP), '#,##0') as c2
	,FORMAT(sum(INELIGIBLE_LESS_60), '#,##0') as c3
    ,FORMAT(sum(INELIGIBLE_MORE_60), '#,##0') as c4
	,FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)), '#,##0') as c5
    ,FORMAT(sum(CLASSIFIED_LESS_60), '#,##0') as c6
    ,FORMAT(sum(CLASSIFIED_MORE_60), '#,##0') as c7
    ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60), '#,##0') as C8 
	,FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)), '#,##0') as c9 
	,FORMAT(sum(TOTAL_AWAITING), '#,##0') as c10		
	,FORMAT(sum(TOTAL_OPEN), '#,##0') as c11 
into ##TotalRow_Sort
FROM ##Report_Final14

if object_Id('tempdb..##group_and_sort_fields') is not null
	drop table ##group_and_sort_fields

create table ##group_and_sort_fields
(
outputOrderID int, 
groupBy varchar(100), 
sortBy varchar(100)
)



insert into ##group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'GENDER'),
(5, 'ELLStatus')


insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'EthnicityGroupCC_sort'),
(6, 'LanguageOfInstructionCC2', 'Language_Sort'),
(7, 'GradeLevel', 'GradeLevel_Sort'),
(8, 'STHFlag', 'STHFlagSort'),
(9, 'FosterCareFlag', 'FosterCareFlagSort')



Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
select @rowCount = count(*) from ##group_and_sort_fields
declare @outputSQL nvarchar(max)
while @i <= @rowCount 
begin
	select @groupBy = '', @sortBy = '', @outputSQL = ''
	select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
	from ##group_and_sort_fields where outputOrderID = @i 

	select @outputSQL =
case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 from ( ' else ' ' end +
' select * from '+
' ( '+
' Select   ' + case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end  
+ case when @sortBy = '' then  @groupBy +' as sort ' 
	when  @i = 8 then ' case when '+@groupBy + ' = ' +'''Y'''+' then '+'''Yes'''+' else '+'''No'''+'  end as STHFlag'
	else  @groupBy  end   
+'	,FORMAT(sum(STUDENTS_WITH_REF), ''#,##0'') as c1 '+
'    ,FORMAT(sum(CLOSED_WITHOUT_IEP), ''#,##0'') as c2 '+
'	,FORMAT(sum(INELIGIBLE_LESS_60), ''#,##0'') as c3 '+
'    ,FORMAT(sum(INELIGIBLE_MORE_60), ''#,##0'') as c4 '+
'	,FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)), ''#,##0'') as c5 '+
'    ,FORMAT(sum(CLASSIFIED_LESS_60), ''#,##0'') as c6 '+
'    ,FORMAT(sum(CLASSIFIED_MORE_60), ''#,##0'') as c7 '+
'    ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60), ''#,##0'') as C8 '+
'	,FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)), ''#,##0'') as c9 '+
'	,FORMAT(sum(TOTAL_AWAITING), ''#,##0'') as c10		'+
'	,FORMAT(sum(TOTAL_OPEN), ''#,##0'') as c11 '+
' FROM ##Report_Final14 '+
case when @i =8 then ' where STHFlag in ('+'''Y'''+', '+'''N'''+') ' 
	 else ' ' end 
+' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow ' else '##TotalRow_Sort ' end +
case when @sortBy != '' then ') a order by sort ' else ' order by sort ' end
	
	PRINT(@outputSQL)
	execute (@outputSQL)
	select @i = @i + 1

end

END
GO


