select DISTINCT StudentID from [SEO_MART].[arch].[INT_T5StudentZoneSchool] --134,187 Distinct studentID 39,770
select * from [SEO_MART].[arch].[INT_T5StudentZoneSchool] WHERE StudentID = 253807044
select * from [SEO_MART].[dbo].[RPT_Locations] WHERE SchoolType = 'CSD' and SchoolDBN not in ('20KCPV') and (Longitude != 0 and Latitude != 0)
select DISTINCT SchoolDBN from [SEO_MART].[dbo].[RPT_Locations] WHERE SchoolDBN IS NOT NULL and Longitude = 0 and Latitude = 0 and ActiveFlag = 'Y'  --ALL NPS SCHOOLS and SchoolType = 'CSD'
select DISTINCT SchoolDBN from [SEO_MART].[dbo].[RPT_Locations] WHERE SchoolDBN IS NOT NULL and Longitude = 73.999467 and Latitude = 40.638286 --20KCPV
select * from SEO_Reporting.BI.VW_HeatMap --NPS student info 


select DISTINCT StudentID from [SEO_REPORTING].[dbo].[NPSStudentAddress_060324]