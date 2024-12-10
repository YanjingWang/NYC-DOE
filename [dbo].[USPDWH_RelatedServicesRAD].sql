USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPDWH_RelatedServicesRAD]    Script Date: 12/9/2024 9:21:09 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO






CREATE PROCEDURE [dbo].[USPDWH_RelatedServicesRAD]

AS

Set XAct_Abort On
Set NoCount On


/**************************************************************************************************************************************************
Object Name: USP_DWHRelatedServicesRAD
Purpose: Populate  Related Services Program Adaptations Document (PAD) Services data in DWH_RelatedServicesRAD table.
Date Created: 09/28/2020  

Modification Details:

Author					ModifiedDate		Comments
Phani Marupaka			06022021			Add SchoolYear column and populated based on DocHistoryYear
***************************************************************************************************************************************************/

BEGIN

If Object_id('tempdb..#DWHRSRAD') is not null
 Drop Table #DWHRSRAD

 
SELECT  
CAST(R.ID as INT) StudentID,
R.ProfileIDT# ProfileIDT,
R.DocumentIDT# DocumentIDT,
R.DocStatus DocStatus,
ParentDocumentIDT# ParentDocumentIDT,
ChildDocProfileIDT# ChildDocProfileIDT,
ChildDocProfileIDX# ChildDocProfileIDX,
UN.ModifiedOn# ModifiedOn,
OrigChildDocProfileIDT# OrigChildDocProfileIDT,
PlanType,
TempSrcIDT# TempSrcIDT,
CounslDurationMin,
DurationAsNeeded,
ND1.Description  DurationAsNeededDESC,
DurationMins,
NULLIF(DurationMinsText,'') DurationMinsText,
DurationNurse,
ND4.Description DurationNurseDESC,
NULLIF(DurationTxt,'') DurationTxt,
FrequencyAsNeed,
ND1.Description FrequencyAsNeedDESC,
FrequencyNurse,
ND3.Description FrequencyNurseDESC,
NULLIF(FrequencyTxt,'')  FrequencyTxt,
GroupOtherSize,
DRO.Description GroupOtherSizeDescription,
Groups,
GI.Description GroupsDESC,
NULLIF(GroupTxt,'')  GroupTxt,
IsTwelveMonthProgram,
Language,
LG.Description LanguageDESC,
NULLIF(LocationNotRequired,'') LocationNotRequired,
NULLIF(LocationOtherTxt,'') LocationOtherTxt,
NULLIF(LocationTxt,'') LocationTxt,
NULLIF(NurseDeliveryTxt,'') NurseDeliveryTxt,
NurseGroup,
NGI.Description NurseGroupDESC,
NULLIF(OtherFrequencyRS,'') OtherFrequencyRS,
PerWeekMonthNotReq,
PWM5.Description as PerWeekMonthNotReqDESC,
PerWeekorMonths,
PWM.Description as TimesPer,
RelatedServiceLocation,
PL.Description RSLocationDESC,
SelectedService,
Service,
STT.Description ServiceDescription,
NULLIF(ServiceOther,'')
SourceChildDocProfileIDT,
TimesPerWk,
OTF.Description TimesPerWkDESC,
NULLIF(TransOralSignDurationOther,'') TransOralSignDurationOther,
NULLIF(TransOralSignFreqOther,'') TransOralSignFreqOther,
CounselingFreqNotReq,
OTF2.Description  CounselingFreqNotDESC,
CounselingLocationNotReq,
PL1.Description CounselingLocationNotReqDESC,
CounselingOtherFrequency,
PWM3.Description CounselingOtherFreqDESC,
NULLIF(CounselingOtherFrequencyTxt,'') CounselingOtherFrequencyTxt,
RSChildDocProfileIDT,
IsDurationModified,
IsFrequencyModified,
PADRSCounslDurationMin,
PADRSDurationAsNeeded,
PD1.Description PADRSDurationAsNeededDESC,
PADRSDurationMins,
NULLIF(PADRSDurationMinsText,'') PADRSDurationMinsText,
PADRSDurationNurse,
PD2.Description  PADRSDurationNurseDESC,
NULLIF(PADRSDurationTxt,'') PADRSDurationTxt,
PADRSFrequencyAsNeed,
PD3.Description PADRSFrequencyAsNeedDESC,
PADRSFrequencyNurse,
NULLIF(PADRSFrequencyTxt,'') PADRSFrequencyTxt,
PADRSGroups,
PGI.Description PADRSGroupsDESC,
PADRSLocation,
PPL.Description PADRSLocationDESC,
PADRSNurseGroup,
PGI1.Description PADRSNurseGroupDESC,
NULLIF(PADRSOtherFrequencyRS,'') PADRSOtherFrequencyRS,
PADRSPerWeekMonthNotReq,
PWM1.Description as  PADRSPerWeekMonthNotReqDESC,
PADRSPerWeekorMonths,
PWM2.Description as  PADRSPerWeekorMonthsDESC,
PADRSTimesPerWk,
OTF1.Description as PADRSTimesPerWkDESC,
NULLIF(PADRSTransOralSignDurationOther,'') PADRSTransOralSignDurationOther,
NULLIF(PADRSTransOralSignFreqOther,'') PADRSTransOralSignFreqOther,
PADRSCounselingFreqNotReq,
OTF3.Description as PADRSCounselingFreqNotReqDESC,
PADRSCounselingOtherFrequency,
PWM4.Description PADRSCounselingOtherFreqDESC,
NULLIF(PADRSCounselingOtherFrequencyTxt,'') PADRSCounselingOtherFrequencyTxt,

------------------------------- GROUP -------------------------------------------
---- IESP Group ----
CASE WHEN PlanType in ('IESP','SP') and Service in (1,3,4,5,6,7,8) THEN GI.Description+' service'
WHEN PlanType in ('IESP','SP') and Service in (17,18,20) THEN 'Individual'
---- IEP,CSP Groups ----
WHEN PlanType  in ('CSP','IEP') and Service in (8,21,22) THEN NGI.Description+' service'
  WHEN PlanType in ('CSP','IEP','IESP','SP') and Service in (11,16,24) THEN 'Other'
WHEN PlanType in ('CSP','IEP') and Service in (1,3,4,5,6,7,15,19,23) and Groups<>3 THEN GI.Description+' service'
WHEN PlanType in ('CSP','IEP')  and Service in (1,3,4,5,6,7,15,19,23) and Groups=3 THEN  'Group of ' +DRO.Keyword
WHEN PlanType  in ('CSP','IEP') and Service in (17,18,20) THEN GI.Description

END AS ConsolidatedGroup,

---- IESP Group other ----
CASE  WHEN PlanType in ('IESP','SP') and Service in (24) THEN GroupTxt
---- IEP,CSP Groups other ----
WHEN PlanType in ('CSP','IEP') and Service in (8,21,22) and NurseGroup=3 THEN NurseDeliveryTxt
  WHEN PlanType in ('CSP','IEP') and Service in (11,16,24) THEN GroupTxt
END AS ConsolidatedGroupOther,

