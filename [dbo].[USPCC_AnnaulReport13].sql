USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport13]    Script Date: 11/12/2024 3:45:47 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [dbo].[USPCC_AnnaulReport13]
@tableNameCCRSMandateR13 varchar(100) = '',
@tableNameRptStudentRegister0615 varchar(100) = '' 
AS

/************************************************************************************************************************
Program				       : Report 13
Purpose				       : 1.To create a Related Services report citywide 
Project				       : City council
Author			           : Charlotte Wang
Programmer                 : Charlotte Wang
Modifications		       : Created the SQL script using existing Triannual City wide scripts
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi			06/25/2024		Replaced TempResFlag with STHFlag to identify students in temporary housing 

************************************************************************************************************************/

BEGIN

	declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCRSMandateR13, '') = ''
	begin
		set @tableNameCCRSMandateR13 = 'CC_RSMandateR13_0615' + @currYear_YY
	end 

	if isnull(@tableNameRptStudentRegister0615, '') = ''
	begin
		set @tableNameRptStudentRegister0615 = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end 

IF OBJECT_ID('tempdb..##CCTotaltemp13') IS NOT NULL
	DROP TABLE ##CCTotaltemp13;

	CREATE TABLE ##CCTotaltemp13(
	[StudentID] [int]  NULL,
	[EnrolledDBN] [varchar](9) NULL,
	[ReportingDistrict] [varchar](7) NULL,
	[STHFlag] [varchar](1) NULL,
	[STHFlagSort] [int]  NULL,
	[MandatesBilingual] [varchar](75) NULL,
	[FullEncounter] [int]  NULL,
	[PartialEncounter] [int]  NULL,
	[NoEncounter] [int]  NULL,
	[MealStatusGrouping] [varchar](50) NULL,
	[EthnicityGroupCC] [varchar](50) NULL,
	[Ethnicity_sort] [int] NULL,
	[GradeLevel] [varchar](25) NULL,
	[RecommendedLanguage] [nvarchar](255) NULL,
	[RecommendedLanguageSort] [int] NULL,
	[Gender] [varchar](50) NULL,
	[ELLStatus] [varchar](7) NULL,
	[GradeSort] [int] NULL,
	[FosterCareFlag] [varchar](1)  NULL,
	[FosterCareFlagSort] [int]  NULL
)

declare @cctotaltemp varchar(max) = ' Insert into ##CCTotaltemp13 '+
' Select a.StudentID '+
		' ,a.EnrolledDBN '+
	    ' ,a.ReportingDistrict '+
		' ,b.STHFlag '+
		' ,case when b.STHFlag='+'''Y'''+' then 1 else 2 '+
		' end as STHFlagSort '+
		 ' ,case when servicetype = '+'''Counseling Services'''+' and RSMandateLanguage <> '+'''English'''+' then '+'''Counseling Services Bilingual'''+
  ' when ServiceType = '+'''Speech-Language Therapy'''+' and RSMandateLanguage <> '+'''English'''+' then '+'''Speech-Language Therapy Bilingual'''+
  ' else ServiceType '+ 
  ' end as MandatesBilingual  '+
   ' ,case when EncounterStatus = '+'''Full Encounter'''+' then 1  '+
   ' else 0 '+
   ' end as '+'''FullEncounter'''+
   ' ,case when EncounterStatus = '+'''Partial Encounter'''+' then 1 '+
   ' else 0  '+
   ' end as '+'''PartialEncounter'''+
   ' ,case when EncounterStatus= '+'''No Encounter'''+' then 1  '+
   ' else 0  '+
   ' end as '+'''NoEncounter'''+
	   ' ,a.[MealStatusGrouping] '+
	   ' ,case when a.[EthnicityGroupCC] is null then '+'''Other'''+
	   ' else a.[EthnicityGroupCC] '+
	   ' end as [EthnicityGroupCC] '+ 
	   ' ,case when a.[EthnicityGroupCC]  = '+'''Asian'''+' then 1 '+
	   ' when a.[EthnicityGroupCC]  = '+'''Black'''+' then 2 '+
	   ' when a.[EthnicityGroupCC]  = '+'''Hispanic'''+' then 3 '+
	   ' when a.[EthnicityGroupCC] = '+'''White'''+' then 4 '+
	   ' when (a.[EthnicityGroupCC] is Null or a.[EthnicityGroupCC] = '+'''Other'''+') then 5 '+
	   ' end as Ethnicity_sort  '+
	   ' ,a.GradeLevel '+
	   ' ,a.RecommendedLanguage '+
	     ' ,case when (a.RecommendedLanguage = '+'''English'''+' OR a.RecommendedLanguage IS NULL) then 1 '+
	   ' when a.RecommendedLanguage = '+'''SPANISH'''+' then 2 '+
	   ' when a.RecommendedLanguage = '+'''CHINESE'''+' then 3 '+
	   ' when a.RecommendedLanguage = '+'''OTHER'''+' then 4 '+
	   '  end as RecommendedLanguageSort '+
	   ' ,a.Gender '+
	   ' ,a.[ELLStatus] '+
	 -- ,a.[EnrolledDBN]
	  ' ,case when a.GradeLevel = '+'''0K'''+' then 1  '+
	   ' when a.GradeLevel = '+'''01'''+' then 2 '+
	   ' when a.GradeLevel = '+'''02'''+' then 3 '+
	   ' when a.GradeLevel = '+'''03'''+' then 4 '+
	   ' when a.GradeLevel = '+'''04'''+' then 5 '+
	   ' when a.GradeLevel = '+'''05'''+' then 6 '+
	   ' when a.GradeLevel = '+'''06'''+' then 7 '+
	   ' when a.GradeLevel = '+'''07'''+' then 8 '+
	   ' when a.GradeLevel = '+'''08'''+' then 9 '+
	   ' when a.GradeLevel = '+'''09'''+' then 10 '+
	   ' when a.GradeLevel = '+'''10'''+' then 11 '+
	   ' when a.GradeLevel = '+'''11'''+' then 12 '+
	   ' when a.GradeLevel = '+'''12'''+' then 13 '+
	   ' end as GradeSort '+
	   ' ,  case when a.FosterCareFlag = ''Y'' then '+'''Y'''+' else '+'''N'''+
		' end as FosterCareFlag '+
		' ,  case when a.FosterCareFlag = ''Y'' then 1 else 2 '+
		' end as FosterCareFlagSort '+
	  ' FROM [SEO_MART].[snap].'+@tableNameCCRSMandateR13+' a '+
	  ' left join [SEO_MART].[snap].' + @tableNameRptStudentRegister0615 + ' b on a.studentid=b.studentid '

	  print (@cctotaltemp)
	  execute (@cctotaltemp)

	  ----- Citywide  Special Education Programs

