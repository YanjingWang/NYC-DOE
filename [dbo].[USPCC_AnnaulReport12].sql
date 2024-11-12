USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport12]    Script Date: 11/12/2024 3:39:57 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [dbo].[USPCC_AnnaulReport12] 
@tableNameCCPSStudentR12 varchar(100) = ''

As
/************************************************************************************************************************
Program				       : Report 12
Purpose				       : 1.To create a Special Programs report citywide 
Project				       : City council
Programmer			       : Charlotte Wang
Modifications		       : Created the SQL script
Created by				   : Charlotte Wang
Comments				   : Created store proc using existing SAS Script 
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi			06/25/2024		Replaced TempResFlag with STHFlag to identify students in temporary housing 

************************************************************************************************************************/

BEGIN

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCPSStudentR12, '') = ''
	begin
		set @tableNameCCPSStudentR12 = 'CC_PSStudentR12_0615' + @currYear_YY
	end 


	IF OBJECT_ID('tempdb..##CCTotaltemp12') IS NOT NULL
	DROP TABLE ##CCTotaltemp12;

CREATE TABLE ##CCTotaltemp12(
	[StudentID] [int]  NULL,
	[EnrolledDBN] [varchar](10) NULL,
	[ReportingDistrict] [varchar](7) NULL,
	[STHFlag] [varchar](1) NULL,
	[STHFlagSort] [int]  NULL,
	[PrimaryProgramType] [varchar](40) NULL,
	[FullyReceiving] [int]  NULL,
	[PartiallyReceiving] [int]  NULL,
	[NotReceiving] [int]  NULL,
	[MealStatusGrouping] [varchar](50) NULL,
	[EthnicityGroupCC] [varchar](50) NULL,
	[Ethnicity_sort] [int] NULL,
	[GradeLevel] [varchar](25) NULL,
	[PSOutcomeLanguage] [varchar](50) NULL,
	[PSOutcomeLanguageSort] [int] NULL,
	[Gender] [varchar](50) NULL,
	[ELLStatus] [varchar](7) NULL,
	[Classification] [varchar](50) NULL,
	[Grade_Sort] [int] NULL,
	[FosterCareFlag] [varchar](1)  NULL,
	[FosterCareFlagSort] [int]  NULL
) 

DECLARE @CCTotaltemp VARCHAR(MAX) =' Insert into ##CCTotaltemp12 '+
' Select a.StudentID '+
    ' ,EnrolledDBN '+
	  '   ,ReportingDistrict '+
		' ,STHFlag '+
		' ,case when STHFlag='+'''Y'''+' then 1 else 2 '+
		' end as STHFlagSort '+
		 ' ,a.PrimaryProgramType '+ 
   ' ,case when compliancecategoryCC = 100 then 1  '+
   ' else 0 '+
   ' end as '+'''FullyReceiving'''+
   ' ,case when compliancecategoryCC = 50 then 1 '+
   ' else 0  '+
   ' end as '+'''PartiallyReceiving'''+
   ' ,case when compliancecategorycc = 0 then 1  '+
   ' else 0  '+
   ' end as '+'''NotReceiving'''+
	   ' ,[MealStatusGrouping] '+
	   ' ,case when [EthnicityGroupCC] is null then '+'''Other'''+
	   ' else [EthnicityGroupCC] '+
	   ' end as [EthnicityGroupCC]  '+
	   ' ,case when [EthnicityGroupCC]  = '+'''Asian'''+' then 1 '+
	   ' when [EthnicityGroupCC]  = '+'''Black'''+' then 2 '+
	   ' when [EthnicityGroupCC]  = '+'''Hispanic'''+' then 3 '+
	   ' when [EthnicityGroupCC] = '+'''White'''+' then 4 '+
	   ' when ([EthnicityGroupCC] is Null or [EthnicityGroupCC] = '+'''Other'''+') then 5 '+
	   ' end as Ethnicity_sort  '+
	   ' ,a.GradeLevel '+
	   ' ,PSOutcomeLanguage '+
	    ' ,case when (PSOutcomeLanguage = '+'''English'''+' OR PSOutcomeLanguage IS NULL) then 1 '+
	   ' when PSOutcomeLanguage = '+'''SPANISH'''+' then 2 '+
	   ' when PSOutcomeLanguage = '+'''CHINESE'''+' then 3 '+
	   ' when PSOutcomeLanguage = '+'''OTHER'''+' then 4 '+
	    ' end as PSOutcomeLanguageSort '+
	   ' ,a.Gender '+
	   ' ,[ELLStatus] '+
	   ' ,[Classification] '+
	   ' ,case when a.GradeLevel = '+'''0K'''+' then 1 '+
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
	   ' end as '+'''Grade_Sort'''+
	   ' ,  case when FosterCareFlag = ''Y'' then '+'''Y'''+' else '+'''N'''+
		' end as FosterCareFlag '+
		' ,  case when FosterCareFlag = ''Y'' then 1 else 2 '+
		' end as FosterCareFlagSort '+
	   -- into ##CCTotaltemp
      ' FROM [SEO_MART].[snap].'+@tableNameCCPSStudentR12+' a '+
	  	'   where  a.AdminDistrict <>79'

		print(@CCTotaltemp)
		execute(@CCTotaltemp)

