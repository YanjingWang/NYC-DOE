USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport13st]    Script Date: 11/12/2024 3:48:41 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[USPCC_AnnaulReport13st] 
@tableNameCCSpecialTransportation varchar(100) = '',
@tableNameStudentRegisterR814 varchar(100)
AS
/************************************************************************************************************************
Program				       : Report 13 Special Transportation
Purpose				       : 1.To Special Transportation report by disaggregations
Project				       : City council
Author			           : Charlotte Wang
Programmer                 : Charlotte Wang
Modifications		       : Created the SQL script using existing BIP Citywide scripts
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi			06/25/2024		Replaced TempResFlag with STHFlag to identify students in temporary housing 
Charlotte Wang           09/06/2024      Line 114,118 [Transportation Assigned] =Curb-to-school for Sy23 and changed to curb to school for SY24 and the store proc is hardcoded to Curb-to-school So data is not pulled from  Excel to table due to value change so added a like operator  Like '+'''Curb%to%School'''
************************************************************************************************************************/

BEGIN 
	declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCSpecialTransportation, '') = ''
	begin
		set @tableNameCCSpecialTransportation = 'CC_SpecialTransportation_0615' + @currYear_YY
	end 

	if isnull(@tableNameStudentRegisterR814, '') = ''
	begin
		set @tableNameStudentRegisterR814 = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end


IF OBJECT_ID('tempdb..##CCTotaltemp13st') IS NOT NULL
	DROP TABLE ##CCTotaltemp13st;

	
CREATE TABLE ##CCTotaltemp13st(
	[StudentID] [int] NULL,
	[EnrolledDBN] [nvarchar](255) NULL,
	[ReportingDistrict] [int] NULL,
	[STHFlag] [varchar](1) NULL,
	[STHFlagSort] [int]  NULL,
	[MealStatusGrouping] [nvarchar](255) NULL,
	[EthnicityGroupCC] [nvarchar](255) NULL,
	[Ethnicity_sort] [int] NULL,
	[GradeLevel] [nvarchar](255) NULL,
	[OutcomeLanguageCC] [nvarchar](255) NULL,
	[OutcomeLanguageCCSort] [int] NULL,
	[Gender] [nvarchar](255) NULL,
	[ELLStatus] [nvarchar](255) NULL,
	[GradeSort] [int] NULL,
	[FosterCareFlag] [varchar](1)  NULL,
	[FosterCareFlagSort] [int]  NULL,
	[CurbtoSchool] [int]  NULL,
	[StoptoSchool] [int]  NULL,
	[Unassigned] [int]  NULL
)

declare @CCTotaltemp13st varchar(max) =' Insert into ##CCTotaltemp13st '+
	' Select a.StudentID '+
		' ,a.EnrolledDBN '+
	    ' ,a.ReportingDistrict '+
		' ,b.STHFlag '+
		' ,case when b.STHFlag='+'''Y'''+' then 1 else 2 '+
		' end as STHFlagSort '+
		 '   ,a.[MealStatusGrouping] '+
	   ' ,case when a.[EthnicityGroupCC] is null then '+'''Other'''+
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
	   ' when a.GradeLevel = '+'''1'''+' then 2 '+
	   ' when a.GradeLevel = '+'''2'''+' then 3 '+
	   ' when a.GradeLevel = '+'''3'''+' then 4 '+
	   ' when a.GradeLevel = '+'''4'''+' then 5 '+
	   ' when a.GradeLevel = '+'''5'''+' then 6 '+
	   ' when a.GradeLevel = '+'''6'''+' then 7 '+
	   ' when a.GradeLevel = '+'''7'''+' then 8 '+
	   ' when a.GradeLevel = '+'''8'''+' then 9 '+
	   ' when a.GradeLevel = '+'''9'''+' then 10 '+
	   ' when a.GradeLevel = '+'''10'''+' then 11 '+
	   ' when a.GradeLevel = '+'''11'''+' then 12 '+
	   ' when a.GradeLevel = '+'''12'''+' then 13 '+
	   ' end as GradeSort '+
	   ' ,  case when a.FosterCareFlag = ''Y'' then '+'''Y'''+' else '+'''N'''+
		' end as FosterCareFlag '+
		' ,  case when a.FosterCareFlag = ''Y'' then 1 else 2 '+
		' end as FosterCareFlagSort '+
		' ,case when [Transportation Assigned] Like '+'''Curb%to%School'''
		+' then 1  '+
   ' else 0 '+
   ' end as '+'''CurbtoSchool'''+
   ' ,case when [Transportation Assigned] Like '+'''Stop%to%School'''+' then 1 '+
   ' else 0  '+
   ' end as '+'''StoptoSchool'''+
   ' ,case when [Transportation Assigned] = '+'''Unassigned'''+' then 1  '+
   ' else 0  '+
   ' end as '+'''Unassigned'''+
  	   --  into ##CCTotaltemp13st 
       ' FROM [SEO_MART].[snap].'+@tableNameCCSpecialTransportation+' a '+
	      ' left join SEO_Mart.snap.'+@tableNameStudentRegisterR814+' b on a.studentid=b.studentid '

	   print(@CCTotaltemp13st)
	   execute(@CCTotaltemp13st)

