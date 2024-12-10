USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPDWH_RelatedServiceMERGE]    Script Date: 12/9/2024 9:22:26 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO







-- =============================================
-- Author:		Phani Marupaka
-- Create date: 04-06-2018
-- Description:	Insert and Update Related Services data in DWH_ReltedServices table
-- =============================================

CREATE Procedure [dbo].[USPDWH_RelatedServiceMERGE]

AS 
BEGIN TRAN;

MERGE DWH_RelatedServices WITH (HOLDLOCK) AS RS

USING   Staging.DWH_RelatedServices AS SRS

ON (SRS.StudentID=RS.StudentID AND SRS.DocumentIDT=RS.DocumentIDT AND SRS.ChildDocProfileIDT=RS.ChildDocProfileIDT) 

WHEN MATCHED THEN 

UPDATE SET 

RS.ProfileIDT = SRS.ProfileIDT,
RS.ParentDocumentIDT = SRS.ParentDocumentIDT,
RS.ChildDocProfileIDX = SRS.ChildDocProfileIDX,
RS.Deleted = SRS.Deleted,
RS.show12monthService = SRS.show12monthService,
RS.IsTwelveMonthProgram = SRS.IsTwelveMonthProgram,
RS.DateIEP = SRS.DateIEP,
RS.DocumentCreatedOn = SRS.DocumentCreatedOn,
RS.DocumentModifiedOn = SRS.DocumentModifiedOn,
RS.OModifiedOn = SRS.OModifiedOn,
RS.RSModifiedOn = SRS.RSModifiedOn,
RS.Updated = SRS.Updated,
RS.DocumentFinalizedOn = SRS.DocumentFinalizedOn,
RS.DocStatus = SRS.DocStatus,
RS.DocHistoryYear = SRS.DocHistoryYear,
RS.PlanType = SRS.PlanType,
RS.Language = SRS.Language,
RS.LanguageDESC = SRS.LanguageDESC,
RS.Service = SRS.Service,
RS.ServiceName = SRS.ServiceName,
RS.ServiceDescription = SRS.ServiceDescription,
RS.ConsolidatedService = SRS.ConsolidatedService,
RS.ServiceOther = NULLIF(SRS.ServiceOther,''),
RS.ConsolidatedServiceOther = NULLIF(SRS.ConsolidatedServiceOther,''),
RS.NurseGroup = SRS.NurseGroup,
RS.NurseGroupDescription = SRS.NurseGroupDescription,
RS.NurseDeliveryTxt = NULLIF(SRS.NurseDeliveryTxt,''),
RS.GroupTxt = NULLIF(SRS.GroupTxt,''),
RS.Groups = SRS.Groups,
RS.GroupsDescription = SRS.GroupsDescription,
RS.GroupOtherSize = SRS.GroupOtherSize,
RS.GroupOtherSizeDescription = SRS.GroupOtherSizeDescription,
RS.ConsolidatedGroup = SRS.ConsolidatedGroup,
RS.ConsolidatedGroupOther = SRS.ConsolidatedGroupOther,
RS.TimesPerWk = SRS.TimesPerWk,
RS.TimesPerWkDescription = SRS.TimesPerWkDescription,
RS.CounselingOtherFrequencyTxt = SRS.CounselingOtherFrequencyTxt,
RS.CounselingOtherFrequency = SRS.CounselingOtherFrequency,
RS.CounselingOtherFreqDESC = SRS.CounselingOtherFreqDESC,
RS.CounselingFreqNotReq = SRS.CounselingFreqNotReq,
RS.CounselingFreqNotDESC = SRS.CounselingFreqNotDESC,
RS.FrequencyAsNeed = SRS.FrequencyAsNeed,
RS.FrequencyAsNeedDESC = SRS.FrequencyAsNeedDESC,
RS.FrequencyNurse = SRS.FrequencyNurse,
RS.FrequencyNurseDESC = SRS.FrequencyNurseDESC,
RS.TransOralSignFreqOther = NULLIF(SRS.TransOralSignFreqOther,''),
RS.PerWeekorMonths = SRS.PerWeekorMonths,
RS.PerWeekMonthNotReq = SRS.PerWeekMonthNotReq,
RS.PerWeekorMonth = SRS.PerWeekorMonth,
RS.OtherFrequencyRS = NULLIF(SRS.OtherFrequencyRS,''),
RS.FrequencyTxt = NULLIF(SRS.FrequencyTxt,''),
RS.TimesPer = SRS.TimesPer,
RS.ConsolidatedFrequency = SRS.ConsolidatedFrequency,
RS.ConsolidatedFrequencyOther = SRS.ConsolidatedFrequencyOther,
RS.DurationMins = SRS.DurationMins,
RS.DurationTxt = NULLIF(SRS.DurationTxt,''),
RS.DurationMinsText = NULLIF(SRS.DurationMinsText,''),
RS.DurationNurse = SRS.DurationNurse,
RS.DurationNurseDESC = SRS.DurationNurseDESC,
RS.DurationAsNeeded = SRS.DurationAsNeeded,
RS.DurationAsNeededDESC = SRS.DurationAsNeededDESC,
RS.TransOralSignDurationOther = NULLIF(SRS.TransOralSignDurationOther,''),
RS.CounslDurationMin = SRS.CounslDurationMin,
RS.ConsolidatedDuration = SRS.ConsolidatedDuration,
RS.ConsolidatedDurationOther = SRS.ConsolidatedDurationOther,
RS.RelatedServiceLocation = SRS.RelatedServiceLocation,
RS.RSLocationDESC = SRS.RSLocationDESC,
RS.LocationOtherTxt = NULLIF(SRS.LocationOtherTxt,''),
RS.LocationTxt = NULLIF(SRS.LocationTxt,''),
RS.LocationNotRequired = NULLIF(SRS.LocationNotRequired,''),
RS.CounselingLocationNotReq = SRS.CounselingLocationNotReq,
RS.CounselingLocationDESC = SRS.CounselingLocationDESC,
RS.ConsolidatedLocation = SRS.ConsolidatedLocation,
RS.ConsolidatedLocationOther = SRS.ConsolidatedLocationOther,
RS.GroupSize = SRS.GroupSize,
RS.AddlParaText = NULLIF(SRS.AddlParaText,''),  
RS.Is12MonthNoView = SRS.Is12MonthNoView,  
RS.Is12MonthRequired = SRS.Is12MonthRequired, 
RS.Is12MonthYesView = SRS.Is12MonthYesView,  
RS.IsVisuallyImpaired = SRS.IsVisuallyImpaired,  
RS.NeedAddlPara = SRS.NeedAddlPara,  
RS.ParaSixToOneText = NULLIF(SRS.ParaSixToOneText,''),  
RS.ReasonForRecommendPlacement12 = NULLIF(SRS.ReasonForRecommendPlacement12,''),  
RS.ReasonForRecomPlaceOtherTxt12 = NULLIF(SRS.ReasonForRecomPlaceOtherTxt12,''),  
RS.ReasonsPreKRequireServ = NULLIF(SRS.ReasonsPreKRequireServ,''),  
RS.SameService = SRS.SameService, 
RS.SevereLoss = SRS.SevereLoss, 
RS.TwelveMonthJustify = NULLIF(SRS.TwelveMonthJustify,''),
RS.StartDate = SRS.StartDate,
RS.EndDate = SRS.EndDate,
RS.IsDelete=0,
RS.ProcessedDate = SRS.ProcessedDate

