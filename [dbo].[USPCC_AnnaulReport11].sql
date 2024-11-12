USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport11]    Script Date: 11/12/2024 3:37:17 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[USPCC_AnnaulReport11]
@tableNameCCThreeYearReevalsR11 varchar(100) = ''
--@tableNameINTStudentDemographics_0630 varchar(100) = ''

AS
/************************************************************************************************************************
Program				       : AnnualReport11.sas
Purpose				       : 1.To create an Initial City council tri-annuals report and generate redacted output.(Note: Run till Part:1 , commenting test_arrays to get unredacted outputs)
					         2.Generate an RTF document using Proc report
					         3.To load data(redacted/unredacted) into the Excel report
Project				       : City council
Programmer			       : Charlotte Wang
Creation /Finalized Date   : Finalized on 11/01/2023
Comments			       : 
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

--11/02/2023: Prasanth worked on this SQL script fo City Council 10 Report using SAS Script

Raji Munnangi			06/25/2024		Replaced TempResFlag with STHFlag to identify students in temporary housing 
Charlotte Wang           10/08/2024      Made changes in the order of the columns HousingType and STHFlag in Temptable for the story MIS-12124
************************************************************************************************************************/

BEGIN

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCThreeYearReevalsR11, '') = ''
	begin
		set @tableNameCCThreeYearReevalsR11 = 'CC_ThreeYearReevalsR11_SY' + @currYear_YY
	end 

	/*if isnull(@tableNameINTStudentDemographics_0630, '') = ''
	begin
		set @tableNameINTStudentDemographics_0630 = 'INT_StudentDemographics_0630' + @currYear_YY
	end
	*/


if object_id('tempdb..##Report_3YRRev') is not null
	drop table ##Report_3YRRev

CREATE TABLE ##Report_3YRRev(
	[StudentID] [int] NOT NULL,
	[ProfileIDT] [int] NULL,
	[FirstName] [varchar](50) NULL,
	[LastName] [varchar](50) NULL,
	[SchoolType] [varchar](10) NULL,
	[AdminDistrict] [varchar](2) NULL,
	[ReferralDocumentIDT] [int] NULL,
	[ReferralTypeCode] [int] NULL,
	[ReferralTypeCC] [varchar](3) NULL,
	[OutcomeDocumentIDT] [int] NULL,
	[OutcomeTypeCode] [int] NULL,
	[OutcomeTypeDesc] [varchar](50) NULL,
	[ReferralDate] [date] NULL,
	[OutcomeDate] [date] NULL,
	[TRIOutcomeDate] [date] NULL,
	[PriorOutcomeDate] [date] NULL,
	[CompareDate] [date] NULL,
	[ComplianceStatus] [varchar](25) NULL,
	[IsRevision] [bit] NULL,
	[IsAmendIEP] [bit] NULL,
	[IsReconveneIEP] [bit] NULL,
	[IsLatestReferral] [bit] NULL,
	[ReferralSchoolYear] [varchar](9) NULL,
	[OutcomeSchoolYear] [varchar](9) NULL,
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
	[ReferralProcessType] [int] NULL,
	[ReferralProcessTypeDesc] [varchar](50) NULL,
	[ReferralProcessStage] [int] NULL,
	[ReferralProcessStageDesc] [varchar](50) NULL,
	[OutcomeProcessStage] [int] NULL,
	[OutcomeProcessStageDesc] [varchar](50) NULL,
	[OutcomeProcessType] [int] NULL,
	[OutcomeProcessTypeDesc] [varchar](50) NULL,
	[ReferralSchoolDBN] [varchar](10) NULL,
	[ReferralSchoolType] [varchar](7) NULL,
	[OutcomeSchoolDBN] [varchar](10) NULL,
	[OutcomeSchoolType] [varchar](7) NULL,
	[ReferralSource] [int] NULL,
	[ReferralSourceDesc] [varchar](150) NULL,
	[ReasonForDelay] [int] NULL,
	[ReasonForDelayDesc] [varchar](169) NULL,
	[OutcomeReason] [int] NULL,
	[OutcomeReasonDesc] [varchar](255) NULL,
	[DisabilityCode] [int] NULL,
	[ClassificationDesc] [varchar](50) NULL,
	[ReferralCreatedDate] [datetime] NULL,
	[ReferralFinalizedDate] [datetime] NULL,
	[OutcomeCreatedDate] [datetime] NULL,
	[OutcomeFinalizedDate] [datetime] NULL,
	[ProcessedDateTime] [datetime] NULL,
	[ProcessedDate] [date] NULL,
	[SchoolYear] [varchar](9) NULL,
	[TempResFlag] [varchar](1) NULL,
	HousingType varchar(50) NULL,
	STHFlag char(1) NULL,
   [FosterCareFlag] [varchar](1) NOT NULL
)

