USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPINT_RelatedServices]    Script Date: 12/9/2024 9:20:38 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO






CREATE PROCEDURE [dbo].[USPINT_RelatedServices]

AS

BEGIN

SET XACT_ABORT ON;
SET NOCOUNT ON;

/**************************************************************************************************************************************************
Object Name: USP_INTRelatedServices
Purpose: Populate Related Services data in SEO_MART database
Date Created: 06/16/2020

Modification Details:

Author					ModifiedDate		Comments
Phani Marupaka          09/24/2020		   Add columns RSMandateLanguageCode,ServiceTypeCode
Phani Marupaka			06/24/2021			Rename DocumentCreatedDate to DocumentCreatedDateTime,  DocumentModifiedDate to DocumentModifiedDateTime, 
                                            DocumentFinalizedDate to DocumentFinalizedDateTime.

Phani Marupaka          06/24/2021          Add DocumentCreatedDate, DocumentModifiedDate and DocumentFinalizedDate  columns.		
***************************************************************************************************************************************************/



    Declare @Today Datetime, @SchoolStartDate Date, @SchoolStartDateCalc Date,@SchoolYear Varchar(10), @Month Int,@COUNT INT
    Set @Today = GETDATE()
    Set @SchoolYear = (SELECT CAST((SchoolYear-1) AS VARCHAR(4))+'-'+CAST(SchoolYear AS VARCHAR(4)) SchoolYear FROM (
					SELECT  CASE WHEN SUBSTRING(replace(convert(varchar, getdate(),101),'/','') ,1,4)<'0715' THEN Year(getdate())
						ELSE Year(getdate())+1 END AS SchoolYear) A)
    Set @Month = 9
	
    Set @SchoolStartDate =  (Select Min(CalendarDate) from DWH_SchoolCalendar with(nolock)
                                Where IsInSession = 1 and SchoolYear = @SchoolYear and Month(CalendarDate) >= @Month)
								             
    Set @SchoolStartDateCalc = Case    when @Today < = @SchoolStartDate then @SchoolStartDate
                                    when @Today > @SchoolStartDate     then @Today
                                End
	Set @COUNT=(Select Count(*) from dbo.INT_RelatedServices WITH (NoLock))


IF (@COUNT<>0) 

BEGIN

TRUNCATE TABLE dbo.INT_RelatedServices

END;

BEGIN

INSERT INTO dbo.INT_RelatedServices 

(StudentID,
ProfileIDT,
OutcomeDocumentIDT,
InactiveDate,
OutcomeDocumentType,
DocumentCreatedDateTime,
DocumentModifiedDateTime,
DocumentFinalizedDateTime,
RSMandateLanguageCode,
RSMandateLanguage,
IsTwelveMonthProgram,
Is12MonthYesView,
SameService,
RecommendedGroupSize,
ServiceTypeCode,
ServiceType,
ServiceTypeOtherText,
RecommendedGroupType,
RecommendedGroupTypeOtherText,
RecommendedFrequency,
RecommendedFrequencyOtherText,
RecommendedDuration,
RecommendedDurationOtherText,
RecommendedLocation,
RecommendedLocationType,
RecommendedLocationOtherText,
RecommendedStartDate,
RecommendedEndDate,
SchoolYear,
EffectiveOutcomeDate,
AuthorizationPDate,
IntentNoticeReceivedDate,
PriorNoticePDate,
RecentAuthorizationDate,
GroupsCode,
GroupsDescription,
GroupType,
RecommendedGroupSizeNumeric,
RecommendedDurationNumeric,
RecommendedFrequencyNumeric,
MatchKey,
MatchKeyNL,
SummerServiceFlag,
ActiveServiceFlag,
ActiveDocumentFlag,
MatchKeyDuration,
MatchKeyLocation,
MatchKeyFull,
DocumentCreatedDate,
DocumentModifiedDate,
DocumentFinalizedDate)



