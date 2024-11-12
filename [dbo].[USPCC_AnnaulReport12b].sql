USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCC_AnnaulReport12b]    Script Date: 11/12/2024 3:41:50 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE procedure [dbo].[USPCC_AnnaulReport12b] 
@tableNameCCPSStudentR12 varchar(100) = ''

As
/************************************************************************************************************************
Program				       : Report 12b
Purpose				       : Citywide Bilingual Special Education Programs
Project				       : City council
Programmer			       : Charlotte Wang
Modifications		       : Created the SQL script
Created by				   : Charlotte Wang
Comments				   : Created store proc using existing SAS Script 
Modifications		       : 05/10/2024 Move Annual City Council Report Stored Procedures to SEO MART from SEO_Reporting
Ticket                     :https://seoanalytics.atlassian.net/browse/MIS-11160 Move Annual City Council Report Stored Procedures to SEO MART
************************************************************************************************************************/

BEGIN

declare @currYear_YY char(2)
	set @currYear_YY = right(CONVERT(char(10), getdate(), 101), 2)
	if isnull(@tableNameCCPSStudentR12, '') = ''
	begin
		set @tableNameCCPSStudentR12 = 'CC_PSStudentR12_0615' + @currYear_YY
	end 


	IF OBJECT_ID('tempdb..##Report_12Bil') IS NOT NULL
	DROP TABLE ##Report_12Bil;

CREATE TABLE ##Report_12Bil(
	[PrimaryProgramType] [varchar](40) NULL,
	[c1] [varchar](30) NULL,
	[c2] [varchar](30) NULL,
	[c3] [varchar](30) NULL,
	[c4] [varchar](30) NULL,
	[c5] [varchar](30) NULL,
	[c6] [varchar](30) NULL
) ON [PRIMARY]


DECLARE @CCTotaltemp_12b VARCHAR(MAX) =' Insert into ##Report_12Bil '+
'select * from '+
'( '+
'select * from  '+
'( '+
    -- Citywide roll-up
 'select distinct '+ 
	'PrimaryProgramType  '+
  ',FORMAT(Sum(FullyReceiving) , ''#,##0'') as c1 '+
  ',CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100  as numeric(7)), ''%'') as c2 '+
  ',FORMAT(sum(PartiallyReceiving) , ''#,##0'') as c3 '+
  ',CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100  as numeric(7)), ''%'') as c4 '+
  ',FORMAT(sum(NotReceiving) , ''#,##0'') as c5 '+
  ',CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100  as numeric(7)), ''%'')as c6 '+
  'from(Select a.studentid '+
   ',a.PrimaryProgramType  '+
   ',case when compliancecategoryCC = 100 then 1  '+
   'else 0 '+
   'end as ''FullyReceiving'' '+
   ',case when compliancecategoryCC = 50 then 1 '+
   'else 0  '+
   'end as ''PartiallyReceiving''  '+
   ',case when compliancecategorycc = 0 then 1  '+
   'else 0  '+
   'end as ''NotReceiving''  '+
   'FROM  [SEO_MART].[snap].'+@tableNameCCPSStudentR12+' as a where a.AdminDistrict <>79 '+
   'and PSOutcomeLanguage <> ''ENGLISH''  '+
   ') as a '+
   'group by PrimaryProgramType   '+
   --order by PrimaryProgramType 
   ') cityide '+

    'union all '+
	'select * from ( '+
 'select distinct ''Total'' PrimaryProgramType '+
   ',FORMAT(Sum(FullyReceiving) , ''#,##0'') as c1 '+
  ',CONCAT(cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c2 '+
  ',FORMAT(sum(PartiallyReceiving) , ''#,##0'') as c3 '+
  ',CONCAT(cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0)*100 as numeric(7)), ''%'') as c4 '+
  ',FORMAT(sum(NotReceiving) , ''#,##0'') as c5 '+
  ',CONCAT(cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0)*100  as numeric(7)), ''%'') as c6 '+
  'from(Select a.studentid '+
   ',a.PrimaryProgramType  '+
   ',case when compliancecategoryCC = 100 then 1  '+
   'else 0 '+
   'end as ''FullyReceiving'' '+
   ',case when compliancecategoryCC = 50 then 1 '+
   'else 0  '+
   'end as ''PartiallyReceiving''  '+
   ',case when compliancecategorycc = 0 then 1  '+
   'else 0  '+
   'end as ''NotReceiving''  '+
    ' FROM  [SEO_MART].[snap].'+@tableNameCCPSStudentR12+' as a where a.AdminDistrict <>79 '+
   'and PSOutcomeLanguage <> ''ENGLISH''  '+
   ') as a)  as total '+

   ') as rep12 '


	print (@CCTotaltemp_12b);
	execute (@CCTotaltemp_12b)


	declare @outputSQL varchar(100) = ' Select PrimaryProgramType,c1,c2,c3,c4,c5,c6 from ##Report_12Bil ';

	execute (@outputSQL)
	print (@outputSQL)

   
   END;
GO


