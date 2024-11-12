USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport8]    Script Date: 11/12/2024 3:11:23 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[USPCC_AnnaulReport8]
@tableNameCCStudentRegisterR814 varchar(100) = ''
AS
--exec USPCCAnnaulReport8 'CC_StudentRegisterR814_061523'
--exec USPCC_AnnaulReport8 'CC_StudentRegisterR814_061523'
/************************************************************************************************************************************************************************
Object Name: USPCCAnnaulReport8c
Purpose:	This procedure returns data for City Council Annaul Report c "SWDs by School"
	SWD = Students with Disabilities
	This particular annual report is based off of June 15th snapshot.
	While city council annual reports are usually based off on June 30th (end of year) snapshots, 
	for this report we use 6/15. Reason: Schools may discharge students early (between June 20th and June 29th).
	It's safe to assume that any student who was active till 6/15 to have completed the school year.

	Python program will call this stored procedure to generate the Excel Report for CC annual report

Date Created: 11/02/2023
Modification Details:

Author			ModifiedDate		Comments
Charlotte Wang		11/02/2023			Initial version
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART
Raji Munnangi		06/25/2024			Replaced TempResFlag with STH flag
***************************************************************************************************************************************************************************/

BEGIN

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	
	if isnull(@tableNameCCStudentRegisterR814, '') = ''
	begin
		set @tableNameCCStudentRegisterR814 = 'CC_StudentRegisterR814_0615' + @currYear_YY
	end 


IF OBJECT_ID('tempdb..##CCTotaltemp8') IS NOT NULL
	DROP TABLE ##CCTotaltemp8;

	CREATE TABLE ##CCTotaltemp8(
	[ReportingDistrict] [varchar](7) NULL,
	[STHFlag] [varchar](1) NULL,
	[Non_ELL_English] [int]  NULL,
	[Non_ELL_Spanish] [int]  NULL,
	[Non_ELL_Chinese] [int]  NULL,
	[Non_ELL_Other] [int]  NULL,
	[ELL_English] [int]  NULL,
	[ELL_Spanish] [int]  NULL,
	[ELL_Chinese] [int]  NULL,
	[ELL_Other] [int]  NULL,
	[MealStatusGrouping] [varchar](50) NULL,
	[EthnicityGroupCC] [varchar](50) NULL,
	[Ethnicity_sort] [int] NULL,
	[GradeLevel] [varchar](25) NULL,
	[OutcomeLanguageCC] [varchar](50) NULL,
	[Gender] [varchar](50) NULL,
	[ELLStatus] [varchar](7) NULL,
	[Classification] [varchar](50) NULL,
	[EnrolledDBN] [varchar](10) NULL,
	[Grade_Sort] [int] NULL,
	[FosterCareFlag] [varchar](3)  NULL,
	[STHFlagSort] [INT],
	[FosterCareFlagSort] [INT]
) 


