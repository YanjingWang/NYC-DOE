USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport14a]    Script Date: 11/12/2024 3:50:47 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [dbo].[USPCC_AnnaulReport14a] 
@tableNameCCStudentRegisterR814 varchar(100) = ''
AS
/************************************************************************************************************************
Program				       : Report 14a
Purpose				       : 1.To Create BIP(Behaioral Intervention Plan) report Citywide
Project				       : City council
Programmer			       : Charlotte Wang
Modifications		       : Created the SQL script using existing BIP Citywide scripts
Author			           : Charlotte Wang
Developer                  : Charlotte Wang             
Created		               : 11/9/2023  Created Stored Procedure using Existing SAS Scripts
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi			06/25/2024		Replaced TempResFlag with STHFlag to identify students in temporary housing 

************************************************************************************************************************/
BEGIN 
	declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCStudentRegisterR814, '') = ''
	begin
		set @tableNameCCStudentRegisterR814 = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end 

IF OBJECT_ID('tempdb..##CCTotaltemp14a') IS NOT NULL
	DROP TABLE ##CCTotaltemp14a;

	CREATE TABLE ##CCTotaltemp14a(
	[StudentID] [int]  NULL,
	[EnrolledDBN] [varchar](10) NULL,
	[ReportingDistrict] [varchar](7) NULL,
	[STHFlag] [varchar](1) NULL,
	[STHFlagSort] [int]  NULL,
	[BIP] [int]  NULL,
	[NoBIP] [int]  NULL,
	[PrimaryProgramType] [varchar](45) NULL,
	[MealStatusGrouping] [varchar](50) NULL,
	[EthnicityGroupCC] [varchar](50) NULL,
	[Ethnicity_sort] [int] NULL,
	[GradeLevel] [varchar](25) NULL,
	[OutcomeLanguageCC] [varchar](50) NULL,
	[OutcomeLanguageCCSort] [int] NULL,
	[Gender] [varchar](50) NULL,
	[ELLStatus] [varchar](7) NULL,
	[GradeSort] [int] NULL,
	[FosterCareFlag] [varchar](1)  NULL,
	[FosterCareFlagSort] [int]  NULL
)

declare @CCTotaltemp14a varchar(max)= ' insert into ##CCTotaltemp14a '+
		' Select a.StudentID '+
		' ,a.EnrolledDBN '+
	    ' ,a.ReportingDistrict '+
		' ,a.STHFlag '+
		' ,case when a.STHFlag='+'''Y'''+' then 1 else 2 '+
		' end as STHFlagSort '+
	 ' ,case when BIPFlagCC = '+'''Y'''+' then 1  '+
   ' else 0 '+
   ' end as '+'''BIP'''+ 
   ' ,case when BIPFlagCC= '+'''N'''+' then 1  '+
   ' else 0  '+
   ' end as '+'''NoBIP'''+
   ' ,Case when PrimaryProgramType = '+'''No Active Program Services'''+' then '+'''Related Services or Assistive Technology Only'''+
' else PrimaryProgramType end as PrimaryProgramType '+
	'    ,a.[MealStatusGrouping] '+
	  '  ,case when a.[EthnicityGroupCC] is null then '+'''Other'''+
	   ' else a.[EthnicityGroupCC] '+
	   ' end as [EthnicityGroupCC]  '+
	   ' ,case when a.[EthnicityGroupCC]  = '+'''Asian'''+' then 1 '+
	   ' when a.[EthnicityGroupCC]  = '+'''Black'''+' then 2 '+
	   ' when a.[EthnicityGroupCC]  = '+'''Hispanic'''+' then 3 '+
	   ' when a.[EthnicityGroupCC] = '+'''White'''+' then 4 '+
	   ' when (a.[EthnicityGroupCC] is Null or a.[EthnicityGroupCC] = '+'''Other'''+') then 5 '+
	   ' end as Ethnicity_sort  '+
	   ' ,a.GradeLevel '+
	   ' ,a.OutcomeLanguageCC '+
	     ' ,case when (a.OutcomeLanguageCC = '+'''English'''+' OR a.OutcomeLanguageCC IS NULL) then 1 '+
	   ' when a.OutcomeLanguageCC = '+'''SPANISH'''+' then 2 '+
	   ' when a.OutcomeLanguageCC = '+'''CHINESE'''+' then 3 '+
	   ' when a.OutcomeLanguageCC = '+'''OTHER'''+' then 4 '+
	    ' end as OutcomeLanguageCCSort '+
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
	   --- into #CCTotaltemp14a
      ' FROM [SEO_MART].[snap].'+@tableNameCCStudentRegisterR814+' a '

		print(@CCTotaltemp14a)
		execute(@CCTotaltemp14a)