WHEN NOT MATCHED THEN

 INSERT (StudentID,
ProfileIDT,
DocumentIDT,
ParentDocumentIDT,
ChildDocProfileIDT,
ChildDocProfileIDX,
Deleted,
show12monthService,
IsTwelveMonthProgram,
DateIEP,
DocumentCreatedOn,
DocumentModifiedOn,
OModifiedOn,
RSModifiedOn,
Updated,
DocumentFinalizedOn,
DocStatus,
DocHistoryYear,
PlanType,
Language,
LanguageDESC,
Service,
ServiceName,
ServiceDescription,
ConsolidatedService,
ServiceOther,
ConsolidatedServiceOther,
NurseGroup,
NurseGroupDescription,
NurseDeliveryTxt,
GroupTxt,
Groups,
GroupsDescription,
GroupOtherSize,
GroupOtherSizeDescription,
ConsolidatedGroup,
ConsolidatedGroupOther,
TimesPerWk,
TimesPerWkDescription,
CounselingOtherFrequencyTxt,
CounselingOtherFrequency,
CounselingOtherFreqDESC,
CounselingFreqNotReq,
CounselingFreqNotDESC,
FrequencyAsNeed,
FrequencyAsNeedDESC,
FrequencyNurse,
FrequencyNurseDESC,
TransOralSignFreqOther,
PerWeekorMonths,
PerWeekMonthNotReq,
PerWeekorMonth,
OtherFrequencyRS,
FrequencyTxt,
TimesPer,
ConsolidatedFrequency,
ConsolidatedFrequencyOther,
DurationMins,
DurationTxt,
DurationMinsText,
DurationNurse,
DurationNurseDESC,
DurationAsNeeded,
DurationAsNeededDESC,
TransOralSignDurationOther,
CounslDurationMin,
ConsolidatedDuration,
ConsolidatedDurationOther,
RelatedServiceLocation,
RSLocationDESC,
LocationOtherTxt,
LocationTxt,
LocationNotRequired,
CounselingLocationNotReq,
CounselingLocationDESC,
ConsolidatedLocation,
ConsolidatedLocationOther,
GroupSize,
AddlParaText,  
Is12MonthNoView,  
Is12MonthRequired, 
Is12MonthYesView,  
IsVisuallyImpaired,  
NeedAddlPara,  
ParaSixToOneText,  
ReasonForRecommendPlacement12,  
ReasonForRecomPlaceOtherTxt12,  
ReasonsPreKRequireServ,  
SameService, 
SevereLoss, 
TwelveMonthJustify,
StartDate,
EndDate)

