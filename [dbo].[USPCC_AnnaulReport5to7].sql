USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport5to7]    Script Date: 11/12/2024 3:09:17 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[USPCC_AnnaulReport5to7] 
@tableNameCCReevalReferralsR510 varchar(100) = ''
--@tableNameINTStudentDemographics_0630 varchar(100) = ''

AS

/************************************************************************************************************************
Program				       : Reevals.sas
Purpose				       : 1.To create an  City council re-evaluation report and generate redacted output.(Note: Run till Part:1 , commenting test_arrays to get unredacted outputs)
					         2.Generate an RTF document using Proc report
					         3.To load data(redacted/unredacted) into the Excel report
Project				       : City council
Programmer			       : Charlotte Wang
Creation /Finalized Date   : Finalized on 11/01/2023
Comments			       : 
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART 

Raji Munnangi		06/25/2024		Modified to add STHFlag and HousingType; And then use STHFlag instead of TempResFlag in output
Charlotte Wang        10/08/2024      Made changes in the order of the columns HousingType and STHFlag in Temptable for the story MIS-12124
************************************************************************************************************************/
/**********   REMOVE COMMENT IN PART 1 FOR REDACTED REPORT *******************/
/*11/02/2023: Prasanth worked on this SQL script fo City Council 5-7 Reports using SAS Script*/

BEGIN 

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCReevalReferralsR510, '') = ''
	begin
		set @tableNameCCReevalReferralsR510 = 'CC_ReevalReferralsR510_SY' + @currYear_YY
	end

	/*if isnull(@tableNameINTStudentDemographics_0630, '') = ''
	begin
		set @tableNameINTStudentDemographics_0630 = 'INT_StudentDemographics_0630' + @currYear_YY
	end
	*/

if object_id('tempdb..##Report_Reev') is not null
	drop table ##Report_Reev

	CREATE TABLE ##Report_Reev(
	[StudentID] [int] NOT NULL,
	[ProfileIDT] [int] NULL,
	[FirstName] [varchar](50) NULL,
	[LastName] [varchar](50) NULL,
	[SchoolType] [varchar](10) NULL,
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
	[ReferralTypeCC] [varchar](12) NULL,
	[OutcomeDocumentIDT] [int] NULL,
	[OutcomeTypeCode] [int] NULL,
	[OutcomeTypeDesc] [varchar](50) NULL,
	[PlacementDocumentIDT] [int] NULL,
	[ReportOutcomeCC] [varchar](25) NULL,
	[ReportOutcome] [varchar](25) NULL,
	[InactiveDate] [date] NULL,
	[ReferralDate] [date] NULL,
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
	[PriorSpecialClass] [int] NULL,
	[CurrentSpecialClass] [int] NULL,
	[SpecialClassLREMRE] [varchar](5) NULL,
	[IsPWNDeferred] [bit] NULL,
	[ReferralSchoolYear] [varchar](9) NULL,
	[OutcomeSchoolYear] [varchar](9) NULL,
	[PriorOutcomeDocumentIDT] [int] NULL,
	[PriorOutcomeDate] [date] NULL,
	[PriorOutcomeTypeCode] [int] NULL,
	[PriorOutcomeTypeDesc] [varchar](50) NULL,
	[PriorRecommendPlacementDesc] [varchar](70) NULL,
	[ReasonForRecommendPlacement] [int] NULL,
	[RecommendPlacementDesc] [varchar](70) NULL,
	[PlacementRecommendChange] [varchar](5) NULL,
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
	[AssessmentCreatedDate] [datetime] NULL,
	[AssessmentFinalizedDate] [datetime] NULL,
	[OutcomeCreatedDate] [datetime] NULL,
	[OutcomeFinalizedDate] [datetime] NULL,
	[PlacementCreatedDate] [datetime] NULL,
	[PlacementFinalizedDate] [datetime] NULL,
	[ProcessedDateTime] [datetime] NULL,
	[ProcessedDate] [date] NULL,
	[TempResFlag] [varchar](1) NULL,
	HousingType	varchar(50),
	STHFlag	char(1),
   [FosterCareFlag] [varchar](1) NOT NULL
)

