USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport8a]    Script Date: 11/12/2024 3:16:18 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[USPCC_AnnaulReport8a]
@tableNameCCStudentRegisterR814 varchar(100) = ''
	
as
/************************************************************************************************************************
Program				       : Report 8a
Purpose				       : 1.To Create BIP(Behaioral Intervention Plan) report Citywide
Project				       : City council
Programmer			       : Charlotte Wang
Modifications		       : Created the SQL script using existing BIP Citywide scripts
Author			ModifiedDate		Comments
Charlotte Wang    11/9/2023           Created Stored Procedure using Existing SAS Scripts

Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi		06/25/2024		Replaced TempResFlag with STHFlag

************************************************************************************************************************/
begin  
                            
	declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCStudentRegisterR814, '') = ''
	begin
		set @tableNameCCStudentRegisterR814 = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end 

if object_Id('tempdb..##CCTotaltemp') is not null
	drop table ##CCTotaltemp

create table  ##CCTotaltemp
(
ReportingDistrict	Varchar(7),
STHFlag	varchar(1),	
Autism	int,
Deaf_Blind	int	,
Deafness	int	,
Emotional	int	,
Hearing	int	,
Intellectual	int,
Learning_disab	int,
Multiple_disab	int,
Orthopedic	int,
Other_Health	int	,
Speech_or_lang	int	,
Traumatic	int	,
Visual_Impair	int	,
MealStatusGrouping	varchar(50),
EthnicityGroupCC	varchar(50),
Ethnicity_sort	int	,
Gradelevel	varchar(25),
Language	varchar(50),
Gender	varchar(50),
ELLStatus	varchar(7),
Classification	varchar(50),
Language_Sort	int	,
Grade_Sort	int	,
FosterCareFlag	varchar(3),
[STHFlagSort] [INT],
[FosterCareFlagSort] [INT]);

