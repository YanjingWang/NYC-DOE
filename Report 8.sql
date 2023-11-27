IF OBJECT_ID('tempdb..#CCTotaltemp') IS NOT NULL
	DROP TABLE #CCTotaltemp;
Select 
	    [ReportingDistrict]
		,TempResFlag
	   ,case when [ELLStatus] = 'NOT ELL' 
	   and ([OutcomeLanguageCC] = 'English' OR [OutcomeLanguageCC] IS NULL)
	   then 1
	   else 0
	   end as 'Non_ELL_English'
	   ,case when [ELLStatus] = 'NOT ELL' 
	   and [OutcomeLanguageCC] = 'Spanish'
	   then 1
	   else 0
	   end as 'Non_ELL_Spanish'
	   ,case when [ELLStatus] = 'NOT ELL' 
	   and [OutcomeLanguageCC] = 'Chinese'
	   then 1
	   else 0
	   end as 'Non_ELL_Chinese'
	   ,case when [ELLStatus] = 'NOT ELL' 
	   and [OutcomeLanguageCC] = 'Other'
	   then 1
	   else 0
	   end as 'Non_ELL_Other'	   
	   ,case when [ELLStatus] = 'ELL' 
	   and ([OutcomeLanguageCC] = 'English' OR [OutcomeLanguageCC] IS NULL)
	   then 1
	   else 0
	   end as 'ELL_English'
	   ,case when [ELLStatus] = 'ELL' 
	   and [OutcomeLanguageCC] = 'Spanish'
	   then 1
	   else 0
	   end as 'ELL_Spanish'
	   ,case when [ELLStatus] = 'ELL' 
	   and [OutcomeLanguageCC] = 'Chinese'
	   then 1
	   else 0
	   end as 'ELL_Chinese'
	   ,case when [ELLStatus] = 'ELL' 
	   and [OutcomeLanguageCC] = 'Other'
	   then 1
	   else 0
	   end as 'ELL_Other'
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
	   ,a.GradeLevel
	   ,[OutcomeLanguageCC]
	   ,a.Gender
	   ,[ELLStatus]
	   ,[Classification]
	   ,[EnrolledDBN]
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
	   end as 'Grade_Sort'
	   ,  case when b.studentid is not null then 'Y' else 'N'
		end as FosterCareFlag
	   into #CCTotaltemp
      FROM [SEO_MART].[snap].[CC_StudentRegisterR814_061523] a
	  left join SEO_Mart.dbo.lk_FosterCare b on a.studentid=b.studentid

	  where [Classification] <> 'Pre-school student with a Disability'  
		and [EnrolledDBN] <> '02M972' and ReportingDistrict <> '98'
	  and a.GradeLevel <> 'AD' and a.Gender <> ' ' 

	  --select * from #CCTotaltemp;


Select  
      ReportingDistrict
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by ReportingDistrict
 order by ReportingDistrict

Select  
       EthnicityGroupCC, Ethnicity_sort
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish +ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by EthnicityGroupCC, Ethnicity_sort
 order by Ethnicity_sort

 Select  
      MealStatusGrouping
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by MealStatusGrouping
 order by MealStatusGrouping

 Select  
      Gender
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by Gender
 order by Gender

 	Select  
       GradeLevel, Grade_Sort
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish +ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by GradeLevel, Grade_Sort
 order by Grade_Sort

 Select  
      Classification
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by Classification
 order by Classification

 Select  
      TempResFlag
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by TempResFlag
 order by TempResFlag

 Select  
      FostercareFlag
	  ,sum(Non_ELL_English) as c1
      ,sum(Non_ELL_Spanish) as c2
	  ,sum(Non_ELL_Chinese) as c3
      ,sum(Non_ELL_Other) as c4
	  ,sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) as c5 
      ,sum(ELL_English) as c6
      ,sum(ELL_Spanish) as c7
      ,sum(ELL_Chinese) as c8
      ,sum(ELL_Other) as  c9
      ,sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) as c10 
 FROM #CCTotaltemp
 group by FostercareFlag
 order by FostercareFlag