--------------------------------- RAD GROUP -------------------------------------------
---- IESP,SP Group ----
CASE WHEN PlanType in ('IESP','SP') and Service in (1,3,4,5,6,7,8) THEN PGI.Description+' service'
WHEN PlanType in ('IESP','SP') and Service in (17,18,20) THEN 'Individual'
---- IEP,CSP Groups ----
WHEN PlanType  in ('CSP','IEP') and Service in (8,21,22) THEN PGI1.Description+' service'
  WHEN PlanType in ('CSP','IEP','IESP','SP') and Service in (11,16,24) THEN 'Other'
WHEN PlanType in ('CSP','IEP') and Service in (1,3,4,5,6,7,15,19,23) and PADRSGroups<>3 THEN PGI.Description+' service'
WHEN PlanType in ('CSP','IEP')  and Service in (1,3,4,5,6,7,15,19,23) and PADRSGroups=3 THEN  'Group of ' +DRO.Keyword
WHEN PlanType  in ('CSP','IEP') and Service in (17,18,20) THEN PGI.Description

END AS RADConsolidatedGroup,

---- IESP,SP Group other ----
CASE  WHEN PlanType in ('IESP','SP') and Service in (24) THEN GroupTxt
---- IEP,CSP Groups other ----
WHEN PlanType in ('CSP','IEP') and Service in (8,21,22) and PADRSNurseGroup=3 THEN NurseDeliveryTxt
  WHEN PlanType in ('CSP','IEP') and Service in (11,16,24) THEN GroupTxt
END AS RADConsolidatedGroupOther,

-------------------------------------------- FREQUENCY -----------------------------------------


---- IEP,CSP Frequency ----

CASE WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,15,19,20,23,25) and  TimesPerWk<>16 and PerWeekorMonths<>3 THEN OTF.Description+' time(s) per '+PWM.Description
WHEN PlanType in ('IEP','CSP') and Service in (17,18) and FrequencyAsNeed<>5 THEN ND2.Description
WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and FrequencyNurse<>5 THEN ND3.Description
WHEN PlanType in ('CSP','IEP') and Service in (11,16,24) THEN 'Other'

---- IESP Frequency other ----

WHEN PlanType in ('IESP','SP') and Service in (8,11,16,21,24) THEN 'Other'
WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,15,19,20,23,25) and  TimesPerWk<>16 and PerWeekorMonths<>3 THEN OTF.Description+' time(s) per '+PWM.Description
WHEN PlanType in ('IESP','SP') and Service in (17,18) and FrequencyAsNeed<>5 THEN ND2.Description
WHEN PlanType in ('IESP','SP') and Service in (1) and CounselingFreqNotReq<>16 THEN OTF2.Description+' time(s) per '+PWM3.Description
END AS ConsolidatedFrequency,

---- IEP,CSP Frequency other ----
CASE WHEN PlanType in ('IEP','CSP') and Service in (11,16,24) THEN Frequencytxt
       WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,15,19,20,23,25) and  TimesPerWk=16 THEN OtherFrequencyRS
       WHEN PlanType in ('IEP','CSP') and Service in (17,18) and FrequencyAsNeed=5 THEN TransOralSignFreqOther
       WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and FrequencyNurse=5 THEN OtherFrequencyRS

---- IESP Frequency other ----
WHEN PlanType in ('IESP','SP') and Service in (8,11,16,21,22,24) THEN Frequencytxt
WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,15,19,20,23,25) and  TimesPerWk=16 THEN OtherFrequencyRS
WHEN PlanType in ('IESP','SP') and Service in (17,18) and FrequencyAsNeed=5 THEN TransOralSignFreqOther
WHEN PlanType in ('IESP','SP') and Service in (1) and CounselingFreqNotReq=16 THEN CounselingOtherFrequencyTxt

END AS ConsolidatedFrequencyOther,


-------------------------------------------- RAD FREQUENCY -----------------------------------------


---- IEP,CSP Frequency ----

CASE WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,15,19,20,23,25) and  PADRSTimesPerWk<>16 and PADRSPerWeekorMonths<>3 THEN OTF1.Description+' time(s) per '+PWM2.Description
WHEN PlanType in ('IEP','CSP') and Service in (17,18) and PADRSFrequencyAsNeed<>5 THEN PD3.Description
WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and PADRSFrequencyNurse<>5 THEN PD4.Description
WHEN PlanType in ('CSP','IEP') and Service in (11,16,24) THEN 'Other'

---- IESP Frequency other ----

WHEN PlanType in ('IESP','SP') and Service in (8,11,16,21,24) THEN 'Other'
WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,15,19,20,23,25) and  PADRSTimesPerWk<>16 and PADRSPerWeekorMonths<>3 THEN OTF.Description+' time(s) per '+PWM2.Description
WHEN PlanType in ('IESP','SP') and Service in (17,18) and PADRSFrequencyAsNeed<>5 THEN PD3.Description
WHEN PlanType in ('IESP','SP') and Service in (1) and PADRSCounselingFreqNotReq<>16 THEN OTF3.Description+' time(s) per '+PWM4.Description
END AS RADConsolidatedFrequency,

---- IEP,CSP Frequency other ----
CASE WHEN PlanType in ('IEP','CSP') and Service in (11,16,24) THEN PADRSFrequencytxt
       WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,15,19,20,23,25) and  PADRSTimesPerWk=16 THEN PADRSOtherFrequencyRS
       WHEN PlanType in ('IEP','CSP') and Service in (17,18) and PADRSFrequencyAsNeed=5 THEN PADRSTransOralSignFreqOther
       WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and FrequencyNurse=5 THEN PADRSOtherFrequencyRS

---- IESP Frequency other ----
WHEN PlanType in ('IESP','SP') and Service in (8,11,16,21,22,24) THEN PADRSFrequencytxt
WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,15,19,20,23,25) and  TimesPerWk=16 THEN PADRSOtherFrequencyRS
WHEN PlanType in ('IESP','SP') and Service in (17,18) and PADRSFrequencyAsNeed=5 THEN PADRSTransOralSignFreqOther
WHEN PlanType in ('IESP','SP') and Service in (1) and PADRSCounselingFreqNotReq=16 THEN PADRSCounselingOtherFrequencyTxt

END AS RADConsolidatedFrequencyOther,



-------------------------------- DURATION ----------------------------------------------

---- IEP,CSP Duration  -----

CASE WHEN PlanType in ('IEP','CSP') and Service in (17,18) and LTRIM(RTRIM(DurationAsNeeded))<>5 THEN ND1.Description
WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and LTRIM(RTRIM(DurationNurse))<>5 THEN ND4.Description
WHEN PlanType in ('IEP','CSP') and Service in (3,4,5,6,7,19,20,23,15,25) THEN CONVERT(Varchar(20),DurationMins)+ ' minutes'
WHEN PlanType in ('IEP','CSP') and Service in (1) THEN CONVERT(Varchar(20),CounslDurationMin)+ ' minutes'
WHEN PlanType in ('CSP','IEP','IESP') and Service in (11,16,24) THEN 'Other'

---- IESP Duration  -----

WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,20,23,15,25) THEN CONVERT(Varchar(20),DurationMins)+ ' minutes'
WHEN PlanType in ('IESP','SP') and Service in (17,18) and LTRIM(RTRIM(DurationAsNeeded))<>5 THEN ND1.Description
WHEN PlanType in ('IESP','SP') and Service in (1) THEN CONVERT(Varchar(20),CounslDurationMin)+ ' minutes'