Declare @SQL varchar(max) = 'Insert into ##CCTotaltemp '+
'Select [ReportingDistrict],STHFlag'+
	   ',case when [Classification] = ' +'''Autism''' +
	   'then 1 '+
	   ' else 0 ' +
	   'end as'+ '''Autism'''+
	   ',case when [Classification] = '+'''Deaf-Blindness'''+
	   'then 1 '+ 
	   'else 0 ' +
	   'end as '+'''Deaf_Blind'''+
	   ',case when [Classification] = '+'''Deafness'''+
	   'then 1 '+
	   'else 0 '+
	   'end as '+'''Deafness'''+
	   ',case when [Classification] = '+'''Emotional Disability'''+
	   'then 1 '+
	   ' else 0 ' +
	   'end as '+'''Emotional'''+
	   ',case when [Classification] = '+'''Hearing Impairment'''+
	   'then 1 '+
	   'else 0 '+
	   'end as '+'''Hearing'''+
	   ',case when [Classification] = '+'''Intellectual Disability'''+
	   'then 1 '+
	   'else 0 '+
	   'end as '+'''Intellectual'''+
	   ',case when [Classification] = '+'''Learning Disability'''+
	   'then 1 ' +
	   'else 0 '+
	   'end as '+'''Learning_disab'''+
	   ',case when [Classification] = '+'''Multiple Disabilities'''+
	   'then 1 '+ 
	   'else 0 '+
	   'end as '+'''Multiple_disab'''+
	   ',case when [Classification] = '+'''Orthopedic Impairment'''+
	   'then 1'+ 
	   ' else 0 '+
	   'end as '+'''Orthopedic'''+
	   ',case when [Classification] = '+'''Other Health Impairment'''+
	   'then 1'+ 
	   ' else 0 '+
	   'end as '+'''Other_Health'''+
	   ',case when [Classification] = '+'''Speech or Language Impairment'''+
	   'then 1 '+
	   ' else 0 '+
	   'end as '+'''Speech_or_lang'''+
	   ',case when [Classification] = '''+'Traumatic Brain Injury'''+
	   'then 1 '+
	   ' else 0 '+
	   ' end as '+'''Traumatic'''+
	   ',case when [Classification] = '+'''Visual Impairment'''+
	   'then 1 '+ 
	   'else 0 '+
	   ' end as '+'''Visual_Impair'''+
	   ',[MealStatusGrouping]'+
	   ',case when [EthnicityGroupCC] is null then '+'''Other'''+
	   'else [EthnicityGroupCC]'+
	   'end as [EthnicityGroupCC]'+ 
	   ',case when [EthnicityGroupCC]  = '+'''Asian'''+' then 1'+
	   'when [EthnicityGroupCC]  = '+'''Black'''+' then 2'+
	   'when [EthnicityGroupCC]  = '+'''Hispanic'''+' then 3'+
	   'when [EthnicityGroupCC] = '+'''White''' +'then 4'+
	   'when ([EthnicityGroupCC] is Null or [EthnicityGroupCC] = '+'''Other'''+') then 5'+
	   ' end as Ethnicity_sort'+ 
	   ',a.Gradelevel'+
	   ',[OutcomeLanguageCC] as Language'+
	   ',a.Gender'+
	   ',case when [EllStatus] = '+'''NOT ELL'''+' then '+'''NOT ELL'''+
	   'when [EllStatus] = '+'''ELL'''+' then '+'''ELL'''+
	   'end as ELLStatus'+
	   ',[Classification]'+
	   ',case when ([OutcomeLanguageCC] = '+'''English'''+' OR [OutcomeLanguageCC] IS NULL) then 1'+
	   'when [OutcomeLanguageCC] = '+'''SPANISH'''+ ' then 2'+
	   'when [OutcomeLanguageCC] = '+'''CHINESE'''+ ' then 3'+
	   'when [OutcomeLanguageCC] = '+'''OTHER'''+' then 4'+
	   'when [OutcomeLanguageCC] = '+'''NOT APPLICABLE'''+' then 5 '+
	   'end as '+'''Language_Sort'''+
	   ',case when a.Gradelevel = '+'''0K'''+' then 1 '+
	   'when a.Gradelevel = '+'''01'''+ 'then 2'+
	   'when a.Gradelevel = '+'''02'''+' then 3'+
	   'when a.Gradelevel = '+'''03'''+' then 4'+
	   'when a.Gradelevel = '+'''04'''+' then 5'+
	   'when a.Gradelevel = '+'''05'''+' then 6'+
	   'when a.Gradelevel = '+'''06'''+' then 7'+
	   'when a.Gradelevel = '+'''07'''+' then 8'+
	   'when a.Gradelevel = '+'''08'''+' then 9'+
	   'when a.Gradelevel = '+'''09'''+' then 10'+
	   'when a.Gradelevel = '+'''10'''+' then 11'+
	   'when a.Gradelevel = '+'''11'''+' then 12'+
	   'when a.Gradelevel = '+'''12'''+' then 13 '+
	   ' end as '+'''Grade_Sort'''+
	   	   +',  case when FosterCareFlag = ''Y'' then '+'''YES'''+' else '+ '''NO'''+
		' end as FosterCareFlag '+
	   +' ,case when STHFlag = '+'''Y'''+' then 1'
	   +' when STHFlag  = '+'''N'''+' then 2 '
	   + ' end as STHFlagSort'
	   +' ,  case when FosterCareFlag = ''Y'' then 1 else 2 '
	   +' end as FosterCareFlagSort'+
	  ' FROM [SEO_MART].[snap].'+@tableNameCCStudentRegisterR814 +' a'+
	  ' where [Classification] <> '+'''Pre-school student with a Disability''' 
	--	' and [EnrolledDBN] <> '+'''02M972'''+' and ReportingDistrict <> '+'''98'''+
	--  ' and a.Gradelevel <> '+'''AD'''+' and a.Gender <> '+''' '''
	  
	  print @SQL
 	exec (@SQL)
	  
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
(4, 'Gender'),
(5, 'ELLStatus')


insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
(6, 'Language', 'Language_Sort'),
(7, 'GradeLevel', 'Grade_Sort'),
(8, 'STHFlag', 'STHFlagSort'),
(9, 'FostercareFlag', 'FosterCareFlagSort')



