
/************************************************************************************************************************
Program				       : Initials.sas
Purpose				       : 1.To create an Initial City council report and generate redacted output.(Note: Run till Part:1 , commenting test_arrays to get unredacted outputs)
					         2.Generate an RTF document using Proc report
					         3.To load data(redacted/unredacted) into the Excel report
Project				       : City council
Programmer			       : Hemalatha Vadlamani
Creation /Finalized Date   : Finalized on 10/01/2018
Comments			       : RAJI created this SQL script on 10/18/2023 

8/29/2019: JV: 
Updated variable names. 
Updated source table
Switched references from Hema's personal drives to City Council folder on R drive. 
Updated year. 
Removed redaction logic.
Excluded District 00

10/18/2023: Raji:
Raji created this SQL script based on SAS code for Reports 1-4
************************************************************************************************************************/
if object_id('tempdb..#Report_Ini') is not null
	drop table #Report_Ini
select a.*, c.TempResFlag,
case when b.studentid is not null then 'Y' else 'N'
		end as FosterCareFlag
into #Report_Ini
from SEO_Mart.snap.CC_InitialReferralsR19_SY23 a
left join SEO_Mart.dbo.lk_FosterCare b on a.studentid=b.studentid
left join SEO_Mart.snap.INT_StudentDemographics_063023 c on a.studentid=c.studentid 
WHERE referraldate < '07-01-2023' AND referraldate >= '07-01-2022' 
AND a.GradeLevel <> '99' AND a.GradeLevel <> 'PK'

update #Report_Ini set GradeLevel = 'KG' where GradeLEvel = '0K'
/*
select top 10 * from #Report_Ini
*/
if object_id('tempdb..#Report_Working') is not null
	drop table #Report_Working
Select studentid,
	    ReportingDistrict
	   ,ReportOutcomeCC
	   ,1 as STUDENTS_WITH_REF
	   ,MealStatusGrouping
	   ,EthnicityGroupCC
	   	,TempResFlag
  
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
	    ,case when TempResFlag = 'Y' then 1
	   when TempResFlag  = 'N' then 2
	    end as TempResFlagSort
	   ,FosterCareFlag
	    ,case when FosterCareFlag = 'Y' then 1
	   when FosterCareFlag  = 'N' then 2
	    end as FosterCareFlagSort
	into #Report_Working 
	FROM #Report_Ini  a
	WHERE ReportingDistrict <> '00' ;

if object_id('tempdb..#Report_Final') is not null
	drop table #Report_Final;
with cteReport as 
(
	select *, case when CLOSED_WITHOUT_IEP=1 or INELIGIBLE_LESS_60=1 or INELIGIBLE_MORE_60=1  then 'UNDETERMINED'
	when OutcomeLanguageCC = 'ENGLISH' then 'ENGLISH'
	   when OutcomeLanguageCC = 'SPANISH' then 'SPANISH'
	   when OutcomeLanguageCC = 'CHINESE' then 'CHINESE'
	   when OutcomeLanguageCC = 'OTHER' then 'OTHER'
	  end as LanguageOfInstructionCC2  
	from #Report_Working 
) 
select *, case when LanguageOfInstructionCC2 = 'ENGLISH' then 1
	   when LanguageOfInstructionCC2 = 'SPANISH' then 2
	   when LanguageOfInstructionCC2 = 'CHINESE' then 3
	   when LanguageOfInstructionCC2 = 'OTHER' then 4
	   when LanguageOfInstructionCC2 = 'UNDETERMINED' then 5
	   end as Language_Sort
into #Report_Final
from cteReport 

if object_id('Tempdb..#totalRow') is not null
	drop table #totalRow
Select  
    'Total' as 'Header'
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
into #TotalRow
FROM #Report_Final

if object_id('Tempdb..#totalRow_Sort') is not null
	drop table #totalRow_Sort 
Select  
    '99' as 'sort'
	,'Totals' as 'Header'
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
into #TotalRow_Sort
FROM #Report_Final

Select  
    ReportingDistrict
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by ReportingDistrict
union all 
select * from #TotalRow
order by ReportingDistrict

select * from 
(
Select  
	EthnicityGroupCC_sort as 'sort'
    ,EthnicityGroupCC
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by EthnicityGroupCC, EthnicityGroupCC_sort
) a 
union all
select * from #TotalRow_Sort
order by sort


Select  
    MealStatusGrouping
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by MealStatusGrouping
union all
select * from #TotalRow
order by MealStatusGrouping

Select  
    GENDER
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by GENDER 
union all
select * from #TotalRow
order by GENDER 

Select  
    ELLStatus
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by ELLStatus
union all
select * from #TotalRow
order by ELLStatus

select * from 
(
Select  
	Language_Sort as 'sort'
    ,LanguageOfInstructionCC2
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by LanguageOfInstructionCC2, Language_Sort
) a
union all 
select * from #TotalRow_Sort
order by sort

select * from 
(
Select  
	GradeLevel_Sort as 'sort'
    ,GradeLevel
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by GradeLevel, GradeLevel_Sort
) a
union all 
select * from #TotalRow_Sort
order by sort

select * from 
(
	Select  
	TempResFlagSort as 'sort'
    ,(case when TempResFlag = 'Y' then 'Yes' else 'No' end) as TempResFlag
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
where TempResFlag in ('Y', 'N')
group by TempResFlag, TempResFlagSort
) a
union all 
select * from #TotalRow_Sort
order by sort

select * from 
(
Select  
	FosterCareFlagSort as 'sort'
    ,FosterCareFlag
	,sum(STUDENTS_WITH_REF) as c1 
    ,sum(CLOSED_WITHOUT_IEP) as c2
	,sum(INELIGIBLE_LESS_60) as c3
    ,sum(INELIGIBLE_MORE_60) as c4
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)) as c5
    ,sum(CLASSIFIED_LESS_60) as c6
    ,sum(CLASSIFIED_MORE_60) as c7
    ,sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60) as C8 
	,sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)) as c9 
	,sum(TOTAL_AWAITING) as c10		
	,sum(TOTAL_OPEN) as c11 
FROM #Report_Final
group by FosterCareFlag, FosterCareFlagSort
) a
union all 
select * from #TotalRow_Sort
order by sort

