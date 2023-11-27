/************************************************************************************************************************
Program				       : Disability.sas
Purpose				       : 1.To create an City council Disability Classification report and generate redacted output.(Note: Run till Part:1 , commenting test_arrays to get unredacted outputs)
					         2.Generate an RTF document using Proc report
					         3.To load data(redacted/unredacted) into the Excel report
Project				       : City council
Programmer			       : Hemalatha Vadlamani
Creation /Finalized Date   : Finalized on 10/01/2018
Comments			       : 
Modifications		       : 

8/29/2019: Julius Vizner made the following changes:

Updated register source location
Updated year
Updated variable names
Commented out redaction logic (three parts)
Excluded ReportingDistrict 98


09/21 : Updated the classification 'Emotional Disturbance' to 'Emotional Disability'
************************************************************************************************************************/

IF OBJECT_ID('tempdb..#CCTotaltemp') IS NOT NULL
	DROP TABLE #CCTotaltemp;
Select 
	    [ReportingDistrict]
		,TempResFlag
	   ,case when [Classification] = 'Autism'
	   then 1 
	   else 0
	   end as 'Autism'
	   ,case when [Classification] = 'Deaf-Blindness'
	   then 1 
	   else 0
	   end as 'Deaf_Blind'
	   ,case when [Classification] = 'Deafness'
	   then 1 
	   else 0
	   end as 'Deafness'
	   ,case when [Classification] = 'Emotional Disability'
	   then 1 
	   else 0
	   end as 'Emotional'
	   ,case when [Classification] = 'Hearing Impairment'
	   then 1 
	   else 0
	   end as 'Hearing'
	   ,case when [Classification] = 'Intellectual Disability'
	   then 1 
	   else 0
	   end as 'Intellectual'
	   ,case when [Classification] = 'Learning Disability'
	   then 1 
	   else 0
	   end as 'Learning_disab'
	   ,case when [Classification] = 'Multiple Disabilities'
	   then 1 
	   else 0
	   end as 'Multiple_disab'
	   ,case when [Classification] = 'Orthopedic Impairment'
	   then 1 
	   else 0
	   end as 'Orthopedic'
	   ,case when [Classification] = 'Other Health Impairment'
	   then 1 
	   else 0
	   end as 'Other_Health'
	   ,case when [Classification] = 'Speech or Language Impairment'
	   then 1 
	   else 0
	   end as 'Speech_or_lang'
	   ,case when [Classification] = 'Traumatic Brain Injury'
	   then 1 
	   else 0
	   end as 'Traumatic'
	   ,case when [Classification] = 'Visual Impairment'
	   then 1 
	   else 0
	   end as 'Visual_Impair'
	   ,[MealStatusGrouping]
	   ,case when [EthnicityGroupCC] is null then 'Other'
	   else [EthnicityGroupCC]
	   end as [EthnicityGroupCC] 
	   ,case when [EthnicityGroupCC]  = 'Asian' then 1
	   when [EthnicityGroupCC]  = 'Black' then 2
	   when [EthnicityGroupCC]  = 'Hispanic' then 3
	   when [EthnicityGroupCC] = 'White' then 4
	   when ([EthnicityGroupCC] is Null or [EthnicityGroupCC] = 'Other') then 5
	   end as Ethnicity_sort 
	   ,a.Gradelevel
	   ,[OutcomeLanguageCC] as Language
	   ,a.Gender
	   ,case when [EllStatus] = 'NOT ELL' then 'NOT ELL'
	   when [EllStatus] = 'ELL' then 'ELL'
	   end as ELLStatus
	   ,[Classification]
	   ,case when ([OutcomeLanguageCC] = 'English' OR [OutcomeLanguageCC] IS NULL) then 1
	   when [OutcomeLanguageCC] = 'SPANISH' then 2
	   when [OutcomeLanguageCC] = 'CHINESE' then 3
	   when [OutcomeLanguageCC] = 'OTHER' then 4
	   when [OutcomeLanguageCC] = 'NOT APPLICABLE' then 5
	   end as 'Language_Sort'
	   ,case when a.Gradelevel = '0K' then 1 
	   when a.Gradelevel = '01' then 2
	   when a.Gradelevel = '02' then 3
	   when a.Gradelevel = '03' then 4
	   when a.Gradelevel = '04' then 5
	   when a.Gradelevel = '05' then 6
	   when a.Gradelevel = '06' then 7
	   when a.Gradelevel = '07' then 8
	   when a.Gradelevel = '08' then 9
	   when a.Gradelevel = '09' then 10
	   when a.Gradelevel = '10' then 11
	   when a.Gradelevel = '11' then 12
	   when a.Gradelevel = '12' then 13
	   end as 'Grade_Sort'
	   	   ,  case when b.studentid is not null then 'Y' else 'N'
		end as FosterCareFlag
	   into #CCTotaltemp
      FROM [SEO_MART].[snap].[CC_StudentRegisterR814_061523] a
	  left join SEO_Mart.dbo.lk_FosterCare b on a.studentid=b.studentid

	  where [Classification] <> 'Pre-school student with a Disability'  
		and [EnrolledDBN] <> '02M972' and ReportingDistrict <> '98'
	  and a.Gradelevel <> 'AD' and a.Gender <> ' ' 

if object_Id('tempdb..#group_and_sort_fields') is not null
	drop table #group_and_sort_fields
create table #group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))
go
insert into #group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'Gender'),
(5, 'ELLStatus'),
(8, 'TempResFlag'),
(9, 'FostercareFlag')

insert into #group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
(6, 'Language', 'Language_Sort'),
(7, 'GradeLevel', 'Grade_Sort')

Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
select @rowCount = count(*) from #group_and_sort_fields
declare @outputSQL nvarchar(max)
while @i <= @rowCount 
begin
	select @groupBy = '', @sortBy = '', @outputSQL = ''
	select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
	from #group_and_sort_fields where outputOrderID = @i 

	select @outputSQL =  
	'Select  ' + 
       @groupBy + 
	  ',sum(Autism) as c1 ' +
      ',sum(Deaf_Blind) as c2 ' +
	  ',sum(Deafness) as c3 ' +
      ',sum(Emotional) as c4' +
	  ',sum(Hearing) as c5' +
      ',sum(Intellectual) as c6' +
      ',sum(Learning_disab) as c7' +
      ',sum(Multiple_disab) as c8' +
      ',sum(Orthopedic) as  c9' +
      ',sum(Other_Health) as c10 ' +
	  ',sum(Speech_or_lang) as c11' +
      ',sum(Traumatic) as  c12' +
      ',sum(Visual_Impair) as c13' +
 ' FROM #CCTotaltemp' +
 ' group by ' + @groupBy + case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
 ' order by ' + case when @sortBy = '' then @groupBy else @sortBy end 

	exec (@outputSQL)
	
	select @i = @i + 1
end