VALUES (SRS.StudentID,
SRS.ProfileIDT,
SRS.DocumentIDT,
SRS.ParentDocumentIDT,
SRS.ChildDocProfileIDT,
SRS.ChildDocProfileIDX,
SRS.Deleted,
SRS.show12monthService,
SRS.IsTwelveMonthProgram,
SRS.DateIEP,
SRS.DocumentCreatedOn,
SRS.DocumentModifiedOn,
SRS.OModifiedOn,
SRS.RSModifiedOn,
SRS.Updated,
SRS.DocumentFinalizedOn,
SRS.DocStatus,
SRS.DocHistoryYear,
SRS.PlanType,
SRS.Language,
SRS.LanguageDESC,
SRS.Service,
SRS.ServiceName,
SRS.ServiceDescription,
SRS.ConsolidatedService,
NULLIF(SRS.ServiceOther,''),
NULLIF(SRS.ConsolidatedServiceOther,''),
SRS.NurseGroup,
SRS.NurseGroupDescription,
NULLIF(SRS.NurseDeliveryTxt,''),
NULLIF(SRS.GroupTxt,''),
SRS.Groups,
SRS.GroupsDescription,
SRS.GroupOtherSize,
SRS.GroupOtherSizeDescription,
SRS.ConsolidatedGroup,
SRS.ConsolidatedGroupOther,
SRS.TimesPerWk,
SRS.TimesPerWkDescription,
SRS.CounselingOtherFrequencyTxt,
SRS.CounselingOtherFrequency,
SRS.CounselingOtherFreqDESC,
SRS.CounselingFreqNotReq,
SRS.CounselingFreqNotDESC,
SRS.FrequencyAsNeed,
SRS.FrequencyAsNeedDESC,
SRS.FrequencyNurse,
SRS.FrequencyNurseDESC,
NULLIF(SRS.TransOralSignFreqOther,''),
SRS.PerWeekorMonths,
SRS.PerWeekMonthNotReq,
SRS.PerWeekorMonth,
NULLIF(SRS.OtherFrequencyRS,''),
NULLIF(SRS.FrequencyTxt,''),
SRS.TimesPer,
SRS.ConsolidatedFrequency,
SRS.ConsolidatedFrequencyOther,
SRS.DurationMins,
NULLIF(SRS.DurationTxt,''),
NULLIF(SRS.DurationMinsText,''),
SRS.DurationNurse,
SRS.DurationNurseDESC,
SRS.DurationAsNeeded,
SRS.DurationAsNeededDESC,
NULLIF(SRS.TransOralSignDurationOther,''),
SRS.CounslDurationMin,
SRS.ConsolidatedDuration,
SRS.ConsolidatedDurationOther,
SRS.RelatedServiceLocation,
SRS.RSLocationDESC,
NULLIF(SRS.LocationOtherTxt,''),
NULLIF(SRS.LocationTxt,''),
NULLIF(SRS.LocationNotRequired,''),
SRS.CounselingLocationNotReq,
SRS.CounselingLocationDESC,
SRS.ConsolidatedLocation,
SRS.ConsolidatedLocationOther,
SRS.GroupSize,
NULLIF(SRS.AddlParaText,''),  
SRS.Is12MonthNoView,  
SRS.Is12MonthRequired, 
SRS.Is12MonthYesView,  
SRS.IsVisuallyImpaired,  
SRS.NeedAddlPara,  
NULLIF(SRS.ParaSixToOneText,''),  
SRS.ReasonForRecommendPlacement12,  
NULLIF(SRS.ReasonForRecomPlaceOtherTxt12,''),  
NULLIF(SRS.ReasonsPreKRequireServ,''),  
SRS.SameService, 
SRS.SevereLoss, 
SRS.TwelveMonthJustify,
SRS.StartDate,
SRS.EndDate
);