DECLARE @SQL VARCHAR(max)='INSERT INTO ##CCTotaltemp8'
+' Select '
	    +' [ReportingDistrict]'
		+' ,STHFlag'
	   +' ,case when [ELLStatus] = '+'''NOT ELL''' 
	   +' and ([OutcomeLanguageCC] = '+'''English'''+' OR [OutcomeLanguageCC] IS NULL)'
	   +' then 1'
	   +' else 0'
	   +' end as '+'''Non_ELL_English'''
	   +' ,case when [ELLStatus] = '+'''NOT ELL''' 
	   +' and [OutcomeLanguageCC] = '+'''Spanish'''
	   +' then 1'
	   +' else 0'
	   +' end as '+'''Non_ELL_Spanish'''
	   +' ,case when [ELLStatus] = '+'''NOT ELL''' 
	   +' and [OutcomeLanguageCC] = '+'''Chinese'''
	   +' then 1'
	   +' else 0'
	   +' end as '+'''Non_ELL_Chinese'''
	   +' ,case when [ELLStatus] = '+'''NOT ELL''' 
	   +' and [OutcomeLanguageCC] = '+'''Other'''
	   +' then 1'
	   +' else 0'
	   +' end as '+'''Non_ELL_Other'''	   
	   +' ,case when [ELLStatus] = '+'''ELL''' 
	   +' and ([OutcomeLanguageCC] = '+'''English'''+' OR [OutcomeLanguageCC] IS NULL)'
	   +' then 1'
	   +' else 0'
	   +' end as '+'''ELL_English'''
	   +' ,case when [ELLStatus] = '+'''ELL''' 
	   +' and [OutcomeLanguageCC] = '+'''Spanish'''
	   +' then 1'
	   +' else 0'
	   +' end as '+'''ELL_Spanish'''
	   +' ,case when [ELLStatus] = '+'''ELL''' 
	   +' and [OutcomeLanguageCC] = '+'''Chinese'''
	   +' then 1'
	   +' else 0'
	   +' end as '+'''ELL_Chinese'''
	   +' ,case when [ELLStatus] = '+'''ELL''' 
	   +' and [OutcomeLanguageCC] = '+'''Other'''
	   +' then 1'
	   +' else 0'
	   +' end as '+'''ELL_Other'''
	   +' ,[MealStatusGrouping]'
	   +' ,case when [EthnicityGroupCC] is null then '+'''Other'''
	   +' else [EthnicityGroupCC]'
	   +' end as [EthnicityGroupCC] '
	   +' ,case when [EthnicityGroupCC]  = '+'''Asian'''+' then 1'
	   +' when [EthnicityGroupCC]  = '+'''Black'''+' then 2'
	   +' when [EthnicityGroupCC]  = '+'''Hispanic'''+' then 3'
	   +' when [EthnicityGroupCC] = '+'''White'''+' then 4'
	   +' when ([EthnicityGroupCC] is Null or [EthnicityGroupCC] = '+'''Other'''+') then 5'
	   +' end as Ethnicity_sort '
	   +' ,a.GradeLevel'
	   +' ,[OutcomeLanguageCC]'
	   +' ,a.Gender'
	   +' ,[ELLStatus]'
	   +' ,[Classification]'
	   +' ,[EnrolledDBN]'
	   +' ,case when a.GradeLevel = '+'''0K'''+' then 1' 
	   +' when a.GradeLevel = '+'''01'''+' then 2'
	   +' when a.GradeLevel = '+'''02'''+' then 3'
	   +' when a.GradeLevel = '+'''03'''+' then 4'
	   +' when a.GradeLevel = '+'''04'''+' then 5'
	   +' when a.GradeLevel = '+'''05'''+' then 6'
	   +' when a.GradeLevel = '+'''06'''+' then 7'
	   +' when a.GradeLevel = '+'''07'''+' then 8'
	   +' when a.GradeLevel = '+'''08'''+' then 9'
	   +' when a.GradeLevel = '+'''09'''+' then 10'
	   +' when a.GradeLevel = '+'''10'''+' then 11'
	   +' when a.GradeLevel = '+'''11'''+' then 12'
	   +' when a.GradeLevel = '+'''12'''+' then 13'
	   +' end as '+'''Grade_Sort'''
	   +' ,  case when FosterCareFlag = ''Y'' then '+'''Yes'''+' else '+'''No'''
	   +' end as FosterCareFlag'
	   +' ,case when STHFlag = '+'''Y'''+' then 1'
	   +' when STHFlag  = '+'''N'''+' then 2 '
	   + ' end as STHFlagSort'
	   +' ,  case when FosterCareFlag = ''Y'' then 1 else 2 '
	   +' end as FosterCareFlagSort'
	  +' FROM [SEO_MART].[snap].'+@tableNameCCStudentRegisterR814 +' a'
	 -- +' where [Classification] <> '+'''Pre-school student with a Disability'''  
	 -- +' and [EnrolledDBN] <> '+'''02M972'''+' and ReportingDistrict <> '+'''98'''
	 -- +' and a.GradeLevel <> '+'''AD'''+' and a.Gender <> '+''' ''' 

	  --select * from ##CCTotaltemp8;

	  PRINT(@SQL)
	  EXEC ( @SQL )
	  
