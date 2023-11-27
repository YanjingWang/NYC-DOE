if object_id('tempdb..#Report_Plac') is not null
	drop table #Report_Plac
select a.*, c.TempResFlag,
case when b.studentid is not null then 'Y' else 'N'
		end as FosterCareFlag
into #Report_Plac
from SEO_Mart.snap.CC_InitialReferralsR19_SY23_fix a
left join SEO_Mart.dbo.lk_FosterCare b on a.studentid=b.studentid
left join SEO_Mart.snap.INT_StudentDemographics_063023 c 
on a.studentid=c.studentid 
where a.GradeLevel <> 'PK'
and a.GradeLevel <> '99'
and a.ReportingDistrict <> '00';

update #Report_Plac set GradeLevel = 'KG' where GradeLevel = '0K'

if object_id('tempdb..#Report') is not null
	drop table #Report 
Select  StudentID 
	   ,ReportingDistrict 
	   ,ReportOutcomeCC 
	   ,MealStatusGrouping 
	   ,EthnicityGroupCC 
	   ,TempResFlag
	   ,FosterCareFlag
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
	    ,case when TempResFlag = 'Y' then 1
	   when TempResFlag  = 'N' then 2
	    end as TempResFlagSort
	   ,case when FosterCareFlag = 'Y' then 1
	   when FosterCareFlag  = 'N' then 2
	    end as FosterCareFlagSort
	into #Report 
    From #Report_Plac
	  where  ReportingDistrict  not in ('98', '99','00')
	  and  IsPWNDeferred  = 0 and  ReportOutcomeCC  = 'IEP' ;

if object_Id('tempdb..#group_and_sort_fields') is not null
	drop table #group_and_sort_fields
create table #group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))
go
insert into #group_and_sort_fields(outputOrderID, groupBy)
values 
(1, 'ReportingDistrict'),
(3, 'MealStatusGrouping'),
(4, 'Gender'),
(5, 'ELLStatus')

insert into #group_and_sort_fields(outputOrderID, groupBy, sortBy)
values 
(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
(6, 'OutcomeLanguageCC', 'Language_Sort'),
(7, 'GradeLevel', 'Grade_Sort'),
(8, 'TempResFlag', 'TempResFlagSort'),
(9, 'FostercareFlag', 'FosterCareFlagSort')

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
	  ', count(StudentID) as TOTAL_PWN ' +
	  ',cast((sum(OutcomePlacementSchoolDays)*1.0)/count(StudentID)  as numeric(8,2)) as Average_Days ' +
--      ',cast(AVG(OutcomePlacementSchoolDays) as numeric(8,2)) as Average_Days ' +
 ' FROM #Report' +
 ' group by ' + @groupBy + case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
 ' order by ' + case when @sortBy = '' then @groupBy else @sortBy end 

	execute(@outputSQL)
	
	select @i = @i + 1
end