SELECT StudentID,
ProfileIDT,
OutcomeDocumentIDT,
InactiveDate,
OutcomeDocumentType,
DocumentCreatedDateTime,
DocumentModifiedDateTime,
DocumentFinalizedDateTime,
RSMandateLanguageCode,
Language,
IsTwelveMonthProgram,
Is12MonthYesView,
SameService,
RecommendedGroupSize,
ServiceTypeCode,
ServiceType,
ServiceTypeOtherText,
RecommendedGroupType,
RecommendedGroupTypeOtherText,
RecommendedFrequency,
RecommendedFrequencyOtherText,
RecommendedDuration,
RecommendedDurationOtherText,
RecommendedLocation,
RecommendedLocationType,
RecommendedLocationOtherText,
RecommendedStartDate,
RecommendedEndDate,
SchoolYear,
EffectiveOutcomeDate,
AuthorizationPDate,
IntentNoticeReceivedDate,
PriorNoticePDate,
RecentAuthorizationDate,
GroupsCode,
GroupsDescription,
GroupType,
ISNULL(RecommendedGroupSizeNumeric,0) RecommendedGroupSizeNumeric,
ISNULL(RecommendedDurationNumeric,0) RecommendedDurationNumeric,
ISNULL(RecommendedFrequencyNumeric,0) RecommendedFrequencyNumeric,
CAST(StudentId as Varchar(10)) + ' ' +isnull(ServiceType,'') + ' ' + GroupType+ ' ' +Language AS MatchKey,
CAST(StudentId as Varchar(10)) + ' ' +isnull(ServiceType,'') + ' ' + GroupType as MatchKeyNL,
CASE WHEN Is12MonthYesView=1 and SameService=0 and IsTwelveMonthProgram=1 THEN 'Y' WHEN Is12MonthYesView=1 
and SameService=1 THEN 'Y' WHEN Is12MonthYesView=1 and SameService is null THEN 'Y' ELSE 'N' END AS SummerServiceFlag,
CASE WHEN RecommendedStartDate<=@SchoolStartDateCalc and (RecommendedEndDate is null or RecommendedEndDate>@SchoolStartDateCalc) 
and (IsTwelveMonthProgram is Null or IsTwelveMonthProgram<>1) THEN 'Y' ELSE 'N' END AS ActiveServiceFlag,
CASE WHEN DocumentIDT is not null and InactiveDate is null and IEPLatestOutcomeFlag='Y' THEN 'Y' ELSE 'N' END AS ActiveDocumentFlag,
CAST(StudentId as Varchar(10)) + ' ' +isnull(ServiceType,'') + ' ' + GroupType+ ' ' +Language+ ' ' +CAST(ISNULL(RecommendedDurationNumeric,0) as Varchar(5)) AS MatchKeyDuration,
CAST(StudentId as Varchar(10)) + ' ' +isnull(ServiceType,'') + ' ' + GroupType+ ' ' +Language+ ' ' + RecommendedLocationType AS MatchKeyLocation,
CAST(StudentId as Varchar(10)) + ' ' +isnull(ServiceType,'') + ' ' + GroupType+ ' ' +Language+ ' ' + RecommendedLocationType+ ' ' +CAST(ISNULL(RecommendedDurationNumeric,0) as Varchar(5)) AS MatchKeyFull,
DocumentCreatedDate,
DocumentModifiedDate,
DocumentFinalizedDate