declare @sql varchar(max) = 'insert into ##Report_Reev '+
' select a.*  '+
' from SEO_MART.Snap.'+@tableNameCCReevalReferralsR510  + ' a '
--' left join SEO_Mart.Snap.'+@tableNameINTStudentDemographics_0630 +' c '+
--' on a.studentid=c.studentid  '+
--' WHERE  a.GradeLevel <> '+'''99'''+' AND a.GradeLevel <> '+'''PK'''

execute (@sql)

update ##Report_Reev set GradeLevel = 'KG' where GradeLEvel = '0K'

if object_id('tempdb..##Report_Final57') is not null
	drop table ##Report_Final57

 SELECT  StudentID
	   ,ReportingDistrict
	   ,ReportOutcomeCC
	   ,STHFlag
	   ,FosterCareFlag
	   ,1 as STUDENTS_WITH_REF
	   ,(case when ReportOutcomeCC = 'IEP' 
	   and IEPComplianceMetricCC = '> 60 Days'
	   then 1
	   else 0
	   end + 
	   case when ReportOutcomeCC = 'IEP' 
	   and IEPComplianceMetricCC = '<= 60 Days'
	   then 1
	   else 0
	   end)  as TOTAL_CLASSIFIED
	   ,case when ReportOutcomeCC = 'Caseclose' then 1
	   else 0 
	   end as CLOSED_WITHOUT_IEP
	   ,case when ReportOutcomeCC = 'Declass' 
	   and IEPComplianceMetricCC = '<= 60 Days'
	   then 1
	   else 0
	   end as Declass_LESS_60
	   , case when ReportOutcomeCC = 'Declass'
	   and IEPComplianceMetricCC = '> 60 Days'
	   then 1
	   else 0
	   end as Declass_MORE_60	  
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
	   ,case when ReportOutcomeCC = 'Open' then 1
	   else 0 
	   end as TOTAL_OPEN
	   ,MealStatusGrouping
	   ,EthnicityGroupCC
	   ,case when EthnicityGroupCC = 'Asian' then 1
	   when EthnicityGroupCC  = 'Black' then 2
	   when EthnicityGroupCC  = 'Hispanic' then 3
	   when EthnicityGroupCC = 'White' then 4
	   when EthnicityGroupCC = 'Other' then 5
	   end as EthnicityGroupCC_sort 
	   ,GradeLevel
	   ,OutcomeLanguageCC
	   ,case when OutcomeLanguageCC = 'ENGLISH' then 1
	   when OutcomeLanguageCC = 'SPANISH' then 2
	   when OutcomeLanguageCC = 'CHINESE' then 3
	   when OutcomeLanguageCC = 'OTHER' then 4
	   when OutcomeLanguageCC = 'NOT APPLICABLE' then 5
	   end as Language_Sort
	   ,GENDER
	     ,case when STHFlag = 'Y' then 1
	   when STHFlag  = 'N' then 2
	    end as STHFlagSort
	    ,case when FosterCareFlag = 'Y' then 1
	  when FosterCareFlag  = 'N' then 2
	    end as FosterCareFlagSort
	   ,case when ELLStatus is null then 'NOT ELL'
	   else ELLStatus
	   end as ELLStatus 
	   ,case when GradeLevel = 'KG' then 1 
	   when GradeLevel = '01' then 2
	   when GradeLevel = '02' then 3
	   when GradeLevel = '03' then 4
	   when GradeLevel = '04' then 5
	   when GradeLevel = '05' then 6
	   when GradeLevel = '06' then 7
	   when GradeLevel = '07' then 8
	   when GradeLevel = '08' then 9
	   when GradeLevel = '09' then 10
	   when GradeLevel = '10' then 11
	   when GradeLevel = '11' then 12
	   when GradeLevel = '12' then 13
	   end as GradeLevel_Sort
	   into ##Report_Final57
	   FROM ##Report_Reev WHERE ReportingDistrict not in('98','99', '00') 

    if object_id('Tempdb..##totalRow') is not null
	drop table ##totalRow

	Select  
	  'Total' as 'Header'
	  ,FORMAT(sum(STUDENTS_WITH_REF),'#,##0') as c1
      ,FORMAT(sum(CLOSED_WITHOUT_IEP),'#,##0') as c2
      ,FORMAT(sum(Declass_LESS_60),'#,##0') as c3
      ,FORMAT(sum(Declass_MORE_60),'#,##0') as c4
	  ,FORMAT(sum(COALESCE(Declass_LESS_60,0) + COALESCE(Declass_MORE_60,0)),'#,##0') as c5
      ,FORMAT(sum(CLASSIFIED_LESS_60),'#,##0') as c6
      ,FORMAT(sum(CLASSIFIED_MORE_60),'#,##0') as c7
      ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60),'#,##0') as  c8
	  ,FORMAT(sum(COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0) + COALESCE(Declass_LESS_60,0) + COALESCE(Declass_MORE_60,0)),'#,##0') as c9 
      ,FORMAT(sum(TOTAL_OPEN),'#,##0') as c10  
	   into ##TotalRow
 FROM ##Report_Final57