if object_id('tempdb..##totalRow') is not null
	 drop table ##totalRow 
	 	    
	  select 
	  'Total' as 'Header',
	    FORMAT(sum(Autism),'#,##0') as c1 
      ,FORMAT(sum(Deaf_Blind),'#,##0') as c2 
	  ,FORMAT(sum(Deafness),'#,##0') as c3 
      ,FORMAT(sum(Emotional),'#,##0') as c4
	  ,FORMAT(sum(Hearing),'#,##0') as c5
      ,FORMAT(sum(Intellectual),'#,##0') as c6
      ,FORMAT(sum(Learning_disab),'#,##0') as c7
      ,FORMAT(sum(Multiple_disab),'#,##0') as c8
      ,FORMAT(sum(Orthopedic) ,'#,##0') as  c9
      ,FORMAT(sum(Other_Health),'#,##0') as c10 
	  ,FORMAT(sum(Speech_or_lang),'#,##0') as c11
      ,FORMAT(sum(Traumatic),'#,##0') as  c12
      ,FORMAT(sum(Visual_Impair),'#,##0') as c13
	  ,FORMAT(sum(Autism)+sum(Deaf_Blind)+sum(Deafness)+sum(Emotional)+sum(Hearing)+sum(Intellectual)
	  +sum(Learning_disab)+sum(Multiple_disab)+sum(Orthopedic)+sum(Other_Health)+sum(Speech_or_lang)
	  +sum(Traumatic)+sum(Visual_Impair),'#,##0') as TotalRegister
	  into ##totalRow
	  from ##CCTotaltemp
	 
	if object_id('tempdb..##totalRow_Sort') is not null
	drop table ##totalRow_Sort 
	 	    
	  select 
	  '99' as 'Sort',
	  'Total' as 'Header',
	   FORMAT(sum(Autism),'#,##0') as c1 
      ,FORMAT(sum(Deaf_Blind),'#,##0') as c2 
	  ,FORMAT(sum(Deafness),'#,##0') as c3 
      ,FORMAT(sum(Emotional),'#,##0') as c4
	  ,FORMAT(sum(Hearing),'#,##0') as c5
      ,FORMAT(sum(Intellectual),'#,##0') as c6
      ,FORMAT(sum(Learning_disab),'#,##0') as c7
      ,FORMAT(sum(Multiple_disab),'#,##0') as c8
      ,FORMAT(sum(Orthopedic) ,'#,##0') as  c9
      ,FORMAT(sum(Other_Health),'#,##0') as c10 
	  ,FORMAT(sum(Speech_or_lang),'#,##0') as c11
      ,FORMAT(sum(Traumatic),'#,##0') as  c12
      ,FORMAT(sum(Visual_Impair),'#,##0') as c13
	  ,FORMAT(sum(Autism)+sum(Deaf_Blind)+sum(Deafness)+sum(Emotional)+sum(Hearing)+sum(Intellectual)
	  +sum(Learning_disab)+sum(Multiple_disab)+sum(Orthopedic)+sum(Other_Health)+sum(Speech_or_lang)
	  +sum(Traumatic)+sum(Visual_Impair),'#,##0') as TotalRegister
	  into ##totalRow_Sort
	  from ##CCTotaltemp

Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
select @rowCount = count(*) from ##group_and_sort_fields
declare @outputSQL nvarchar(max)
while @i <= @rowCount 
begin
	select @groupBy = '', @sortBy = '', @outputSQL = ''
	select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
	from ##group_and_sort_fields where outputOrderID = @i 

	select @outputSQL = 
	case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,TotalRegister from ( ' else ' ' end +
' select * from '+
' ( '+
' Select   ' + case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end  
+ case when @sortBy = ''
		then  @groupBy +' as sort '
		when  @i = 8 then ' case when '+@groupBy + ' = ' +'''Y'''+' then '+'''Yes'''+' else '+'''No'''+'  end as STHFlag'
		else  @groupBy  end  +
	  ',FORMAT(sum(Autism),''#,##0'') as c1 ' +
      ',FORMAT(sum(Deaf_Blind),''#,##0'') as c2 ' +
	  ',FORMAT(sum(Deafness),''#,##0'') as c3 ' +
      ',FORMAT(sum(Emotional),''#,##0'') as c4' +
	  ',FORMAT(sum(Hearing),''#,##0'') as c5' +
      ',FORMAT(sum(Intellectual),''#,##0'') as c6' +
      ',FORMAT(sum(Learning_disab),''#,##0'') as c7' +
      ',FORMAT(sum(Multiple_disab),''#,##0'') as c8' +
      ',FORMAT(sum(Orthopedic),''#,##0'') as  c9' +
      ',FORMAT(sum(Other_Health),''#,##0'') as c10 ' +
	  ',FORMAT(sum(Speech_or_lang),''#,##0'') as c11' +
      ',FORMAT(sum(Traumatic),''#,##0'') as  c12' +
      ',FORMAT(sum(Visual_Impair),''#,##0'') as c13' +
	  ',FORMAT(sum(Autism)+sum(Deaf_Blind)+sum(Deafness)+sum(Emotional)+sum(Hearing)+sum(Intellectual)+'+
	  'sum(Learning_disab)+sum(Multiple_disab)+sum(Orthopedic)+sum(Other_Health)+sum(Speech_or_lang)+'+
	  'sum(Traumatic)+sum(Visual_Impair)'+
	  ',''#,##0'') as TotalRegister' +
 ' FROM ##CCTotaltemp' +
 case when @i =8 then ' where STHFlag in ('+'''Y'''+', '+'''N'''+') ' 
	 else ' ' end 
+' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow ' else '##TotalRow_Sort ' end +
case when @sortBy != '' then ' ) a order by sort ' 
     when @i in (8,9) then ' ' else ' order by sort ' end
	
	
	print(@outputSQL)
	exec (@outputSQL)

	

	
	select @i = @i + 1


end

select 'Checking records count in ##CCTotaltemp '

	select count(*) from ##CCTotaltemp

END 
GO


