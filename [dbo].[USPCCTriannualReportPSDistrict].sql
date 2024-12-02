USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCCTriannualReportPSDistrict]    Script Date: 12/2/2024 2:19:36 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE Procedure [dbo].[USPCCTriannualReportPSDistrict]

As

Begin

Set XACT_Abort on
Set NoCount On

/*************************************************************************************************
Object Name:	USPCCTriannualReportPSDistrict
Purpose:	Create PS District Triannual report	
Ticket:     MIS-10333
Modification Details:
Author				ModifiedDate		Comments
------------------	------------		-------------------------------
Charlotte			    09/19/2024			
**************************************************************************************************/

Begin Try

Declare @TableNameCC_PSStudentR12 as Varchar(100) = Null
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

Set @TableNameCC_PSStudentR12=QuoteName(Concat('CC_PSStudentR12_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))

Begin

If Object_ID('tempdb..##PSDistrict') Is Not Null
Drop Table ##PSDistrict

Create Table ##PSDistrict
([School District] Varchar(5) NULL
,[Primary Program Type] Varchar(50) NULL
,[Fully Receiving] Varchar(10) NULL
,[Percent Fully Receiving] Varchar(25) NULL
,[Partially Receiving] Varchar(25) NULL
,[Percent Partially Receiving] Varchar(25) NULL
,[Not Receiving] Varchar(25)
,[Percent Not Receiving] Varchar(25)
)

Declare @SQL Varchar(Max)=
'Insert into ##PSDistrict
Select * 
from
(
 select ReportingDistrict as [School District]
 , PrimaryProgramType as [Primary Program Type]
 , fullyreceiving as [Fully Receiving] 
 , Percentfully as [Percent Fully Receiving] 
 , partiallyreceiving as [Partially Receiving] 
 , PercentPartially as [Percent Partially Receiving]
 , notreceiving as [Not Receiving] 
 ,PercentNot as [Percent Not Receiving] 
 from (select distinct ReportingDistrict 
  ,primaryprogramtype 
  ,cast(Sum(FullyReceiving) as varchar) as FullyReceiving
  ,cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentFully
  ,cast(sum(PartiallyReceiving) as varchar) as PartiallyReceiving
  ,Cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartially
  ,cast(sum(NotReceiving)as varchar) as NotReceiving
  ,cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentNot
  from(Select a.studentid
  ,a.ReportingDistrict
  , a.PrimaryProgramType 
   ,case when compliancecategoryCC = 100 then
   1 
   else 
   0
   end as FullyReceiving
   ,case when compliancecategoryCC = 50 then 
   1
   else 
   0 
   end as PartiallyReceiving 
   ,case when compliancecategorycc = 0 then 
   1 
   else 
   0 
   end as NotReceiving 
   FROM [SEO_MART].[snap].'+@TableNameCC_PSStudentR12+' as a with (NoLock)
 where a.AdminDistrict <>79 
) as c
   group by ReportingDistrict, PrimaryProgramType
   ) as c 
  ) as PSDistrict'
Execute(@SQL)

Set @SQL =
'Insert into ##PSDistrict
Select * from
(
 select distinct 
 ''Total'' as PrimaryProgramtype
  ,'''' as [Primary Program Type]
  ,cast(Sum(FullyReceiving) as varchar) as FullyReceiving
  ,cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentFully
  ,cast(sum(PartiallyReceiving) as varchar) as PartiallyReceiving
  ,Cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartially
  ,cast(sum(NotReceiving)as varchar) as NotReceiving
  ,cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentNot
  from(Select a.studentid
   ,a.PrimaryProgramType 
   ,case when compliancecategoryCC = 100 then 
   1 
   else 
   0
   end as FullyReceiving
   ,case when compliancecategoryCC = 50 then 
   1
   else 
   0 
   end as PartiallyReceiving
   ,case when compliancecategorycc = 0 then 
   1 
   else 
   0 
   end as NotReceiving 
   FROM  [SEO_MART].[snap].'+@tableNameCC_PSStudentR12+' as a With (NoLock)
   where a.AdminDistrict <>79
   ) as a
  ) as PSCityWide_Rollup'

Execute(@SQL)

Declare @OutputSQL Varchar(Max)=
'Select * 
from ##PSDistrict
order by 
case when [School District]=''Total'' then
''zzzzz''
End
,[School District]
,[Primary Program Type]'

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