if object_id('Tempdb..##totalRow_Sort') is not null
	drop table ##totalRow_Sort 

	Select  
	   '99' as 'sort'
	  ,'Total' as 'Header'
	  ,FORMAT(sum(STUDENTS_WITH_REF),'#,##0') as c1
      ,FORMAT(sum(CLOSED_WITHOUT_IEP),'#,##0') as c2
      ,FORMAT(sum(Declass_LESS_60),'#,##0') as c3
      ,FORMAT(sum(Declass_MORE_60),'#,##0') as c4
	  ,FORMAT(sum(COALESCE(Declass_LESS_60,0) + COALESCE(Declass_MORE_60,0)),'#,##0') as c5
      ,FORMAT(sum(CLASSIFIED_LESS_60),'#,##0') as c6
      ,FORMAT(sum(CLASSIFIED_MORE_60),'#,##0') as c7
      ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60),'#,##0') as  c8
	  ,FORMAT(sum(COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0) + COALESCE(Declass_LESS_60,0) + COALESCE(Declass_MORE_60,0)),'#,##0') as c9 
      ,FORMAT(sum(TOTAL_OPEN),'#,##0') as c10   
	  into ##TotalRow_Sort
 FROM ##Report_Final57

 if object_Id('tempdb..##group_and_sort_fields') is not null
	drop table ##group_and_sort_fields
create table ##group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))

insert into ##group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'GENDER'),
(5, 'ELLStatus')

insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'EthnicityGroupCC_sort'),
(6, 'OutcomeLanguageCC', 'Language_Sort'),
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
	case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 from ( ' else ' ' end +
' select * from '+
' ('+
' Select   ' + case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end  
+ case when @sortBy = '' then  @groupBy +' as sort '
		when  @i = 8 then ' case when '+@groupBy + ' = ' +'''Y'''+' then '+'''Yes'''+' else '+'''No'''+'  end as STHFlag'
		else  @groupBy  end   
+' ,FORMAT(sum(STUDENTS_WITH_REF),''#,##0'') as c1 '+ 
     ',FORMAT(sum(CLOSED_WITHOUT_IEP),''#,##0'') as c2 '+
     ',FORMAT(sum(Declass_LESS_60),''#,##0'') as c3 '+
     ' ,FORMAT(sum(Declass_MORE_60),''#,##0'') as c4'+
	  ' ,FORMAT(sum(COALESCE(Declass_LESS_60,0) + COALESCE(Declass_MORE_60,0)),''#,##0'') as c5 '+
      ' ,FORMAT(sum(CLASSIFIED_LESS_60),''#,##0'') as c6'+
      '  ,FORMAT(sum(CLASSIFIED_MORE_60),''#,##0'') as c7'+
      ' ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60),''#,##0'') as  c8 '+
	  ' ,FORMAT(sum(COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0) + COALESCE(Declass_LESS_60,0) + COALESCE(Declass_MORE_60,0)),''#,##0'') as c9  '+
      ' ,FORMAT(sum(TOTAL_OPEN),''#,##0'') as c10    '+  
' FROM ##Report_Final57 '+
case when @i =8 then ' where STHFlag in ('+'''Y'''+', '+'''N'''+') ' 
	 else ' ' end 
+' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow ' else '##TotalRow_Sort ' end +
case when @sortBy != '' then ') a order by sort ' else ' order by sort ' end

	execute(@outputSQL)
	PRINT(@outputSQL)
	select @i = @i + 1

end 


end
GO