--select distinct GradeSort from #CCTotaltemp13st


--Checking the total
declare @total varchar(max) = 
  ' select distinct ''Total'' as  col, '+
  ' FORMAT(Sum(CurbtoSchool) , ''#,##0'') as c1 '+
  ' ,concat(cast(Sum(CurbtoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
  ' ,FORMAT(sum(StoptoSchool) , ''#,##0'') as c3 '+
  ' ,concat(Cast(Sum(StoptoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ' ,FORMAT(sum(Unassigned) , ''#,##0'') as c5 '+
  ' ,concat(cast(Sum(Unassigned)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c6 '+
  ' from ##CCTotaltemp13st  '

  print (@total)
  execute (@total)


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


 if object_id('tempdb..##totalRow13st') is not null
	 drop table ##totalRow13st 
	 	    
	  select 
	  'Total' as 'Header'
	  ,FORMAT(Sum(CurbtoSchool) , '#,##0') as c1 
	  ,concat(cast(Sum(CurbtoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	,FORMAT(sum(StoptoSchool) , '#,##0') as c3 
	,concat(cast(Sum(StoptoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4 
	,FORMAT(sum(Unassigned) , '#,##0') as c5 
	,concat(cast(Sum(Unassigned)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c6  
	  into ##totalRow13st
	  from ##CCTotaltemp13st
	 
	if object_id('tempdb..##totalRow_Sort13st') is not null
	drop table ##totalRow_Sort13st 
	 	    
	  select 
	  '99' as 'Sort',
	  'Total' as 'Header'
	  ,FORMAT(Sum(CurbtoSchool) , '#,##0') as c1 
	  ,concat(cast(Sum(CurbtoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c2 
	,FORMAT(sum(StoptoSchool) , '#,##0') as c3 
	,concat(cast(Sum(StoptoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c4 
	,FORMAT(sum(Unassigned) , '#,##0') as c5 
	,concat(cast(Sum(Unassigned)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), '%') as c6 
	into ##totalRow_Sort13st
	  from ##CCTotaltemp13st


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
  case  when @sortBy = ''
		then  @groupBy +' as sort '
		else  @groupBy  end  + 
  ',FORMAT(Sum(CurbtoSchool) , ''#,##0'') as c1 '+
  ',concat(cast(Sum(CurbtoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
  ',FORMAT(sum(StoptoSchool) , ''#,##0'') as c3 '+
  ',concat(cast(Sum(StoptoSchool)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ',FORMAT(sum(Unassigned) , ''#,##0'') as c5 '+
  ',concat(cast(Sum(Unassigned)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c6 '+
 ' FROM ##CCTotaltemp13st '+
 ' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
 ' ) a '+ 
' union all '+
 case when @sortBy = '' and @i = 1 then 'select 99 as  total, c1,c2,c3,c4,c5,c6 from ##totalRow13st'
	  when @sortBy = '' then 'select * from ##totalRow13st ' else ' select * from ##totalRow_Sort13st ' end +
case when @sortBy != '' then ' ) a order by sort ' 
      else ' order by sort ' end


 print(@new_outputSQL)
 execute(@new_outputSQL)

	select @i = @i + 1
END
	
END
GO


