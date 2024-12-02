USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCCTriannualReportRSDistrict]    Script Date: 12/2/2024 2:24:13 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE Procedure [dbo].[USPCCTriannualReportRSDistrict]

As

Begin

Set XACT_Abort on
Set NoCount On

/*************************************************************************************************
Object Name:	USPCCTriannualReportRSDistrict
Purpose:	Create RS District Triannual report	
Ticket:     MIS-10333
Modification Details:
Author				ModifiedDate		Comments
------------------	------------		-------------------------------
Charlotte			    09/19/2024			
**************************************************************************************************/
Begin Try

Declare @TableNameCC_RSMandateR13 as Varchar(100) = Null
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


Set @TableNameCC_RSMandateR13=QuoteName(Concat('CC_RSMandateR13_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))


BEGIN

If Object_ID('tempdb..##RSDistrict') Is Not Null
Drop Table ##RSDistrict

Create Table ##RSDistrict
([School District] Varchar(5) NULL
,[Related Services Recommendation Type] Varchar(Max) NULL
,[Full Encounter] Varchar(10) NULL
,[Percent Full Encounter] Varchar(50) NULL
,[Partial Encounter] Varchar(50) NULL
,[Percent Partial Encounter] Varchar(50) NULL
,[No Encounter] Varchar(10)
,[Percent No Encounter] Varchar(Max)
)

Declare @SQL Varchar(Max)=
'Insert into ##RSDistrict
Select * 
from
(
Select distinct 
   ReportingDistrict 
  ,MandatesBilingual 
  ,cast(Sum(FullEncounter) as varchar) as FullEncounter
  ,cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentFull
  ,cast(sum(PartialEncounter) as varchar) as PartialEncounter
  ,Cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartial
  ,cast(sum(NoEncounter)as varchar) as NoEncounter
  ,cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentNo
  from (
  Select a.studentid
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
   end as ''FullEncounter''
   ,case when EncounterStatus = ''Partial Encounter'' then 
   1
   else 
   0 
   end as ''PartialEncounter'' 
   ,case when EncounterStatus= ''No Encounter'' then 
   1 
   else 
   0 
   end as ''NoEncounter'' 
   FROM [SEO_MART].[snap].'+@TableNameCC_RSMandateR13+' as a
) as c
 group by ReportingDistrict
 , MandatesBilingual
) as RSMandate'

Execute(@SQL)

End

Begin

Set @SQL =
'Insert into ##RSDistrict
Select * 
from
(
   select distinct
   ''Total'' as [School District]
   ,'''' as [Related Services Recommendation Type]
  ,cast(Sum(FullEncounter) as varchar) as FullEncounter
  ,cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentFull
  ,cast(sum(PartialEncounter) as varchar) as PartialEncounter
  ,Cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartial
  ,cast(sum(NoEncounter)as varchar) as NoEncounter
  ,cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentNo
  from
  (
  Select a.studentid
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

Execute(@SQL)

Declare @OutputSQL Varchar(Max)=
'Select * 
from ##RSDistrict
order by [School District]
,[Related Services Recommendation Type]'

Execute (@OutputSQL)

Print(@OutputSQL)
End

End Try

Begin Catch

Select Error_Message() as ErrMessage;

End Catch

Set NoCount Off

End


GO


