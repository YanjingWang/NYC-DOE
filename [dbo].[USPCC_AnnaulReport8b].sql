USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport8b]    Script Date: 11/12/2024 3:19:17 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

/************************************************************************************************************************************************************************
Object Name: dbo.USPCCAnnaulReport8b
Purpose:	This procedure returns data for City Council Annaul Report c "SWDs by School"
	SWD = Students with Disabilities
	This particular annual report is based off of June 15th snapshot.
	While city council annual reports are usually based off on June 30th (end of year) snapshots, 
	for this report we use 6/15. Reason: Schools may discharge students early (between June 20th and June 29th).
	It's safe to assume that any student who was active till 6/15 to have completed the school year.

	Python program will call this stored procedure to generate the Excel Report for CC annual report

Date Created: 10/23/2023
Modification Details:

Author			ModifiedDate		Comments
Raji Munnangi	10/23/2023			Initial version
Charlotte Wang  10/24/2023          Added comma for every three digit and percentage % and Total row at the end  of each table
Charlotte Wang    11/09/2023         Created  Final version
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART

Raji Munnangi	06/25/2024			Replaced TempResFlag with STHFlag to identify "Students in Temporary Housing"
***************************************************************************************************************************************************************************/
CREATE procedure [dbo].[USPCC_AnnaulReport8b]
	@tableNameCCStudentRegisterR814 varchar(100) = ''
as
begin

	declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCStudentRegisterR814, '') = ''
	begin
		set @tableNameCCStudentRegisterR814 = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end 

	IF OBJECT_ID('tempdb..##Report8b') IS NOT NULL
	DROP TABLE ##Report8b;

	CREATE TABLE ##Report8b(
	[StudentID] [int]  NULL,
	[Classification] [varchar](50) NULL,
	[EnrolledDBN] [varchar](10) NULL,
	[ReportingDistrict] [varchar](7) NULL,
	[STHFlag] [varchar](1) NULL,
	[STHFlagSort] [int]  NULL,
	[RecommendPlacementDesc] [varchar](70) NULL,
	[IEPRecFlag] [varchar](15) NULL,
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