----- Citywide
	declare @c_outputsql varchar(max) =
' select * from '+
' ( '+
 ' select distinct  PrimaryProgramType '+
  ' ,FORMAT(Sum(BIP) , ''#,##0'') as c1 '+
  ' ,concat(cast(Sum(BIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
  ' ,FORMAT(sum(NoBIP) , ''#,##0'') as c3 '+
  ' ,concat(cast(Sum(NoBIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ' from ##CCTotaltemp14a a '+
   ' group by PrimaryProgramType   '+
   --order by PrimaryProgramType 
   ' ) cityide '+
	' union all '+
' select * from ( '+
 ' select distinct ''Total'' as  PrimaryProgramType '+
  ' ,FORMAT(Sum(BIP) , ''#,##0'') as c1 '+
  ' ,concat(cast(Sum(BIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
  ' ,FORMAT(sum(NoBIP) , ''#,##0'') as c3 '+
  ' ,concat(cast(Sum(NoBIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ' from ##CCTotaltemp14a a)  as total '

  print(@c_outputsql)
  execute(@c_outputsql)

  
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
(6, 'OutcomeLanguageCC', 'OutcomeLanguageCCSort'),
(7, 'GradeLevel', 'GradeSort'),
(8, 'STHFlag', 'STHFlagSort'),
(9, 'FostercareFlag', 'FosterCareFlagSort')


 if object_id('tempdb..##totalRow14a') is not null
	 drop table ##totalRow14a 
	 	    
	  select 
	  'Total' as 'Header'
	  ,FORMAT(Sum(BIP) , '#,##0') as c1 
	,concat(cast(Sum(BIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	,FORMAT(sum(NoBIP) , '#,##0') as c3 
	,concat(cast(Sum(NoBIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4	  
	into ##totalRow14a
	  from ##CCTotaltemp14a
	 
	if object_id('tempdb..##totalRow_Sort14a') is not null
	drop table ##totalRow_Sort14a 
	 	    
	  select 
	  '99' as 'Sort',
	  'Total' as 'Header'
	  ,FORMAT(Sum(BIP) , '#,##0') as c1 
	,concat(cast(Sum(BIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	,FORMAT(sum(NoBIP) , '#,##0') as c3 
	,concat(cast(Sum(NoBIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4
	  into ##totalRow_Sort14a
	  from ##CCTotaltemp14a
 
 Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
select @rowCount = count(*) from ##group_and_sort_fields
declare @new_outputSQL nvarchar(max)
while @i <= @rowCount 
begin
	select @groupBy = '', @sortBy = '', @new_outputSQL = ''
	select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
	from ##group_and_sort_fields where outputOrderID = @i 

	select @new_outputSQL = 
	case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4 from ( ' else ' ' end +
' select * from '+
' ( '+
 'Select '+  
  case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end +
  case when @sortBy = ''
		then  @groupBy +' as sort '
		else  @groupBy  end  + 
   ',FORMAT(Sum(BIP) , ''#,##0'') as c1 '+
  ',concat(cast(Sum(BIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
  ',FORMAT(sum(NoBIP) , ''#,##0'') as c3 '+
  ',concat(cast(Sum(NoBIP)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
 ' FROM ##CCTotaltemp14a '+
 ' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
 ' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow14a ' else '##TotalRow_Sort14a ' end +
case when @sortBy != '' then ' ) a order by sort ' 
      else ' order by sort ' end

 print(@new_outputSQL)
 execute(@new_outputSQL)

	select @i = @i + 1
end

end;
GO