END AS ConsolidatedDuration,

---- IEP,CSP Duration other -----

CASE WHEN PlanType in ('IEP','CSP') and Service in (11,16,24) THEN DurationMinsText 
WHEN PlanType in ('IEP','CSP') and Service in (17,18) and DurationAsNeeded=5 THEN TransOralSignDurationOther
WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and LTRIM(RTRIM(DurationNurse))=5 THEN DurationTxt


---- IESP Duration other  -----
WHEN PlanType in ('IESP','SP') and Service in (8,11,16,21,22,24) THEN DurationMinsText 
WHEN PlanType in ('IESP','SP') and Service in (17,18) and DurationAsNeeded=5 THEN TransOralSignDurationOther
WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,20,23,15,25) THEN DurationMinsText

END AS ConsolidatedDurationOther,

-------------------------------- RAD DURATION ----------------------------------------------

---- IEP,CSP Duration  -----

CASE WHEN PlanType in ('IEP','CSP') and Service in (17,18) and LTRIM(RTRIM(PADRSDurationAsNeeded))<>5 THEN PD1.Description
WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and LTRIM(RTRIM(PADRSDurationNurse))<>5 THEN PD2.Description
WHEN PlanType in ('IEP','CSP') and Service in (3,4,5,6,7,19,20,23,15,25) THEN CONVERT(Varchar(20),PADRSDurationMins)+ ' minutes'
WHEN PlanType in ('IEP','CSP') and Service in (1) THEN CONVERT(Varchar(20),PADRSCounslDurationMin)+ ' minutes'
WHEN PlanType in ('CSP','IEP','IESP') and Service in (11,16,24) THEN 'Other'

---- IESP Duration  -----

WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,20,23,15,25) THEN CONVERT(Varchar(20),PADRSDurationMins)+ ' minutes'
WHEN PlanType in ('IESP','SP') and Service in (17,18) and LTRIM(RTRIM(PADRSDurationAsNeeded))<>5 THEN PD1.Description
WHEN PlanType in ('IESP','SP') and Service in (1) THEN CONVERT(Varchar(20),PADRSCounslDurationMin)+ ' minutes'


END AS RADConsolidatedDuration,

---- IEP,CSP Duration other -----

CASE WHEN PlanType in ('IEP','CSP') and Service in (11,16,24) THEN PADRSDurationMinsText 
WHEN PlanType in ('IEP','CSP') and Service in (17,18) and PADRSDurationAsNeeded=5 THEN PADRSTransOralSignDurationOther
WHEN PlanType in ('IEP','CSP') and Service in (8,21,22) and LTRIM(RTRIM(PADRSDurationNurse))=5 THEN PADRSDurationTxt


---- IESP Duration other  -----
WHEN PlanType in ('IESP','SP') and Service in (8,11,16,21,22,24) THEN PADRSDurationMinsText 
WHEN PlanType in ('IESP','SP') and Service in (17,18) and PADRSDurationAsNeeded=5 THEN PADRSTransOralSignDurationOther
WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,20,23,15,25) THEN PADRSDurationMinsText

END AS RADConsolidatedDurationOther,


------------------------------------------ LOCATION -------------------------------------------


------ IEP, CSP Location  -------

CASE WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,19,23)  THEN PL.Description 
 WHEN PlanType in ('IEP','CSP') and Service in (8,11,16,17,18,21,22,24,20) THEN 'Other'


 ------ IESP Location  -------

WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,23,15,25)  THEN PL.Description 
 WHEN PlanType in ('IESP','SP') and Service in (8,11,16,17,18,21,22,24,20) THEN 'Other'
WHEN PlanType in ('IESP','SP') and Service in (1)  THEN  PL1.Description

END AS ConsolidatedLocation,


  ------ IEP, CSP Location Other -------

  CASE WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,19,23,15,25) and RelatedServiceLocation=13 THEN NULLIF(LocationOtherTxt,'')
  WHEN PlanType in ('IEP','CSP') and Service in (8,11,16,17,18,21,22,24) THEN NULLIF(LocationTxt,'')
  WHEN PlanType in ('IEP','CSP') and Service in (20) THEN LocationNotRequired
  WHEN PlanType in ('IESP','SP') and Service in (1) and CounselingLocationNotReq=13 THEN  NULLIF(LocationOtherTxt,'')


   ------ IESP Location Other -------

  WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,23,15,25) and RelatedServiceLocation=13 THEN NULLIF(LocationOtherTxt,'')
  WHEN PlanType in ('IESP','SP') and Service in (8,11,16,17,18,21,22,24) THEN NULLIF(LocationTxt,'')
  WHEN PlanType in ('IESP','SP') and Service in (20) THEN LocationNotRequired
  WHEN PlanType in ('IESP','SP') and Service in (1) and CounselingLocationNotReq=13 THEN  NULLIF(LocationTxt,'')

END AS ConsolidatedLocationOther,

------------------------------------------ RAD LOCATION -------------------------------------------


------ IEP, CSP Location  -------

CASE WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,19,23)  THEN PPL.Description 
 WHEN PlanType in ('IEP','CSP') and Service in (8,11,16,17,18,21,22,24,20) THEN 'Other'


 ------ IESP,SP Location  -------

WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,23,15,25)  THEN PPL.Description 
 WHEN PlanType in ('IESP','SP') and Service in (8,11,16,17,18,21,22,24,20) THEN 'Other'
WHEN PlanType in ('IESP','SP') and Service in (1)  THEN  PL1.Description

END AS RADConsolidatedLocation,


  ------ IEP, CSP Location Other -------

  CASE WHEN PlanType in ('IEP','CSP') and Service in (1,3,4,5,6,7,19,23,15,25) and PADRSLocation=13 THEN NULLIF(LocationOtherTxt,'')
  WHEN PlanType in ('IEP','CSP') and Service in (8,11,16,17,18,21,22,24) THEN NULLIF(LocationTxt,'')
  WHEN PlanType in ('IEP','CSP') and Service in (20) THEN LocationNotRequired
  WHEN PlanType in ('IESP','SP') and Service in (1) and PADRSCounselingFreqNotReq=13 THEN  NULLIF(LocationOtherTxt,'')


   ------ IESP Location Other -------

  WHEN PlanType in ('IESP','SP') and Service in (3,4,5,6,7,19,23,15,25) and PADRSLocation=13 THEN NULLIF(LocationOtherTxt,'')
  WHEN PlanType in ('IESP','SP') and Service in (8,11,16,17,18,21,22,24) THEN NULLIF(LocationTxt,'')
  WHEN PlanType in ('IESP','SP') and Service in (20) THEN LocationNotRequired
  WHEN PlanType in ('IESP','SP') and Service in (1) and PADRSCounselingFreqNotReq=13 THEN  NULLIF(LocationTxt,'')

END AS RADConsolidatedLocationOther,



 ------- GROUP SIZE ------

