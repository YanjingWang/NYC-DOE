USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCCTriannualReportRSSuperintendent]    Script Date: 12/2/2024 2:25:33 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE Procedure [dbo].[USPCCTriannualReportRSSuperintendent]

As

BEGIN


Set XACT_Abort on
Set NoCount On


/*************************************************************************************************
Object Name:	USPCCTriannualReportRSSuperintendent
Purpose:	Create RS Superintendent Triannual report	
Ticket:     MIS-10333
Modification Details:
Author				ModifiedDate		Comments
------------------	------------		-------------------------------
Charlotte			    09/19/2024			
**************************************************************************************************/
Begin Try

Declare @TableNameCC_RSMandateR13 Varchar(100) = Null
Declare @TableNameRPT_Locations Varchar(100) = Null
Declare @Snapshot_Date as Date

Declare @err_message varchar(255)
Declare @Counter as Int

Set @Counter=
(Select Count(*) as [Counter]
from
(Select LookupValue 
from [SEO_MART].[dbo].[lk_SEOBusinessRules] wwith (Nolock)
where (LookupCategory='CCTriAnnualReportsSnapShotDates'
And isactive=1)
) 
as Counter)

If @Counter=0

Begin

Set @Err_Message='IsActive field in the lk_SEOBusinessrules table is not set to true for any of the records'
Select @Err_Message ErrMessage

End

Else If @Counter>1

Begin

Set @Err_Message='There is more then one record set to true in IsActive field in the lk_SEOBusinessrules table'
Select @Err_Message as ErrMessage

End

Else 

Begin

Set @Snapshot_Date=
(Select LookupValue 
from [SEO_MART].[dbo].[lk_SEOBusinessRules] with (Nolock)
where LookupCategory='CCTriAnnualReportsSnapShotDates'
And isactive=1
)

End


Set @TableNameCC_RSMandateR13=
QuoteName(Concat('CC_RSMandateR13_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))
Set @TableNameRPT_Locations=
QuoteName(Concat('RPT_Locations_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))

If Object_ID('tempdb..##RSSuperintendent') is not null
Drop Table ##RSSuperintendent

Create Table ##RSSuperintendent
(Superintendent Varchar(100) NULL
,SuperintendentDistrict Varchar(100) NULL
,[Related Services Recommendation Type] Varchar(50) NULL
,[Full Encounter] Varchar(10) NULL
,[Percent Full Encounter] Varchar(50) NULL
,[Partial Encounter] Varchar(10) NULL
,[Percent Partial Encounter] Varchar(50)
,[No Encounter] Varchar(10)
,[Percent No Encounter] Varchar(50)
)

Declare @SQL Varchar(Max)=
'Insert Into ##RSSuperIntendent
 Select 
  SuperintendentName as Superintendent
 ,SuperintendentDistrict
 ,MandatesBilingual 
 ,FullEncounter 
 ,Percentfull 
 ,PartialEncounter 
 ,PercentPartial 
 ,NoEncounter 
 ,PercentNo 
 from 
 (
 Select Distinct 
  Superintendentname
 ,Superintendentdistrict
 ,MandatesBilingual
  ,cast(Sum(FullEncounter) as varchar) as FullEncounter
  ,cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentFull
  ,cast(sum(PartialEncounter) as varchar) as PartialEncounter
  ,Cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartial
  ,cast(sum(NoEncounter)as varchar) as NoEncounter
  ,cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentNo
  from(Select a.studentid
  ,SuperintendentName
  ,SuperintendentDistrict
   ,case when servicetype = ''Counseling Services'' and 
   RSMandateLanguage <> ''English'' then 
   ''Counseling Services Bilingual''
  when ServiceType = ''Speech-Language Therapy'' and 
  RSMandateLanguage <> ''English'' then 
  ''Speech-Language Therapy Bilingual''
  else 
  ServiceType 
  end as MandatesBilingual 
   ,case when EncounterStatus = ''Full Encounter'' then 
   1 
   else 
   0
   end as FullEncounter
   ,case when EncounterStatus = ''Partial Encounter'' then 
   1
   else 
   0 
   end as PartialEncounter 
   ,case when EncounterStatus= ''No Encounter'' then 
   1 
   else 
   0 
   end as NoEncounter 
   FROM [SEO_MART].[snap].'+@TableNameCC_RSMandateR13+' as a 
   left join (Select schooldbn
   ,SuperintendentDistrict
   ,case when  SuperintendentName = ''MARY ANNE SHEPPARD'' then 
   ''SHEPPARD, MARY ANNE''
   when  SuperintendentName = ''THOMAS MCBRYDE JR'' then 
   ''MCBRYDE JR, THOMAS''
   when  SuperintendentName = ''JOSEPH OBRIEN'' then 
  ''OBRIEN, JOSEPH''
   else 
   SuperintendentName 
   end as SuperintendentName
  from [SEO_MART].[snap].'+@TableNameRPT_Locations+') as b 
  on a.EnrolledDBN = b.SchoolDBN) as c
  group by SuperintendentName
  ,MandatesBilingual
  ,[SuperintendentDistrict]
) as Superintendent'

Execute(@SQL)

Set @SQL=
'Insert into ##RSSuperintendent
Select * 
from
(
   select distinct
   ''Total'' as Superintendent
  ,'''' as SupeintendentDistrict
  ,'''' as [Related Services Recommendation Type]
  ,cast(Sum(FullEncounter) as varchar) as [Full Encounter]
  ,cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0) as varchar) as [Percent Full Encounter]
  ,cast(sum(PartialEncounter) as varchar) as [Partial Encounter]
  ,Cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0) as varchar) as [Percent Partial Encounter]
  ,cast(sum(NoEncounter)as varchar) as [No Encounter]
  ,cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0) as varchar) as [Percent No Encounter]
  from(Select a.studentid
   ,ReportingDistrict
   ,case when servicetype = ''Counseling Services'' and 
   RSMandateLanguage <> ''English'' then 
   ''Counseling Services Bilingual''
  when ServiceType = ''Speech-Language Therapy'' and 
  RSMandateLanguage <> ''English'' then 
  ''Speech-Language Therapy Bilingual''
  else 
  ServiceType 
  end as MandatesBilingual 
   ,case when EncounterStatus = ''Full Encounter'' then 
   1 
   else 
   0
   end as FullEncounter
   ,case when EncounterStatus = ''Partial Encounter'' then 
   1
   else 
   0 
   end as PartialEncounter 
   ,case when EncounterStatus= ''No Encounter'' then 
   1 
   else 
   0 
   end as NoEncounter  
   FROM [SEO_MART].[snap].'+@TableNameCC_RSMandateR13+' as a with (NoLock)
) as c
) as RSCitywideRollup'

Execute (@SQL)

Declare @OutputSQL Varchar(Max)=
'Select * 
from ##RSSuperintendent
Order by
case when [SuperIntendent]=''Total'' then
''zzzzz''
End
,Superintendent
,[Related Services Recommendation Type]
,SuperintendentDistrict'

Execute (@OutputSQL)

Print(@OutputSQL)

End Try

Begin Catch

Select Error_Message() as ErrMessage;

End Catch

End

Set NoCount Off



GO