FROM (
SELECT 
D.StudentID,
D.ProfileIDT,
D.DocumentIDT OutcomeDocumentIDT,
R.InactiveDate,
D.PlanType OutcomeDocumentType,
D.DocumentCreatedOn DocumentCreatedDateTime,
D.DocumentModifiedOn DocumentModifiedDateTime,
D.DocumentFinalizedOn DocumentFinalizedDateTime,
D.Language RSMandateLanguageCode,
CASE WHEN D.LanguageDESC IS NULL THEN 'English' WHEN D.LanguageDESC in ('French-Haitian Creole','Haitian-Creole') THEN 'Haitian Creole' ELSE D.LanguageDESC END AS Language,
D.IsTwelveMonthProgram,
D.Is12MonthYesView,
D.SameService,
CASE WHEN D.Groups=1 THEN 1 WHEN D.Groups=2 THEN 8 WHEN  D.Groups=3  THEN D.GroupOtherSizeDescription END AS  RecommendedGroupSize,
--CASE WHEN D.GroupSize is not null AND  ISNUMERIC(D.GroupSize)=0 THEN D.GroupSize ELSE NULL END AS RecommendedGroupSizeText,
D.Service ServiceTypeCode,
D.ConsolidatedService ServiceType,
D.ConsolidatedServiceOther ServiceTypeOtherText,
 CASE WHEN D.ConsolidatedGroup='Individual service' THEN 'Individual' 
  WHEN D.ConsolidatedGroup='Other service' THEN 'Other'
  ELSE D.ConsolidatedGroup END AS  RecommendedGroupType,
D.ConsolidatedGroupOther RecommendedGroupTypeOtherText,
D.ConsolidatedFrequency RecommendedFrequency,
D.ConsolidatedFrequencyOther RecommendedFrequencyOtherText,
D.ConsolidatedDuration RecommendedDuration,
NULLIF(D.ConsolidatedDurationOther,'') RecommendedDurationOtherText,
D.ConsolidatedLocation RecommendedLocation,
CASE WHEN  ConsolidatedLocation in ('Separate Location','Other') THEN 'Separate Location' 
WHEN  ConsolidatedLocation in ('Special Education Classroom','General Education Classroom') THEN 'Classroom' END AS
RecommendedLocationType,
NULLIF(D.ConsolidatedLocationOther,'') RecommendedLocationOtherText,
D.StartDate RecommendedStartDate,
D.EndDate RecommendedEndDate,
D.OutcomeSchoolYear SchoolYear,
D.OutcomeDate EffectiveOutcomeDate,
R.AuthorizationPDate,
R.IntentNoticeReceivedDate,
R.PriorNoticePDate,
R.RecentAuthorizationDate,
D.Groups GroupsCode,
D.GroupsDescription GroupsDescription,

CASE WHEN D.GroupsDescription = 'Group' THEN GroupsDescription
     WHEN D.GroupsDescription = 'Individual' THEN GroupsDescription
     WHEN GroupSize in ('2','3','4','5','6','7') THEN 'Group'
	 WHEN D.PlanType in ('IESP','SP') and D.Service in (17,18,20) THEN 'Individual'
   ELSE NULL END as GroupType,

CASE WHEN D.Groups=1 THEN 1 WHEN D.Groups=2 THEN 8 WHEN  D.Groups=3  THEN D.GroupOtherSizeDescription END AS RecommendedGroupSizeNumeric,

CASE WHEN D.ConsolidatedDuration IS NOT NULL  and ISNUMERIC(LEFT(D.ConsolidatedDuration,CHARINDEX(' ',D.ConsolidatedDuration)-0))=1
THEN  CAST(LEFT(D.ConsolidatedDuration,CHARINDEX(' ',D.ConsolidatedDuration)-0) as INT) END  AS RecommendedDurationNumeric,

CASE WHEN D.ConsolidatedFrequency IS NOT NULL and ISNUMERIC(LEFT(D.ConsolidatedFrequency,CHARINDEX(' ',D.ConsolidatedFrequency)-0))=1 
THEN CAST(LEFT(D.ConsolidatedFrequency,CHARINDEX(' ',D.ConsolidatedFrequency)-0) as INT) END AS RecommendedFrequencyNumeric,
R.OutcomeDocumentIDT DocumentIDT,
R.IEPLatestOutcomeFlag,
CAST(D.DocumentCreatedOn as DATE) DocumentCreatedDate,
CAST(D.DocumentModifiedOn as DATE) DocumentModifiedDate,
CAST(D.DocumentFinalizedOn as DATE) DocumentFinalizedDate


From dbo.DWH_RelatedServices D WITH(NOLOCK)
LEFT JOIN dbo.RPT_SESISActiveIEP R WITH(NOLOCK) ON R.StudentID=D.StudentID and R.OutcomeDocumentIDT=D.DocumentIDT and R.OutcomeDocumentType=D.PlanType
WHERE  D.DocStatus=3 and D.Deleted=0 and IsDelete=0 )DWH

END

END;







GO