CASE WHEN Service in (1,3,4,5,6,7,15,19,23,17,18,20) and Groups=1 THEN '1'
WHEN Service in (1,3,4,5,6,7,15,19,23,17,18,20) and Groups=2 THEN '8'
  WHEN Service in (1,3,4,5,6,7,15,19,23,17,18,20) and Groups=3 THEN DRO.Keyword
   WHEN Service in (8,21,22) and NurseGroup=1 THEN '1'
   WHEN Service in (8,21,22) and NurseGroup=3 THEN NurseDeliveryTxt
  END as GroupSize,
R.SchoolYear,
0 IsDelete,
GETDATE() ProcessedDate INTO #DWHRSRAD

FROM (

--------- IEP RAD ---------------------
SELECT 
IEP.ParentDocumentIDT#,
IEP.ChildDocProfileIDT#,
IEP.ChildDocProfileIDX#,
IEP.ModifiedOn#,
IEP.OrigChildDocProfileIDT#,
'IEP' PlanType,
IEP.TempSrcIDT#,
IEP.CounslDurationMin,
IEP.DurationAsNeeded,
IEP.DurationMins,
IEP.DurationMinsText,
IEP.DurationNurse,
IEP.DurationTxt,
IEP.FrequencyAsNeed,
IEP.FrequencyNurse,
IEP.FrequencyTxt,
IEP.GroupOtherSize,
IEP.Groups,
IEP.GroupTxt,
IEP.IsTwelveMonthProgram,
IEP.Language,
IEP.LocationNotRequired,
IEP.LocationOtherTxt,
IEP.LocationTxt,
IEP.NurseDeliveryTxt,
IEP.NurseGroup,
IEP.OtherFrequencyRS,
IEP.PerWeekMonthNotReq,
IEP.PerWeekorMonths,
IEP.RelatedServiceLocation,
IEP.SelectedService,
IEP.Service,
IEP.ServiceOther,
IEP.SourceChildDocProfileIDT,
IEP.TimesPerWk,
IEP.TransOralSignDurationOther,
IEP.TransOralSignFreqOther,
NULL CounselingFreqNotReq,
NULL CounselingLocationNotReq,
NULL CounselingOtherFrequency,
CONVERT(VARCHAR,NULL) CounselingOtherFrequencyTxt,
UIEP.RSChildDocProfileIDT,
UIEP.IsDurationModified,
UIEP.IsFrequencyModified,
UIEP.PADRSCounslDurationMin,
UIEP.PADRSDurationAsNeeded,
UIEP.PADRSDurationMins,
UIEP.PADRSDurationMinsText,
UIEP.PADRSDurationNurse,
UIEP.PADRSDurationTxt,
UIEP.PADRSFrequencyAsNeed,
UIEP.PADRSFrequencyNurse,
UIEP.PADRSFrequencyTxt,
UIEP.PADRSGroups,
UIEP.PADRSLocation,
UIEP.PADRSNurseGroup,
UIEP.PADRSOtherFrequencyRS,
UIEP.PADRSPerWeekMonthNotReq,
UIEP.PADRSPerWeekorMonths,
UIEP.PADRSTimesPerWk,
UIEP.PADRSTransOralSignDurationOther,
UIEP.PADRSTransOralSignFreqOther,
NULL PADRSCounselingFreqNotReq,
NULL PADRSCounselingOtherFrequency,
CONVERT(VARCHAR,NULL) PADRSCounselingOtherFrequencyTxt
FROM (Select * from [NYCONFIG_Link_v16].[nyconfigSnapshot].dbo.Doc#PADRS#IEPService#Profiles  WITH(NOLOCK)  where SelectedService=1 )  IEP  
LEFT OUTER JOIN    (Select * from [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#IEPServUPD#Profiles]  WITH(NOLOCK)  where SelectedService=1)   UIEP ON 
UIEP.ParentDocumentIDT#=IEP.ParentDocumentIDT#  and IEP.Service=UIEP.Service and UIEP.RSChildDocProfileIDT=IEP.ChildDocProfileIDT#


UNION ALL

--------- IESP RAD ---------------------

SELECT 
IESP.ParentDocumentIDT#,
IESP.ChildDocProfileIDT#,
IESP.ChildDocProfileIDX#,
IESP.ModifiedOn#,
IESP.OrigChildDocProfileIDT#,
'IESP' PlanType,
IESP.TempSrcIDT#,
IESP.CounslDurationMin,
IESP.DurationAsNeeded,
IESP.DurationMins,
IESP.DurationMinsText,
NULL DurationNurse,
CONVERT(VARCHAR,NULL) DurationTxt,
IESP.FrequencyAsNeed,
NULL FrequencyNurse,
IESP.FrequencyTxt,
IESP.GroupOtherSize,
IESP.Groups,
IESP.GroupTxt,
NULL IsTwelveMonthProgram,
IESP.Language,
IESP.LocationNotRequired,
IESP.LocationOtherTxt,
IESP.LocationTxt,
IESP.NurseDeliveryTxt,
IESP.NurseGroup,
IESP.OtherFrequencyRS,
NULL PerWeekMonthNotReq,
IESP.PerWeekorMonths,
IESP.RelatedServiceLocation,
IESP.SelectedService,
IESP.Service,
IESP.ServiceOther,
IESP.SourceChildDocProfileIDT,
IESP.TimesPerWk,
IESP.TransOralSignDurationOther,
IESP.TransOralSignFreqOther,
IESP.CounselingFreqNotReq,
IESP.CounselingLocationNotReq,
IESP.CounselingOtherFrequency,
IESP.CounselingOtherFrequencyTxt,
UIESP.RSChildDocProfileIDT,
UIESP.IsDurationModified,
UIESP.IsFrequencyModified,
UIESP.PADRSCounslDurationMin,
UIESP.PADRSDurationAsNeeded,
UIESP.PADRSDurationMins,
UIESP.PADRSDurationMinsText,
NULL PADRSDurationNurse,
CONVERT(VARCHAR,NULL)PADRSDurationTxt,
UIESP.PADRSFrequencyAsNeed,
NULL PADRSFrequencyNurse,
UIESP.PADRSFrequencyTxt,
UIESP.PADRSGroups,
UIESP.PADRSLocation,
UIESP.PADRSNurseGroup,
UIESP.PADRSOtherFrequencyRS,
NULL PADRSPerWeekMonthNotReq,
UIESP.PADRSPerWeekorMonths,
UIESP.PADRSTimesPerWk,
UIESP.PADRSTransOralSignDurationOther,
UIESP.PADRSTransOralSignFreqOther,
UIESP.PADRSCounselingFreqNotReq,
UIESP.PADRSCounselingOtherFrequency,
UIESP.PADRSCounselingOtherFrequencyTxt


FROM (SELECT * FROM [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#IESPSrv#Profiles]  WITH(NOLOCK)  where SelectedService=1)  IESP
LEFT OUTER JOIN  ( Select * from [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#IESPRelSrv#Profiles]  WITH(NOLOCK)  where SelectedService=1)  UIESP ON
UIESP.ParentDocumentIDT#=IESP.ParentDocumentIDT#  and IESP.Service=UIESP.Service and UIESP.RSChildDocProfileIDT=IESP.ChildDocProfileIDT#



UNION ALL

--------- SP RAD ---------------------

SELECT 
SP.ParentDocumentIDT#,
SP.ChildDocProfileIDT#,
SP.ChildDocProfileIDX#,
SP.ModifiedOn#,
SP.OrigChildDocProfileIDT#,
'SP' PlanType,
SP.TempSrcIDT#,
SP.CounslDurationMin,
SP.DurationAsNeeded,
SP.DurationMins,
SP.DurationMinsText,
NULL DurationNurse,
CONVERT(VARCHAR,NULL) DurationTxt,
SP.FrequencyAsNeed,
NULL FrequencyNurse,
SP.FrequencyTxt,
NULL GroupOtherSize,
SP.Groups,
SP.GroupTxt,
NULL IsTwelveMonthProgram,
SP.Language,
SP.LocationNotRequired,
SP.LocationOtherTxt,
SP.LocationTxt,
CONVERT(VARCHAR,NULL) NurseDeliveryTxt,
SP.NurseGroup,
CONVERT(VARCHAR,NULL) OtherFrequencyRS,
NULL PerWeekMonthNotReq,
SP.PerWeekorMonths,
SP.RelatedServiceLocation,
SP.SelectedService,
SP.Service,
SP.ServiceOther,
SP.SourceChildDocProfileIDT,
SP.TimesPerWk,
NULL TransOralSignDurationOther,
NULL TransOralSignFreqOther,
SP.CounselingFreqNotReq,
SP.CounselingLocationNotReq,
SP.CounselingOtherFrequency,
CONVERT(VARCHAR,NULL) CounselingOtherFrequencyTxt,
USP.RSChildDocProfileIDT,
USP.IsDurationModified,
USP.IsFrequencyModified,
USP.PADRSCounslDurationMin,
USP.PADRSDurationAsNeeded,
USP.PADRSDurationMins,
USP.PADRSDurationMinsText,
NULL PADRSDurationNurse,
CONVERT(VARCHAR,NULL) PADRSDurationTxt,
USP.PADRSFrequencyAsNeed,
NULL PADRSFrequencyNurse,
USP.PADRSFrequencyTxt,
USP.PADRSGroups,
USP.PADRSLocation,
USP.PADRSNurseGroup,
NULL PADRSOtherFrequencyRS,
NULL PADRSPerWeekMonthNotReq,
USP.PADRSPerWeekorMonths,
USP.PADRSTimesPerWk,
NULL PADRSTransOralSignDurationOther,
NULL PADRSTransOralSignFreqOther,
USP.PADRSCounselingFreqNotReq,
USP.PADRSCounselingOtherFrequency,
CONVERT(VARCHAR,NULL) PADRSCounselingOtherFrequencyTxt

FROM (Select * from [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#SPReltServ#Profiles] WITH(NOLOCK) WHERE SelectedService=1) SP
LEFT OUTER JOIN (SELECT * FROM [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#SPServUpd#Profiles] WITH(NOLOCK) WHERE SelectedService=1) USP ON 
USP.ParentDocumentIDT#=SP.ParentDocumentIDT#  and SP.Service=USP.Service and USP.RSChildDocProfileIDT=SP.ChildDocProfileIDT#



UNION ALL

--------- CSP RAD ---------------------


SELECT 
CSP.ParentDocumentIDT#,
CSP.ChildDocProfileIDT#,
CSP.ChildDocProfileIDX#,
CSP.ModifiedOn#,
CSP.OrigChildDocProfileIDT#,
'CSP' PlanType,
CSP.TempSrcIDT#,
CSP.CounslDurationMin,
CSP.DurationAsNeeded,
CSP.DurationMins,
CSP.DurationMinsText,
CSP.DurationNurse,
CSP.DurationTxt,
CSP.FrequencyAsNeed,
CSP.FrequencyNurse,
CSP.FrequencyTxt,
CSP.GroupOtherSize,
CSP.Groups,
CSP.GroupTxt,
NULL IsTwelveMonthProgram,
CSP.Language,
CSP.LocationNotRequired,
CSP.LocationOtherTxt,
CSP.LocationTxt,
CSP.NurseDeliveryTxt,
CSP.NurseGroup,
CSP.OtherFrequencyRS,
CSP.PerWeekMonthNotReq,
CSP.PerWeekorMonths,
CSP.RelatedServiceLocation,
CSP.SelectedService,
CSP.Service,
CSP.ServiceOther,
CSP.SourceChildDocProfileIDT,
CSP.TimesPerWk,
CSP.TransOralSignDurationOther,
CSP.TransOralSignFreqOther,
NULL CounselingFreqNotReq,
NULL CounselingLocationNotReq,
NULL CounselingOtherFrequency,
CONVERT(VARCHAR,NULL)  CounselingOtherFrequencyTxt,
UCSP.RSChildDocProfileIDT,
UCSP.IsDurationModified,
UCSP.IsFrequencyModified,
UCSP.PADRSCounslDurationMin,
UCSP.PADRSDurationAsNeeded,
UCSP.PADRSDurationMins,
UCSP.PADRSDurationMinsText,
NULL PADRSDurationNurse,
UCSP.PADRSDurationTxt,
UCSP.PADRSFrequencyAsNeed,
UCSP.PADRSFrequencyNurse,
UCSP.PADRSFrequencyTxt,
UCSP.PADRSGroups,
UCSP.PADRSLocation,
UCSP.PADRSNurseGroup,
UCSP.PADRSOtherFrequencyRS,
UCSP.PADRSPerWeekMonthNotReq,
UCSP.PADRSPerWeekorMonths,
UCSP.PADRSTimesPerWk,
UCSP.PADRSTransOralSignDurationOther,
UCSP.PADRSTransOralSignFreqOther,
NULL PADRSCounselingFreqNotReq,
NULL PADRSCounselingOtherFrequency,
CONVERT(VARCHAR,NULL) PADRSCounselingOtherFrequencyTxt


FROM (SELECT * FROM  [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#RelServCSP#Profiles] WHERE SelectedService=1) CSP
LEFT OUTER JOIN 
(SELECT * FROM  [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].[DOC#PADRS#CSPServUpd#Profiles] WHERE  SelectedService=1) UCSP ON 
UCSP.ParentDocumentIDT#=CSP.ParentDocumentIDT#  and CSP.Service=UCSP.Service and UCSP.RSChildDocProfileIDT=CSP.ChildDocProfileIDT# ) UN 
INNER JOIN 
(SELECT CAST((DocHistoryYear) AS VARCHAR(4))+'-'+CAST(DocHistoryYear+1 AS VARCHAR(4)) SchoolYear,* FROM [NYCONFIG_Link_v16].[nyconfigSnapshot].dbo.Doc#PADRS#Profiles WITH(NOLOCK)) R  
 ON  R.DocumentIDT#=UN.ParentDocumentIDT# and R.Deleted#=0 
LEFT OUTER JOIN    (Select IDT#,Keyword,Description from  [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].ServiceTypeTable WITH (NOLOCK)) STT  on UN.Service=STT.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].Languages LG WITH (NOLOCK)  on  UN.Language=LG.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration ND1 WITH (NOLOCK) on UN.DurationAsNeeded=ND1.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration ND2 WITH (NOLOCK) on UN.FrequencyAsNeed=ND2.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration ND3 WITH (NOLOCK) on UN.FrequencyNurse=ND3.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration ND4 WITH (NOLOCK) on UN.DurationNurse=ND4.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].DelRecomOther DRO WITH (NOLOCK)  on UN.GroupOtherSize=DRO.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].IEPServiceGroupInd GI WITH (NOLOCK)  on  UN.Groups=GI.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].OneToFifteen OTF  WITH (NOLOCK)on UN.TimesPerWk=OTF.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].OneToFifteen OTF2 WITH (NOLOCK) on UN.CounselingFreqNotReq=OTF2.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].PerWeekorMonth PWM3 WITH (NOLOCK) on UN.CounselingOtherFrequency=PWM3.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].PerWeekorMonth PWM WITH (NOLOCK) on UN.PerWeekorMonths=PWM.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].PerWeekorMonth PWM5 WITH (NOLOCK) on UN.PerWeekMonthNotReq=PWM5.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].ProgramLocationTable PL WITH (NOLOCK) on UN.RelatedServiceLocation=PL.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].ProgramLocationTable PL1 WITH (NOLOCK) on UN.CounselingLocationNotReq=PL1.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].IEPServiceGroupInd NGI WITH (NOLOCK)  on UN.NurseGroup=NGI.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration PD1 WITH (NOLOCK) on UN.PADRSDurationAsNeeded=PD1.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration PD2 WITH (NOLOCK) on UN.PADRSDurationNurse=PD2.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration PD3 WITH (NOLOCK) on UN.PADRSFrequencyAsNeed=PD3.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].AsNeededDuration PD4 WITH (NOLOCK) on UN.PADRSFrequencyNurse=PD4.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].IEPServiceGroupInd PGI WITH (NOLOCK)  on  UN.PADRSGroups=PGI.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].ProgramLocationRemote  PPL WITH (NOLOCK) on UN.PADRSLocation=PPL.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].IEPServiceGroupInd PGI1 WITH (NOLOCK)  on  UN.PADRSNurseGroup=PGI1.IDT# 
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].PerWeekorMonth PWM1 WITH (NOLOCK) on UN.PADRSPerWeekMonthNotReq=PWM1.IDT# 
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].PerWeekorMonth PWM2 WITH (NOLOCK) on UN.PADRSPerWeekorMonths =PWM2.IDT# 
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].OneToFifteen OTF1  WITH (NOLOCK)on UN.PADRSTimesPerWk=OTF1.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].OneToFifteen OTF3 WITH (NOLOCK) on UN.PADRSCounselingFreqNotReq=OTF3.IDT#
LEFT OUTER JOIN    [NYCONFIG_Link_v16].[nyconfigSnapshot].[dbo].PerWeekorMonth PWM4 WITH (NOLOCK) on UN.PADRSCounselingOtherFrequency=PWM4.IDT#


END;




---- Merge Data in DWH_RelatedServicesRAD table -------

BEGIN TRAN;

MERGE DWH_RelatedServicesRAD WITH (HOLDLOCK) AS DWH

USING   #DWHRSRAD AS   RAD 

ON (DWH.StudentID = RAD.StudentID and RAD.DocumentIDT=DWH.DocumentIDT  and DWH.ChildDocProfileIDT=RAD.ChildDocProfileIDT ) 

WHEN MATCHED THEN 

UPDATE SET 
DWH.StudentID  =  RAD.StudentID,
DWH.ProfileIDT  =  RAD.ProfileIDT,
DWH.DocumentIDT  =  RAD.DocumentIDT,
DWH.DocStatus  =  RAD.DocStatus,
DWH.ParentDocumentIDT  =  RAD.ParentDocumentIDT,
DWH.ChildDocProfileIDT  =  RAD.ChildDocProfileIDT,
DWH.ChildDocProfileIDX  =  RAD.ChildDocProfileIDX,
DWH.ModifiedOn  =  RAD.ModifiedOn,
DWH.OrigChildDocProfileIDT  =  RAD.OrigChildDocProfileIDT,
DWH.PlanType  =  RAD.PlanType,
DWH.TempSrcIDT  =  RAD.TempSrcIDT,
DWH.CounslDurationMin  =  RAD.CounslDurationMin,
DWH.DurationAsNeeded  =  RAD.DurationAsNeeded,
DWH.DurationAsNeededDESC  =  RAD.DurationAsNeededDESC,
DWH.DurationMins  =  RAD.DurationMins,
DWH.DurationMinsText  =  RAD.DurationMinsText,
DWH.DurationNurse  =  RAD.DurationNurse,
DWH.DurationNurseDESC  =  RAD.DurationNurseDESC,
DWH.DurationTxt  =  RAD.DurationTxt,
DWH.FrequencyAsNeed  =  RAD.FrequencyAsNeed,
DWH.FrequencyAsNeedDESC  =  RAD.FrequencyAsNeedDESC,
DWH.FrequencyNurse  =  RAD.FrequencyNurse,
DWH.FrequencyNurseDESC  =  RAD.FrequencyNurseDESC,
DWH.FrequencyTxt  =  RAD.FrequencyTxt,
DWH.GroupOtherSize  =  RAD.GroupOtherSize,
DWH.GroupOtherSizeDescription  =  RAD.GroupOtherSizeDescription,
DWH.Groups  =  RAD.Groups,
DWH.GroupsDESC  =  RAD.GroupsDESC,
DWH.GroupTxt  =  RAD.GroupTxt,
DWH.IsTwelveMonthProgram  =  RAD.IsTwelveMonthProgram,
DWH.Language  =  RAD.Language,
DWH.LanguageDESC  =  RAD.LanguageDESC,
DWH.LocationNotRequired  =  RAD.LocationNotRequired,
DWH.LocationOtherTxt  =  RAD.LocationOtherTxt,
DWH.LocationTxt  =  RAD.LocationTxt,
DWH.NurseDeliveryTxt  =  RAD.NurseDeliveryTxt,
DWH.NurseGroup  =  RAD.NurseGroup,
DWH.NurseGroupDESC  =  RAD.NurseGroupDESC,
DWH.OtherFrequencyRS  =  RAD.OtherFrequencyRS,
DWH.PerWeekMonthNotReq  =  RAD.PerWeekMonthNotReq,
DWH.PerWeekMonthNotReqDESC  =  RAD.PerWeekMonthNotReqDESC,
DWH.PerWeekorMonths  =  RAD.PerWeekorMonths,
DWH.TimesPer  =  RAD.TimesPer,
DWH.RelatedServiceLocation  =  RAD.RelatedServiceLocation,
DWH.RSLocationDESC  =  RAD.RSLocationDESC,
DWH.SelectedService  =  RAD.SelectedService,
DWH.Service  =  RAD.Service,
DWH.ServiceDescription  =  RAD.ServiceDescription,
DWH.SourceChildDocProfileIDT  =  RAD.SourceChildDocProfileIDT,
DWH.TimesPerWk  =  RAD.TimesPerWk,
DWH.TimesPerWkDESC  =  RAD.TimesPerWkDESC,
DWH.TransOralSignDurationOther  =  RAD.TransOralSignDurationOther,
DWH.TransOralSignFreqOther  =  RAD.TransOralSignFreqOther,
DWH.CounselingFreqNotReq  =  RAD.CounselingFreqNotReq,
DWH.CounselingFreqNotDESC  =  RAD.CounselingFreqNotDESC,
DWH.CounselingLocationNotReq  =  RAD.CounselingLocationNotReq,
DWH.CounselingLocationNotReqDESC  =  RAD.CounselingLocationNotReqDESC,
DWH.CounselingOtherFrequency  =  RAD.CounselingOtherFrequency,
DWH.CounselingOtherFreqDESC  =  RAD.CounselingOtherFreqDESC,
DWH.CounselingOtherFrequencyTxt  =  RAD.CounselingOtherFrequencyTxt,
DWH.RSChildDocProfileIDT  =  RAD.RSChildDocProfileIDT,
DWH.IsDurationModified  =  RAD.IsDurationModified,
DWH.IsFrequencyModified  =  RAD.IsFrequencyModified,
DWH.PADRSCounslDurationMin  =  RAD.PADRSCounslDurationMin,
DWH.PADRSDurationAsNeeded  =  RAD.PADRSDurationAsNeeded,
DWH.PADRSDurationAsNeededDESC  =  RAD.PADRSDurationAsNeededDESC,
DWH.PADRSDurationMins  =  RAD.PADRSDurationMins,
DWH.PADRSDurationMinsText  =  RAD.PADRSDurationMinsText,
DWH.PADRSDurationNurse  =  RAD.PADRSDurationNurse,
DWH.PADRSDurationNurseDESC  =  RAD.PADRSDurationNurseDESC,
DWH.PADRSDurationTxt  =  RAD.PADRSDurationTxt,
DWH.PADRSFrequencyAsNeed  =  RAD.PADRSFrequencyAsNeed,
DWH.PADRSFrequencyAsNeedDESC  =  RAD.PADRSFrequencyAsNeedDESC,
DWH.PADRSFrequencyNurse  =  RAD.PADRSFrequencyNurse,
DWH.PADRSFrequencyTxt  =  RAD.PADRSFrequencyTxt,
DWH.PADRSGroups  =  RAD.PADRSGroups,
DWH.PADRSGroupsDESC  =  RAD.PADRSGroupsDESC,
DWH.PADRSLocation  =  RAD.PADRSLocation,
DWH.PADRSLocationDESC  =  RAD.PADRSLocationDESC,
DWH.PADRSNurseGroup  =  RAD.PADRSNurseGroup,
DWH.PADRSNurseGroupDESC  =  RAD.PADRSNurseGroupDESC,
DWH.PADRSOtherFrequencyRS  =  RAD.PADRSOtherFrequencyRS,
DWH.PADRSPerWeekMonthNotReq  =  RAD.PADRSPerWeekMonthNotReq,
DWH.PADRSPerWeekMonthNotReqDESC  =  RAD.PADRSPerWeekMonthNotReqDESC,
DWH.PADRSPerWeekorMonths  =  RAD.PADRSPerWeekorMonths,
DWH.PADRSPerWeekorMonthsDESC  =  RAD.PADRSPerWeekorMonthsDESC,
DWH.PADRSTimesPerWk  =  RAD.PADRSTimesPerWk,
DWH.PADRSTimesPerWkDESC  =  RAD.PADRSTimesPerWkDESC,
DWH.PADRSTransOralSignDurationOther  =  RAD.PADRSTransOralSignDurationOther,
DWH.PADRSTransOralSignFreqOther  =  RAD.PADRSTransOralSignFreqOther,
DWH.PADRSCounselingFreqNotReq  =  RAD.PADRSCounselingFreqNotReq,
DWH.PADRSCounselingFreqNotReqDESC  =  RAD.PADRSCounselingFreqNotReqDESC,
DWH.PADRSCounselingOtherFrequency  =  RAD.PADRSCounselingOtherFrequency,
DWH.PADRSCounselingOtherFreqDESC  =  RAD.PADRSCounselingOtherFreqDESC,
DWH.PADRSCounselingOtherFrequencyTxt  =  RAD.PADRSCounselingOtherFrequencyTxt,
DWH.ConsolidatedGroup  =  RAD.ConsolidatedGroup,
DWH.ConsolidatedGroupOther  =  RAD.ConsolidatedGroupOther,
DWH.RADConsolidatedGroup  =  RAD.RADConsolidatedGroup,
DWH.RADConsolidatedGroupOther  =  RAD.RADConsolidatedGroupOther,
DWH.ConsolidatedFrequency  =  RAD.ConsolidatedFrequency,
DWH.ConsolidatedFrequencyOther  =  RAD.ConsolidatedFrequencyOther,
DWH.RADConsolidatedFrequency  =  RAD.RADConsolidatedFrequency,
DWH.RADConsolidatedFrequencyOther  =  RAD.RADConsolidatedFrequencyOther,
DWH.ConsolidatedDuration  =  RAD.ConsolidatedDuration,
DWH.ConsolidatedDurationOther  =  RAD.ConsolidatedDurationOther,
DWH.RADConsolidatedDuration  =  RAD.RADConsolidatedDuration,
DWH.RADConsolidatedDurationOther  =  RAD.RADConsolidatedDurationOther,
DWH.ConsolidatedLocation  =  RAD.ConsolidatedLocation,
DWH.ConsolidatedLocationOther  =  RAD.ConsolidatedLocationOther,
DWH.RADConsolidatedLocation  =  RAD.RADConsolidatedLocation,
DWH.RADConsolidatedLocationOther  =  RAD.RADConsolidatedLocationOther,
DWH.GroupSize  =  RAD.GroupSize,
DWH.SchoolYear = RAD.SchoolYear,
DWH.IsDelete  =  RAD.IsDelete,
DWH.ProcessedDate  =  RAD.ProcessedDate


WHEN NOT MATCHED THEN

 INSERT (
StudentID,
ProfileIDT,
DocumentIDT,
DocStatus,
ParentDocumentIDT,
ChildDocProfileIDT,
ChildDocProfileIDX,
ModifiedOn,
OrigChildDocProfileIDT,
PlanType,
TempSrcIDT,
CounslDurationMin,
DurationAsNeeded,
DurationAsNeededDESC,
DurationMins,
DurationMinsText,
DurationNurse,
DurationNurseDESC,
DurationTxt,
FrequencyAsNeed,
FrequencyAsNeedDESC,
FrequencyNurse,
FrequencyNurseDESC,
FrequencyTxt,
GroupOtherSize,
GroupOtherSizeDescription,
Groups,
GroupsDESC,
GroupTxt,
IsTwelveMonthProgram,
Language,
LanguageDESC,
LocationNotRequired,
LocationOtherTxt,
LocationTxt,
NurseDeliveryTxt,
NurseGroup,
NurseGroupDESC,
OtherFrequencyRS,
PerWeekMonthNotReq,
PerWeekMonthNotReqDESC,
PerWeekorMonths,
TimesPer,
RelatedServiceLocation,
RSLocationDESC,
SelectedService,
Service,
ServiceDescription,
SourceChildDocProfileIDT,
TimesPerWk,
TimesPerWkDESC,
TransOralSignDurationOther,
TransOralSignFreqOther,
CounselingFreqNotReq,
CounselingFreqNotDESC,
CounselingLocationNotReq,
CounselingLocationNotReqDESC,
CounselingOtherFrequency,
CounselingOtherFreqDESC,
CounselingOtherFrequencyTxt,
RSChildDocProfileIDT,
IsDurationModified,
IsFrequencyModified,
PADRSCounslDurationMin,
PADRSDurationAsNeeded,
PADRSDurationAsNeededDESC,
PADRSDurationMins,
PADRSDurationMinsText,
PADRSDurationNurse,
PADRSDurationNurseDESC,
PADRSDurationTxt,
PADRSFrequencyAsNeed,
PADRSFrequencyAsNeedDESC,
PADRSFrequencyNurse,
PADRSFrequencyTxt,
PADRSGroups,
PADRSGroupsDESC,
PADRSLocation,
PADRSLocationDESC,
PADRSNurseGroup,
PADRSNurseGroupDESC,
PADRSOtherFrequencyRS,
PADRSPerWeekMonthNotReq,
PADRSPerWeekMonthNotReqDESC,
PADRSPerWeekorMonths,
PADRSPerWeekorMonthsDESC,
PADRSTimesPerWk,
PADRSTimesPerWkDESC,
PADRSTransOralSignDurationOther,
PADRSTransOralSignFreqOther,
PADRSCounselingFreqNotReq,
PADRSCounselingFreqNotReqDESC,
PADRSCounselingOtherFrequency,
PADRSCounselingOtherFreqDESC,
PADRSCounselingOtherFrequencyTxt,
ConsolidatedGroup,
ConsolidatedGroupOther,
RADConsolidatedGroup,
RADConsolidatedGroupOther,
ConsolidatedFrequency,
ConsolidatedFrequencyOther,
RADConsolidatedFrequency,
RADConsolidatedFrequencyOther,
ConsolidatedDuration,
ConsolidatedDurationOther,
RADConsolidatedDuration,
RADConsolidatedDurationOther,
ConsolidatedLocation,
ConsolidatedLocationOther,
RADConsolidatedLocation,
RADConsolidatedLocationOther,
GroupSize,
SchoolYear,
IsDelete,
ProcessedDate)

VALUES (
RAD.StudentID,
RAD.ProfileIDT,
RAD.DocumentIDT,
RAD.DocStatus,
RAD.ParentDocumentIDT,
RAD.ChildDocProfileIDT,
RAD.ChildDocProfileIDX,
RAD.ModifiedOn,
RAD.OrigChildDocProfileIDT,
RAD.PlanType,
RAD.TempSrcIDT,
RAD.CounslDurationMin,
RAD.DurationAsNeeded,
RAD.DurationAsNeededDESC,
RAD.DurationMins,
RAD.DurationMinsText,
RAD.DurationNurse,
RAD.DurationNurseDESC,
RAD.DurationTxt,
RAD.FrequencyAsNeed,
RAD.FrequencyAsNeedDESC,
RAD.FrequencyNurse,
RAD.FrequencyNurseDESC,
RAD.FrequencyTxt,
RAD.GroupOtherSize,
RAD.GroupOtherSizeDescription,
RAD.Groups,
RAD.GroupsDESC,
RAD.GroupTxt,
RAD.IsTwelveMonthProgram,
RAD.Language,
RAD.LanguageDESC,
RAD.LocationNotRequired,
RAD.LocationOtherTxt,
RAD.LocationTxt,
RAD.NurseDeliveryTxt,
RAD.NurseGroup,
RAD.NurseGroupDESC,
RAD.OtherFrequencyRS,
RAD.PerWeekMonthNotReq,
RAD.PerWeekMonthNotReqDESC,
RAD.PerWeekorMonths,
RAD.TimesPer,
RAD.RelatedServiceLocation,
RAD.RSLocationDESC,
RAD.SelectedService,
RAD.Service,
RAD.ServiceDescription,
RAD.SourceChildDocProfileIDT,
RAD.TimesPerWk,
RAD.TimesPerWkDESC,
RAD.TransOralSignDurationOther,
RAD.TransOralSignFreqOther,
RAD.CounselingFreqNotReq,
RAD.CounselingFreqNotDESC,
RAD.CounselingLocationNotReq,
RAD.CounselingLocationNotReqDESC,
RAD.CounselingOtherFrequency,
RAD.CounselingOtherFreqDESC,
RAD.CounselingOtherFrequencyTxt,
RAD.RSChildDocProfileIDT,
RAD.IsDurationModified,
RAD.IsFrequencyModified,
RAD.PADRSCounslDurationMin,
RAD.PADRSDurationAsNeeded,
RAD.PADRSDurationAsNeededDESC,
RAD.PADRSDurationMins,
RAD.PADRSDurationMinsText,
RAD.PADRSDurationNurse,
RAD.PADRSDurationNurseDESC,
RAD.PADRSDurationTxt,
RAD.PADRSFrequencyAsNeed,
RAD.PADRSFrequencyAsNeedDESC,
RAD.PADRSFrequencyNurse,
RAD.PADRSFrequencyTxt,
RAD.PADRSGroups,
RAD.PADRSGroupsDESC,
RAD.PADRSLocation,
RAD.PADRSLocationDESC,
RAD.PADRSNurseGroup,
RAD.PADRSNurseGroupDESC,
RAD.PADRSOtherFrequencyRS,
RAD.PADRSPerWeekMonthNotReq,
RAD.PADRSPerWeekMonthNotReqDESC,
RAD.PADRSPerWeekorMonths,
RAD.PADRSPerWeekorMonthsDESC,
RAD.PADRSTimesPerWk,
RAD.PADRSTimesPerWkDESC,
RAD.PADRSTransOralSignDurationOther,
RAD.PADRSTransOralSignFreqOther,
RAD.PADRSCounselingFreqNotReq,
RAD.PADRSCounselingFreqNotReqDESC,
RAD.PADRSCounselingOtherFrequency,
RAD.PADRSCounselingOtherFreqDESC,
RAD.PADRSCounselingOtherFrequencyTxt,
RAD.ConsolidatedGroup,
RAD.ConsolidatedGroupOther,
RAD.RADConsolidatedGroup,
RAD.RADConsolidatedGroupOther,
RAD.ConsolidatedFrequency,
RAD.ConsolidatedFrequencyOther,
RAD.RADConsolidatedFrequency,
RAD.RADConsolidatedFrequencyOther,
RAD.ConsolidatedDuration,
RAD.ConsolidatedDurationOther,
RAD.RADConsolidatedDuration,
RAD.RADConsolidatedDurationOther,
RAD.ConsolidatedLocation,
RAD.ConsolidatedLocationOther,
RAD.RADConsolidatedLocation,
RAD.RADConsolidatedLocationOther,
RAD.GroupSize,
RAD.SchoolYear,
RAD.IsDelete,
RAD.ProcessedDate
);

COMMIT TRAN;

----- Update IsDelete column -----------

BEGIN TRAN 

  UPDATE  DWH  SET IsDelete=1
  FROM DWH_RelatedServicesRAD DWH  WITH (NOLOCK)
  WHERE NOT EXISTS (select Distinct StudentID,DocumentIDT from #DWHRSRAD RAD where DWH.StudentID=RAD.StudentID and   DWH.DocumentIDT=RAD.DocumentIDT and DWH.ChildDocProfileIDT=RAD.ChildDocProfileIDT)

COMMIT TRAN;




GO