----- Citywide  Special Education Programs
declare @CS_outputSQL varchar(max) = ' select * from '+
' ( '+
 ' select distinct  '+
 ' PrimaryProgramType  '+
  ' ,FORMAT(Sum(FullyReceiving) , ''#,##0'') as c1  '+
  ' ,CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2  '+
  ' ,FORMAT(sum(PartiallyReceiving) , ''#,##0'') as c3  '+
  ' ,CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ' ,FORMAT(sum(NotReceiving) , ''#,##0'') as c5 '+
  ' ,CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c6 '+
  ' from ##CCTotaltemp12 a  '+
  ' group by PrimaryProgramType   '+
   --order by PrimaryProgramType 
  '  ) cityide  '+
' union all '+
' select * from ( '+
 ' select distinct ''Total'' PrimaryProgramType '+
' ,FORMAT(Sum(FullyReceiving) , ''#,##0'') as c1 '+
  ',CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
 '  ,FORMAT(sum(PartiallyReceiving) , ''#,##0'') as c3 '+
  ' ,CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ' ,FORMAT(sum(NotReceiving) , ''#,##0'') as c5 '+
  ' ,CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c6 '+
  ' from ##CCTotaltemp12 a)  as total '


	print (@CS_outputSQL);
	execute (@CS_outputSQL)


   /*Disaggregations by Demogrphics*/

if object_Id('tempdb..##group_and_sort_fields') is not null
	drop table ##group_and_sort_fields

create table ##group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))

insert into ##group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'Gender'),
(7, 'ELLStatus')

insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
(5, 'GradeLevel', 'Grade_Sort'),
(6, 'PSOutcomeLanguage', 'PSOutcomeLanguageSort'),
(8, 'STHFlag', 'STHFlagSort'),
(9, 'FostercareFlag', 'FosterCareFlagSort')

 
 if object_id('tempdb..##totalRow12') is not null
	 drop table ##totalRow12 
	 	    
	  select 
	  'Total' as 'Header'
	  ,FORMAT(Sum(FullyReceiving), '#,##0') as c1 
	  ,CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	  ,FORMAT(sum(PartiallyReceiving) , '#,##0') as c3 
	  ,CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4 
	  ,FORMAT(sum(NotReceiving) , '#,##0') as c5 
	  ,CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c6 
	  into ##totalRow12
	  from ##CCTotaltemp12
	 
	if object_id('tempdb..##totalRow_Sort12') is not null
	drop table ##totalRow_Sort12 
	 	    
	  select 
	  '99' as 'Sort',
	  'Total' as 'Header'
	  ,FORMAT(Sum(FullyReceiving), '#,##0') as c1 
	  ,CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	  ,FORMAT(sum(PartiallyReceiving) , '#,##0') as c3 
	  ,CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4 
	  ,FORMAT(sum(NotReceiving) , '#,##0') as c5 
	  ,CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c6 
	  into ##totalRow_Sort12
	  from ##CCTotaltemp12



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
 ',FORMAT(Sum(FullyReceiving), ''#,##0'') as c1 '+
 ',CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
 ',FORMAT(sum(PartiallyReceiving) , ''#,##0'') as c3 '+
 ',CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
 ',FORMAT(sum(NotReceiving) , ''#,##0'') as c5 '+
 ',CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c6 '+
 ' FROM ##CCTotaltemp12 '+
 ' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
 ' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow12 ' else '##TotalRow_Sort12 ' end +
case when @sortBy != '' then ' ) a order by sort ' 
      else ' order by sort ' end



 -- case when @sortBy != '' then ' order by sort ' else ' order by sort ' end


 print(@new_outputSQL)
 execute(@new_outputSQL)

	select @i = @i + 1
end

END;
GO