declare @Report8b varchar(max) = ' insert into ##Report8b '+
' Select a.StudentID '+
		' ,a.Classification '+
		' ,a.EnrolledDBN '+
	    ' ,a.ReportingDistrict '+
		' ,a.STHFlag '+
		' ,case when a.STHFlag =''Y'' then 1 else 2 '+
		' end as STHFlagSort '+
	  ' ,a.RecommendPlacementDesc  '+
	  	' ,CASE WHEN a.MRERecommendation = ''Special Class''  '+
		' and RecommendPlacementDesc in (''NYSED-Approved Non Public School - Day'', '+
		' ''NYSED-Approved Non Public School - Residential'', '+
		' ''NYS Supported Non Public School – 4201 - Day'') '+
          ' Then  ''SpecialClassNPS'' '+
		 ' WHEN a.MRERecommendation = ''Special Class'' and a.AdminDistrict=''75''  '+
           '   THEN  ''SpecialClassD75'' '+
		 ' WHEN a.MRERecommendation = ''Special Class'' and a.AdminDistrict<>''75''  '+
           '   THEN ''SpecialClass'' '+
		 ' WHEN a.MRERecommendation in (''RS Only'', ''Other Program'', ''No Services'') '+
           '   THEN ''RSOnly'' '+
		 ' WHEN a.MRERecommendation like ''%SETSS%'' '+
           '   THEN ''SETSS'' '+
		 ' WHEN a.MRERecommendation like ''%Co-%'' '+
         '     THEN ''ICT''  '+
		' 	end as IEPRecFlag '+
	   
	   ' ,a.[MealStatusGrouping] '+
	   ' ,case when a.[EthnicityGroupCC] is null then ''Other'' '+
	   ' else a.[EthnicityGroupCC] '+
	   ' end as [EthnicityGroupCC]  '+
	   ' ,case when a.[EthnicityGroupCC]  = ''Asian'' then 1 '+
	   ' when a.[EthnicityGroupCC]  = ''Black'' then 2 '+
	   ' when a.[EthnicityGroupCC]  = ''Hispanic'' then 3 '+
	   ' when a.[EthnicityGroupCC] = ''White'' then 4 '+
	   ' when (a.[EthnicityGroupCC] is Null or a.[EthnicityGroupCC] = ''Other'') then 5 '+
	   ' end as Ethnicity_sort  '+
	   ' ,a.GradeLevel '+
	   ' ,a.OutcomeLanguageCC '+
	     ' ,case when (a.OutcomeLanguageCC = ''English'' OR a.OutcomeLanguageCC IS NULL) then 1 '+
	   ' when a.OutcomeLanguageCC = ''SPANISH'' then 2 '+
	   ' when a.OutcomeLanguageCC = ''CHINESE'' then 3 '+
	   ' when a.OutcomeLanguageCC = ''OTHER'' then 4 '+
	    ' end as OutcomeLanguageCCSort '+
	   ' ,a.Gender '+
	   ' ,a.[ELLStatus] '+
	 -- ,a.[EnrolledDBN]
	   ' ,case when a.GradeLevel = ''0K'' then 1  '+
	   ' when a.GradeLevel = ''01'' then 2 '+
	   ' when a.GradeLevel = ''02'' then 3 '+
	   ' when a.GradeLevel = ''03'' then 4 '+
	   ' when a.GradeLevel = ''04'' then 5 '+
	   ' when a.GradeLevel = ''05'' then 6 '+
	   ' when a.GradeLevel = ''06'' then 7 '+
	   ' when a.GradeLevel = ''07'' then 8 '+
	   ' when a.GradeLevel = ''08'' then 9 '+
	   ' when a.GradeLevel = ''09'' then 10 '+
	   ' when a.GradeLevel = ''10'' then 11 '+
	   ' when a.GradeLevel = ''11'' then 12 '+
	   ' when a.GradeLevel = ''12'' then 13 '+
	   ' end as GradeSort '+
	   ' ,  case when FosterCareFlag = ''Y'' then ''Y'' else ''N'' '+
		' end as FosterCareFlag '+
		' ,  case when FosterCareFlag = ''Y'' then 1 else 2 '+
		' end as FosterCareFlagSort '+
	  ' FROM [SEO_MART].[snap].'+@tableNameCCStudentRegisterR814+' a '
	   ;
	  

	   print(@Report8b)
	   execute(@Report8b)

	IF OBJECT_ID('tempdb..##CCTotaltemp8b') IS NOT NULL
	DROP TABLE ##CCTotaltemp8b;