declare @sql varchar(max) = 'insert into ##Report_3YRRev '+
' select a.*  '+
'    from SEO_Mart.Snap.'+@tableNameCCThreeYearReevalsR11+' a '
--' left join SEO_Mart.Snap.'+@tableNameINTStudentDemographics_0630 +' c  '+
--' on a.studentid=c.studentid  '+
--' WHERE  a.GradeLevel NOT IN  ('+'''99'''+', '+'''00'''+') AND a.GradeLevel <> '+'''PK''' 

-- print(@sql)
execute(@sql)

update ##Report_3YRRev set GradeLevel = 'KG' where GradeLEvel = '0K'

if object_id('tempdb..##Report_Final11') is not null
	drop table ##Report_Final11
	
Select 
        ComplianceStatus        
	   ,MealStatusGrouping
	   ,EthnicityGroupCC
	     ,STHFlag
	   ,FosterCareFlag
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
	   end as LanguageOfInstruction_Sort
	   ,GENDER
	   ,case when ELLStatus is null then 'NOT ELL'
	   else ELLStatus
	   end as ELLStatus
	   ,ReportingDistrict
	   ,case when ComplianceStatus = 'Conducted on time' 
	   then 1
	   else 0
	   end as Conduct_on_time
	   ,case when ComplianceStatus = 'Not Conducted on time' 
	   then 1
	   else 0
	   end as Not_conducT_on_t
	   ,case when STHFlag = 'Y' then 1
	   when STHFlag  = 'N' then 2
	    end as STHFlagSort
	  	    ,case when FosterCareFlag = 'Y' then 1
	   when FosterCareFlag  = 'N' then 2
	    end as FosterCareFlagSort
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
	   into ##Report_Final11
  FROM ##Report_3YRRev
  WHERE ReportingDistrict not in('98','99', '00')  AND ComplianceStatus <> 'other'


  update  ##Report_Final11 set MealStatusGrouping = 'Full Price Meal' where MealStatusGrouping  = 'Unspecified'

   if object_id('tempdb..##TotalRow') is not null
	drop table ##TotalRow

	Select  
	'Total' as 'Header'
	  ,FORMAT(Count(ComplianceStatus), '#,##0') as c1 
      ,FORMAT(sum(Conduct_on_time), '#,##0') as c2
	  ,FORMAT(sum(Not_conducT_on_t), '#,##0') as c3 
	   into ##TotalRow
 FROM ##Report_Final11

 if object_id('tempdb..##TotalRow_Sort') is not null
	drop table ##TotalRow_Sort 

	Select  
	   '99' as 'sort'
	  ,'Total' as 'Header'
	  ,FORMAT(Count(ComplianceStatus), '#,##0') as c1 
      ,FORMAT(sum(Conduct_on_time), '#,##0') as c2
	  ,FORMAT(sum(Not_conducT_on_t), '#,##0') as c3 
	  into ##TotalRow_Sort
 FROM ##Report_Final11

 
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
(6, 'OutcomeLanguageCC', 'LanguageOfInstruction_Sort'),
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
	case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3 from ( ' else ' ' end +
' select * from '+
' ( '+
' Select   ' + case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end  
+ case when @sortBy = '' then  @groupBy +' as sort '
		when  @i = 8 then ' case when '+@groupBy + ' = ' +'''Y'''+' then '+'''Yes'''+' else '+'''No'''+'  end as STHFlag'
		else  @groupBy  end   
+' 	 ,FORMAT(Count(ComplianceStatus), ''#,##0'') as c1  '+
'       ,FORMAT(sum(Conduct_on_time), ''#,##0'') as c2 '+
'       ,FORMAT(sum(Not_conducT_on_t), ''#,##0'') as c3 '+ 
' FROM ##Report_Final11 '+
case when @i =8 then ' where STHFlag in ('+'''Y'''+', '+'''N'''+') ' 
	 else ' ' end 
+' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow ' else '##TotalRow_Sort ' end +
case when @sortBy != '' then ') a order by sort ' else ' order by sort ' end

	
	 -- print(@outputSQL)
	execute(@outputSQL)
	print(@outputSQL)
	select @i = @i + 1
end

end
GO