COMMIT TRAN;


BEGIN TRAN 
UPDATE RS
SET RS.OutcomeDate = CONVERT(DATE,O.OutcomeDate,101),
RS.OutcomeSchoolYear = O.OutcomeSchoolYear
FROM DWH_RelatedServices RS
INNER JOIN DWH_Outcome O
    ON O.StudentID=RS.StudentID and RS.DocumentIDT=O.DocumentIDT
and PlanType=OutcomeTypeDesc
COMMIT TRAN;

BEGIN TRAN 
UPDATE DWH_RelatedServices
SET ServiceSchoolYear=[dbo].[fn_SY] (StartDate)
COMMIT TRAN;

BEGIN TRAN 
  UPDATE  RS  SET  IsDelete=1
  FROM DWH_RelatedServices RS
  WHERE NOT EXISTS (select  StudentID,DocumentIDT,ChildDocProfileIDT from Staging.DWH_RelatedServices SRS where
  RS.StudentID = SRS.StudentID and RS.DocumentIDT = SRS.DocumentIDT and RS.ChildDocProfileIDT=SRS.ChildDocProfileIDT)
  COMMIT TRAN;


BEGIN TRAN 
  UPDATE DWH_RelatedServices SET  ConsolidatedSDR = CASE WHEN ConsolidatedGroup='Other' and LanguageDESC is NULL THEN ConsolidatedGroupOther
WHEN ConsolidatedGroup='Other' and LanguageDESC is not NULL THEN RTRIM(LTRIM(ConsolidatedGroupOther)) +' Language of Service: '+LanguageDESC
WHEN ConsolidatedGroup not in ('Other') and LanguageDESC is not NULL  THEN ConsolidatedGroup+' Language of Service: '+LanguageDESC
ELSE ConsolidatedGroup
  END
 COMMIT TRAN;


 


GO


