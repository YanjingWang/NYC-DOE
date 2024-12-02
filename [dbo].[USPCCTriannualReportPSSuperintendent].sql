USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPCCTriannualReportPSSuperintendent]    Script Date: 12/2/2024 2:23:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE Procedure [dbo].[USPCCTriannualReportPSSuperintendent]

As

BEGIN

Set XACT_Abort on
Set NoCount On

/*************************************************************************************************
Object Name:	USPCCTriannualReportPSSuperintendent
Purpose:	Create PS Superintendent Triannual report	
Ticket:     MIS-10333
Modification Details:
Author				ModifiedDate		Comments
------------------	------------		-------------------------------
Charlotte			    09/19/2024			
**************************************************************************************************/
Begin Try

Declare @TableNameCC_PSStudentR12 Varchar(100) = Null
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

Set @TableNameCC_PSStudentR12=
QuoteName(Concat('CC_PSStudentR12_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))
Set @TableNameRPT_Locations=
QuoteName(Concat('RPT_Locations_',Format(Cast(@Snapshot_Date as Date),'MMddyy')))

If Object_ID('tempdb..##PSSuperintendent') is not null
Drop Table ##PSSuperintendent

Create Table ##PSSuperintendent
(Superintendent Varchar(100) NULL
,[School District] Varchar(100) NULL
,[Primary Program Type] Varchar(50) NULL
,[Fully Receiving] Varchar(10) NULL
,[Percent Fully Receiving] Varchar(50) NULL
,[Partially Receiving] Varchar(10) NULL
,[Percent Partially Receiving] Varchar(50) Null
,[Not Receiving] Varchar(10) Null
,[Percent Not Receiving] Varchar(50) Null
)
 
 Declare @SQL Varchar(Max)=
 
'Insert Into ##PSSuperIntendent
select SuperintendentName as [Superintendent]
 , [SuperintendentDistrict] as [School District]
 , PrimaryProgramType as [Primary Program Type]
 , fullyreceiving as [Fully Receiving]
 , Percentfully as [Percent Fully Receiving] 
 , partiallyreceiving as [Partially Receiving] 
 , PercentPartially as [Percent Partially Receiving] 
 , notreceiving as [Not Receiving] 
 ,PercentNot as [Percent Not Receiving]
 from 
 (select distinct 
   SuperintendentName
  ,[SuperintendentDistrict]
  ,primaryprogramtype 
  ,cast(Sum(FullyReceiving) as varchar) as FullyReceiving
  ,cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentFully
  ,cast(sum(PartiallyReceiving) as varchar) as PartiallyReceiving
  ,Cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartially
  ,cast(sum(NotReceiving)as varchar) as NotReceiving
  ,cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentNot
  from(Select a.studentid
  ,[SuperintendentName]
  ,[SuperintendentDistrict]
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
   FROM  [SEO_MART].[snap].'+@TableNameCC_PSStudentR12+' as a 
   left join(select schooldbn
   , [SuperintendentDistrict]
   ,case when  SuperintendentName = ''MARY ANNE SHEPPARD'' then 
   ''SHEPPARD, MARY ANNE''
   when  SuperintendentName = ''THOMAS MCBRYDE JR'' then 
   ''MCBRYDE JR, THOMAS''
   when  SuperintendentName = ''JOSEPH OBRIEN'' then 
   ''OBRIEN, JOSEPH''
   else 
   SuperintendentName 
   end as SuperintendentName
  from [SEO_MART].[snap].'+@TableNameRPT_Locations+') as c 
  on a.enrolledDBN = c.SchoolDBN
   where a.AdminDistrict <>79
   ) as c
   group by SuperintendentName
   , PrimaryProgramType
   ,[SuperintendentDistrict]
   ) as d'

Execute (@SQL)

Set @SQL=
'Insert into ##PSSuperIntendent
Select * from
(
 select distinct 
 ''Total'' as Superintendent
 ,'''' as [School District]
 ,'''' as [Primary Program Type]
  ,cast(Sum(FullyReceiving) as varchar) as FullyReceiving
  ,cast(Sum(FullyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentFully
  ,cast(sum(PartiallyReceiving) as varchar) as PartiallyReceiving
  ,Cast(Sum(PartiallyReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentPartially
  ,cast(sum(NotReceiving)as varchar) as NotReceiving
  ,cast(Sum(NotReceiving)*1.0/nullif(Count(studentid),0) as varchar) as PercentNot
  from
  (
  Select 
    a.studentid
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

Execute (@SQL)

Declare @OutputSQL Varchar(Max)=
'Select * 
from ##PSSuperintendent
Order by
case when [SuperIntendent]=''Total'' then
''zzzzz''
End
,Superintendent
,[Primary Program Type]
,[School District]'

Execute (@OutputSQL)

Print(@OutputSQL)

End Try

Begin Catch

Select Error_Message() as ErrMessage;

End Catch

Set NoCount Off

End
GO


