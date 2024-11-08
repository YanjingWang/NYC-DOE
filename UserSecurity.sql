  insert into [SEO_MART].[dbo].[lk_BICentralBCOUsers] ([SourceName]
      ,[BIRole]
      ,[LocationKey]
      ,[UserName]
      ,[UserEmail]
      ,[EffectiveStartDate]
      ,[EffectiveEndDate]
      ,[Status] 
	  ,[CreatedBy]
	  ,[ProcessedDate]
	  ,[SchoolYear]) values ('NULL','FSC','Access','Crystal Davis','CDavis34@schools.nyc.gov',(GETDATE()),'','1', 'Charlotte Wang',(GETDATE()),'2024-2025')


	  Delete from [SEO_MART].[dbo].[lk_BICentralBCOUsers]
	  Where useremail = 'AMiller14@schools.nyc.gov' 


	  select  top 10 * from [SEO_MART].[dbo].[lk_BICentralBCOUsers] where [UserEmail] = 'MLeong@schools.nyc.gov' 
	  select distinct [BIRole] from  [SEO_MART].[dbo].[lk_BICentralBCOUsers] --Central(all access); FSC(family support, location key,D75, certain district); Superintendent Support(DA79)
	  SELECT DISTINCT BIROLE, LOCATIONKEY FROM [dbo].[lk_BICentralBCOUsers] --Central	N/A
	  --remove people no longer need access
	  SELECT * FROM [SEO_MART].[dbo].[lk_BICentralBCOUsers]  WHERE USERNAME LIKE '%Abby%' --same agency but different role
	  --may add requestor column or put requestor for SourceName eg. Jared 
	  --may remove SchoolYear 

	  --NULL	FSC	Access	Abby Miller	AMiller14@schools.nyc.gov	2018-11-15	NULL	1	Psubburaja	2021-07-01	2021-2022	84	NULL
	  --BI Role: Central, FSC, Superintendent Support
	  --LocationKey: Access, D75, DA79,N/A, Bronx, Brooklyn North, Brooklyn South, Manhattan, Queens North, Queens South, Staten Island
	  --Status: 1, 0
	  --CreatedBy: Charlotte
	  --ProcessedDate: 2021-07-01
	  --SchoolYear: 2021-2022
	  --Id:1,2,3,4...etc
	  --EffectiveStartDate: 2021-07-01
	  --EffectiveEndDate: 2021-07-01
	  --UserEmail:
	  --UserName:
	  --SourceName: NULL, Jared, Charlotte, etc
	  --Requestor: NULL, Jared, Charlotte, etc
	  --select distinct BIRole, LocationKey from [SEO_MART].[dbo].[lk_BICentralBCOUsers] 


	  select distinct BIROLE, locationkey from [SEO_MART].[dbo].[lk_BICentralBCOUsers] 

	  --column [source name] is NULL so may redesign this table, from different users requests, we may use user team name or BI excel file instead of NULL
	  
	  SELECT * from [SEO_MART].[dbo].[lk_BICentralBCOUsers] 