if object_Id('tempdb..##group_and_sort_fields') is not null
		drop table ##group_and_sort_fields
	create table ##group_and_sort_fields(outputOrderID int, groupBy varchar(100), sortBy varchar(100))
	insert into ##group_and_sort_fields(outputOrderID, groupBy)
	values 
	(1, 'ReportingDistrict'),
	(3, 'MealStatusGrouping'),
	(4, 'Gender'),
	(6, 'Classification')
	
	
	insert into ##group_and_sort_fields(outputOrderID, groupBy, sortBy)
	values 
	(2, 'EthnicityGroupCC', 'Ethnicity_sort'),
	(5, 'GradeLevel', 'Grade_Sort'),
	(7, 'STHFlag', 'STHFlagSort'),
	(8, 'FostercareFlag', 'FosterCareFlagSort')

	if object_id('tempdb..##totalRow') is not null
	 drop table ##totalRow 
	 	    
	  select 
	  'Total' as 'Header',
	    FORMAT(sum(Non_ELL_English),'#,##0') as c1 
      ,FORMAT(sum(Non_ELL_Spanish),'#,##0') as c2 
	  ,FORMAT(sum(Non_ELL_Chinese),'#,##0') as c3 
      ,FORMAT(sum(Non_ELL_Other),'#,##0') as c4
	  ,FORMAT(sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other),'#,##0') as c5
      ,FORMAT(sum(ELL_English),'#,##0') as c6
      ,FORMAT(sum(ELL_Spanish),'#,##0') as c7
      ,FORMAT(sum(ELL_Chinese),'#,##0') as c8
      ,FORMAT(sum(ELL_Other) ,'#,##0') as  c9
      ,FORMAT(sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other),'#,##0') as c10 
	  ,FORMAT(sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) + sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) , '#,##0') as TotalRegister 
	  into ##totalRow
	  from ##CCTotaltemp8
	 
	if object_id('tempdb..##totalRow_Sort') is not null
	drop table ##totalRow_Sort 
	 	    
	  select 
	  '99' as 'Sort',
	  'Total' as 'Header',
	   FORMAT(sum(Non_ELL_English),'#,##0') as c1 
      ,FORMAT(sum(Non_ELL_Spanish),'#,##0') as c2 
	  ,FORMAT(sum(Non_ELL_Chinese),'#,##0') as c3 
      ,FORMAT(sum(Non_ELL_Other),'#,##0') as c4
	  ,FORMAT(sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other),'#,##0') as c5
      ,FORMAT(sum(ELL_English),'#,##0') as c6
      ,FORMAT(sum(ELL_Spanish),'#,##0') as c7
      ,FORMAT(sum(ELL_Chinese),'#,##0') as c8
      ,FORMAT(sum(ELL_Other) ,'#,##0') as  c9
      ,FORMAT(sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other),'#,##0') as c10 
	  ,FORMAT(sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) + sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) , '#,##0') as TotalRegister 
	  into ##totalRow_Sort
	  from ##CCTotaltemp8
	
Declare @rowCount int = 0, @i int = 1, @groupBy varchar(100), @sortBy varchar(100)
	select @rowCount = count(*) from ##group_and_sort_fields
	declare @outputSQL nvarchar(max)
	while @i <= @rowCount 
	begin
		select @groupBy = '', @sortBy = '', @outputSQL = ''
		select @groupBy = groupBy, @sortBy = isnull(sortBy, '') 
		from ##group_and_sort_fields where outputOrderID = @i 
 select @outputSQL =
 case when @sortBy != '' then 'select '+@groupBy+', c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 '+
 ',  TotalRegister from ( ' else ' ' end +
 ' select * from '+
' ( '+
' Select   ' + case when @sortBy = '' then ' ' else  @sortBy + ' as sort , '   end  
+ case when @sortBy = ''
		then  @groupBy +' as sort '
		when  @i = 7 then ' case when '+@groupBy + ' = ' +'''Y'''+' then '+'''Yes'''+' else '+'''No'''+'  end as STHFlag'
		else  @groupBy  end  
	  +' ,FORMAT(sum(Non_ELL_English), ''#,##0'') as c1'
      +' ,FORMAT(sum(Non_ELL_Spanish), ''#,##0'') as c2'
	  +' ,FORMAT(sum(Non_ELL_Chinese), ''#,##0'') as c3'
      +' ,FORMAT(sum(Non_ELL_Other), ''#,##0'') as c4'
	  +' ,FORMAT(sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other), ''#,##0'') as c5 '
      +' ,FORMAT(sum(ELL_English), ''#,##0'') as c6'
      +' ,FORMAT(sum(ELL_Spanish), ''#,##0'') as c7'
      +' ,FORMAT(sum(ELL_Chinese), ''#,##0'') as c8'
      +' ,FORMAT(sum(ELL_Other), ''#,##0'') as  c9'
      +' ,FORMAT(sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other), ''#,##0'') as c10 '
	  +' ,FORMAT(sum(Non_ELL_English + Non_ELL_Spanish + Non_ELL_Chinese + Non_ELL_Other) + sum(ELL_English + ELL_Spanish + ELL_Chinese + ELL_Other) , ''#,##0'') as TotalRegister '
	 +' FROM ##CCTotaltemp8'+
	case when @i =7 then ' where STHFlag in ('+'''Y'''+', '+'''N'''+') ' 
	 else ' ' end 
	  +' group by '+ @groupBy +  case when @sortBy = '' then ' ' else ', ' end + @sortBy + 
	   ' ) a '+ 
	   ' union all '+
	   ' select * from '+ case when @sortBy = '' then '##TotalRow ' else '##TotalRow_Sort ' end +
case when @sortBy != '' then ' ) a order by sort ' else ' order by sort ' end
	
		
		print(@outputSQL)
		exec (@outputSQL)
	
		select @i = @i + 1
		
	end
 
 end;
GO