declare @cs_outputsql varchar(max)= 
' select * from '+
' ( '+
' select distinct  MandatesBilingual '+
   ' ,  FORMAT(Sum(FullEncounter) , ''#,##0'') as c1 '+
  ' ,concat(cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c2 '+
  ' ,FORMAT(sum(PartialEncounter) , ''#,##0'') as c3 '+
  ' ,concat(cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c4 '+
  ' ,FORMAT(sum(NoEncounter) , ''#,##0'') as c5 '+
  ' ,concat(cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c6 '+
  ' from ##CCTotaltemp13 a '+
   ' group by MandatesBilingual   '+
   --order by PrimaryProgramType 
   ' ) cityide '+
' union all '+
' select * from ( '+
 ' select distinct ''Total'' MandatesBilingual '+
   ' ,  FORMAT(Sum(FullEncounter) , ''#,##0'') as c1 '+
  ' ,concat(cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c2 '+
  ' ,FORMAT(sum(PartialEncounter) , ''#,##0'') as c3 '+
  ' ,concat(cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c4 '+
  ' ,FORMAT(sum(NoEncounter) , ''#,##0'') as c5 '+
  ' ,concat(cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c6 '+
  ' from ##CCTotaltemp13 a)  as total '

  print(@cs_outputsql)
  execute(@cs_outputsql)

  if object_id('Tempdb..##totalRow13') is not null
	drop table ##totalRow13
Select  
    'Total' as 'Header'
	,FORMAT(Sum(FullEncounter) , '#,##0') as c1 
	,CONCAT(cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	,FORMAT(sum(PartialEncounter) , '#,##0') as c3 
	,CONCAT(cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4 
	,FORMAT(sum(NoEncounter) , '#,##0') as c5 
	,CONCAT(cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c6   
into ##TotalRow13
FROM ##CCTotaltemp13

if object_id('Tempdb..##totalRow_Sort13') is not null
	drop table ##totalRow_Sort13 
Select  
    '99' as 'sort'
	,'Totals' as 'Header'
	,FORMAT(Sum(FullEncounter) , '#,##0') as c1 
	,CONCAT(cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	,FORMAT(sum(PartialEncounter) , '#,##0') as c3 
	,CONCAT(cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4 
	,FORMAT(sum(NoEncounter) , '#,##0') as c5 
	,CONCAT(cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c6   
into ##TotalRow_Sort13
FROM ##CCTotaltemp13


   /*Disaggregations by Demogrphics*/

if object_Id('tempdb..##group_and_sort_fields') is not null
	drop table ##group_and_sort_fields

create table ##group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))

insert into ##group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'Gender'),
(5, 'ELLStatus'),
(10, 'EnrolledDBN')

insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
(6, 'RecommendedLanguage', 'RecommendedLanguageSort'),
(7, 'GradeLevel', 'GradeSort'),
(8, 'STHFlag', 'STHFlagSort'),
(9, 'FostercareFlag', 'FosterCareFlagSort')

 
 Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
select @rowCount = count(*) from ##group_and_sort_fields
declare @new_outputSQL nvarchar(max)
while @i <= @rowCount 
begin
	select @groupBy = '', @sortBy = '', @new_outputSQL = ''
	select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
	from ##group_and_sort_fields where outputOrderID = @i 

	select @new_outputSQL =  
	case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4,c5,c6 from ( ' else ' ' end +
' select * from '+
' ( '+
 'Select '+  
  case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end +
  case when @sortBy = ''
		then  @groupBy +' as sort '
		else  @groupBy  end  + 
  ',FORMAT(Sum(FullEncounter) , ''#,##0'') as c1 '+
  ',CONCAT(cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c2 '+
  ',FORMAT(sum(PartialEncounter) , ''#,##0'') as c3 '+
  ',CONCAT(cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c4 '+
  ',FORMAT(sum(NoEncounter) , ''#,##0'') as c5 '+
  ',CONCAT(cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'')  as c6 '+
 ' FROM ##CCTotaltemp13 '+
 ' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
 ' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow13 ' else '##TotalRow_Sort13 ' end +
case when @sortBy != '' then ' ) a order by sort ' 
      else ' order by sort ' end

 print(@new_outputSQL)
 execute(@new_outputSQL)

	select @i = @i + 1
end


end
GO