select *, CASE when IEPRecFlag='SpecialClassNPS'
             THEN 1 ELSE 0 
                     END AS SpecialClassNPS
		,CASE when IEPRecFlag='SpecialClassD75'
             THEN 1 ELSE 0 
                     END AS SpecialClassD75
		,CASE when IEPRecFlag='SpecialClass'
             THEN 1 ELSE 0 
                     END AS SpecialClass
		,CASE when IEPRecFlag='RSOnly'
             THEN 1 ELSE 0 
                     END AS RSOnly
		,CASE when IEPRecFlag='SETSS'
             THEN 1 ELSE 0 
                     END AS SETSS
		,CASE when IEPRecFlag='ICT'
             THEN 1 ELSE 0 
                     END AS ICT

	Into ##CCTotaltemp8b from ##Report8b



	if object_Id('tempdb..##group_and_sort_fields') is not null
		drop table ##group_and_sort_fields
	create table ##group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))
	insert into ##group_and_sort_fields(outputOrderID, groupBy)
	values 
	(1, 'ReportingDistrict'),
	(3, 'MealStatusGrouping'),
	(4, 'Gender'),
	(5, 'ELLStatus'),
	(8,'Classification')

	insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
	values 
	(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
	(6, 'OutcomeLanguageCC', 'OutcomeLanguageCCSort'),
	(7, 'GradeLevel', 'GradeSort'),
	(9, 'STHFlag', 'STHFlagSort'),
	(10, 'FostercareFlag', 'FosterCareFlagSort')



	if object_id('tempdb..##totalRow8b') is not null
	 drop table ##totalRow8b 
	 	    
	  select 
	  'Total' as 'Header'
	  ,FORMAT(sum(RSOnly), '#,##0') as c1 
	 		  ,CONCAT(cast((sum(RSOnly)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7) ), '%') as c2 
	 		  ,FORMAT(sum(SETSS), '#,##0') as c3 
	 		  ,CONCAT(cast((sum(SETSS)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c4 
	 		  ,FORMAT(sum(ICT), '#,##0') as c5 
	 		  ,CONCAT(cast((sum(ICT)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c6
	 		  ,FORMAT(sum(SpecialClass), '#,##0') as c7 
	 		  ,CONCAT(cast((sum(SpecialClass)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c8 
	 		  ,FORMAT(sum(SpecialClassD75), '#,##0') as c9 
	 		 ,CONCAT(cast((sum(SpecialClassD75)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c10 
	 		  ,FORMAT(sum(SpecialClassNPS), '#,##0') as c11 
	 		  ,CONCAT(cast((sum(SpecialClassNPS)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c12
	into ##totalRow8b
	  from ##CCTotaltemp8b
	 
	if object_id('tempdb..##totalRow_Sort8b') is not null
	drop table ##totalRow_Sort8b 
	 	    
				select 
				'99' as 'Sort',
				'Total' as 'Header'
			  ,FORMAT(sum(RSOnly), '#,##0') as c1 
	 		  ,CONCAT(cast((sum(RSOnly)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c2 
	 		  ,FORMAT(sum(SETSS), '#,##0') as c3 
	 		  ,CONCAT(cast((sum(SETSS)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c4 
	 		  ,FORMAT(sum(ICT), '#,##0') as c5 
	 		  ,CONCAT(cast((sum(ICT)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c6
	 		  ,FORMAT(sum(SpecialClass), '#,##0') as c7 
	 		  ,CONCAT(cast((sum(SpecialClass)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c8 
	 		  ,FORMAT(sum(SpecialClassD75), '#,##0') as c9 
	 		  ,CONCAT(cast((sum(SpecialClassD75)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c10 
	 		  ,FORMAT(sum(SpecialClassNPS), '#,##0') as c11 
	 		  ,CONCAT(cast((sum(SpecialClassNPS)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), '%') as c12 
			into ##totalRow_Sort8b
			from ##CCTotaltemp8b
 

	Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
	select @rowCount = count(*) from ##group_and_sort_fields
	declare @outputSQL nvarchar(max)
	while @i <= @rowCount 
	begin
		select @groupBy = '', @sortBy = '', @outputSQL = ''
		select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
		from ##group_and_sort_fields where outputOrderID = @i 

	 select @outputSQL = case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12 from ( ' else ' ' end +
' select * from '+
' ( '+ 
	 	'Select '+  
  case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end +
  case when @sortBy = ''
		then  @groupBy +' as sort '
		else  @groupBy  end  +  
	 		  ',FORMAT(sum(RSOnly), ''#,##0'') as c1 ' +
	 		  ',CONCAT(cast((sum(RSOnly)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), ''%'') as c2 ' +
	 		  ',FORMAT(sum(SETSS), ''#,##0'') as c3 ' +
	 		  ',CONCAT(cast((sum(SETSS)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), ''%'') as c4 ' +
	 		  ',FORMAT(sum(ICT), ''#,##0'') as c5 ' +
	 		  ',CONCAT(cast((sum(ICT)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), ''%'') as c6 ' +
	 		  ',FORMAT(sum(SpecialClass), ''#,##0'') as c7 ' +
	 		  ',CONCAT(cast((sum(SpecialClass)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), ''%'') as c8 ' +
	 		  ',FORMAT(sum(SpecialClassD75), ''#,##0'') as c9 ' +
	 		  ',CONCAT(cast((sum(SpecialClassD75)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), ''%'') as c10 ' +
	 		  ',FORMAT(sum(SpecialClassNPS), ''#,##0'') as c11 ' +
	 		  ',CONCAT(cast((sum(SpecialClassNPS)*1.0)/(nullif(Count(studentid),0))*100 as numeric(7)), ''%'') as c12 ' +
	 ' FROM ##CCTotaltemp8b ' +
	 ' group by ' + @groupBy + case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
	 -- case when @i=8 then ' order by 1 ' else ' ' end +
	 ' ) a '+ 
' union all '+
' select * from '+ case when @sortBy = '' then '##TotalRow8b ' else '##TotalRow_Sort8b ' end +
case when @sortBy != '' then ' ) a order by sort '
	 when @i = 8 then ' '
      else ' order by sort ' end 
	 
	 

		exec (@outputSQL)
	
		select @i = @i + 1
		print(@outputSQL)
	end
end
GO


