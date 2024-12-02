USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCCTriannualReportRSSchoolLevel]    Script Date: 12/2/2024 2:24:47 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE Procedure [dbo].[USPCCTriannualReportRSSchoolLevel]

As

BEGIN

Set XACT_Abort on
Set NoCount On

/*************************************************************************************************
Object Name:	USPCCTriannualReportRSSchoolLevel
Purpose:	Create RS School Level Triannual report	
Ticket:     MIS-10333
Modification Details:
Author				ModifiedDate		Comments
------------------	------------		-------------------------------
Charlotte			    09/19/2024			
**************************************************************************************************/
Begin Try


Declare @TableNameCC_RSMandateR13 Varchar(100) = Null
Declare @TableNameCC_StudentRegisterR814 Varchar(100) = Null
Declare @Snapshot_Date as date
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
Set @TableNameCC_StudentRegisterR814=QuoteName(Concat('CC_StudentRegisterR814_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))

If Object_ID('tempdb..##RSSchoolLevel') is not null
Drop Table ##RSSchoolLevel

Create Table ##RSSchoolLevel
([School DBN] Varchar(9) NULL
,[Related Services Recommendation Type] Varchar(Max) NULL
,[Full Encounter] Varchar(10) NULL
,[Percent Full Encounter] Varchar(50) NULL
,[Partial Encounter] Varchar(50) NULL
,[Percent Partial Encounter] Varchar(50) NULL
,[No Encounter] Varchar(10)
,[Percent No Encounter] Varchar(Max)
)

Declare @SQL Varchar(Max)=
'Insert into ##RSSchoolLevel
Select * 
from
(
select 
  EnrolledDBN as [School DBN]
 ,MandatesBilingual as [Related Services Recommendation Type]
 ,FullEncounter as [Full Encounter] 
 ,Percentfull as [Percent Full Encounter] 
 ,PartialEncounter as [Partial Encounter] 
 ,PercentPartial as [Percent Partial Encounter] 
 , NoEncounter as [No Encounter] 
 ,PercentNo as [Percent No Encounter] 
 from 
 (
 select distinct 
   EnrolledDBN
  ,MandatesBilingual 
  ,cast(Sum(FullEncounter) as varchar) as FullEncounter
  ,cast(Sum(FullEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentFull
  ,cast(sum(PartialEncounter) as varchar) as PartialEncounter
  ,Cast(Sum(PartialEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartial
  ,cast(sum(NoEncounter)as varchar) as NoEncounter
  ,cast(Sum(NoEncounter)*1.0/nullif(Count(studentid),0) as varchar) as PercentNo
  from(Select a.studentid
   ,b.EnrolledDBN 
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
   FROM [SEO_MART].[snap].' + @tableNameCC_RSMandateR13+'  as a With (NoLock)
    left join [SEO_MART].[snap].'+  @tableNameCC_StudentRegisterR814 +'as b With (NoLock)
	on a.studentid = b.studentid ) as c
   group by EnrolledDBN
   , MandatesBilingual
   ) as c 
) As RSSchoolLevel'

Execute(@SQL)

Set @SQL=
'Insert into ##RSSchoolLevel
Select * 
from
(
   select distinct
   ''Total'' as [School DBN]
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

Execute (@SQL)

Declare @OutputSQL Varchar(Max)=
'Select * 
from ##RSSchoolLevel
order by 
case when [School DBN]=''Total'' then
''zzzzz''
End 
,[School DBN]
,[Related Services Recommendation Type]
' 
Execute (@OutputSQL)

Print(@OutputSQL)

End Try

Begin Catch

Select Error_Message() as ErrMessage;

End Catch

Set NoCount Off

End


GO


