USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPRPT_RSProvisioning]    Script Date: 12/9/2024 9:38:08 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE PROCEDURE [dbo].[USPRPT_RSProvisioning]

AS

Set XAct_Abort On
Set NoCount On

/**************************************************************************************************************************************************
Object Name: USP_RPTRSProvisioning
Purpose: Populate Related Services Linakge  data in SEO_MART database
Date Created: 06/17/2020

Modification Details:

Author					ModifiedDate		Comments
Phani Marupaka			08/27/2020			Add columns TotalEncounterService,SESISFirstEncounterDateService,SESISLastEncounterDateService,PAFirstAttendDateService,FirstAttendDateService
Phani Marupaka			10/05/2020			Add columns RSRADStatus,TotalRADAttempts,IsRADAttemptSuccessful,RADPrintDate,RADDocumentIDT
Phani Marupaka			10/27/2020			Add MatchKeyDuration column
Phani Marupaka			12/21/2020			Add columns TempResFlag,Ethnicity,EthnicityGroupCC,ELLStatus 
Phani Marupaka			01/06/2021			Add Assistive Technology services data 
Phani Marupaka			01/28/2021          Exclude students with Paraprofessional - D75 Inclusion services from RPT_ParaServicesLinkage table
Phani Marupaka			02/05/2021          Populate SchoolYear column in arch.RPT_RSProvisioning table
Christopher Agwu		08/17/2022			Added SuperintendentLocationCode column per JIRA ticket MIS-8496
***************************************************************************************************************************************************/

DECLARE @FYR as Char(4) = CASE WHEN SUBSTRING(replace(convert(varchar, getdate(),101),'/','') ,1,4)<'0715' THEN Year(getdate())
ELSE Year(getdate())+1 END

DECLARE @SCHOOLYEAR as VARCHAR(9)=CAST((@FYR-1) AS VARCHAR(4))+'-'+CAST(@FYR AS VARCHAR(4))



DECLARE @COUNT INT

SET @COUNT=(Select Count(*) from dbo.RPT_RSProvisioning WITH (NoLock))

IF (@COUNT<>0) 

BEGIN

TRUNCATE TABLE dbo.RPT_RSProvisioning

END;
---------------------------------
Set @Count=(Select Count(*) from dbo.RPT_RSProvisioning With (NoLock))
IF (@Count=0)

BEGIN
INSERT INTO  dbo.RPT_RSProvisioning (
StudentID,
ProfileIDT,
OutcomeDocumentIDT,
FirstName,
LastName,
BirthDate,
AgeSchoolStart,
EnrolledDBN,
PhysicalLocation,
PhysicalLocationName,
PhysicalLocationZipCode,
SchoolDistrict,
EnrollmentStatus,
GradeLevel,
EthnicityGroupCC,
ELLStatus,
TempResFlag,
OutcomeDocumentType,
MandateType,
ServiceType,
RecommendedGroupSizeNumeric,
RecommendedFrequencyNumeric,
RecommendedDurationNumeric,
RSMandateLanguage,
IntentNoticeReceivedDate,
PriorNoticePDate,
AuthorizationPDate,
RecentAuthorizationDate,
EffectiveOutcomeDate,
FieldSupportCenterReportingName,
SuperintendentName,
EnrolledSchoolSetting,
FirstAttendDate,
FirstAttendDateService,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
AttendRate,
TotalPartialEncounters,
SESISFirstPartialEncounterDate,
SESISLastPartialEncounterDate,
TotalFullEncounters,
SESISFirstFullEncounterDate,
SESISLastFullEncounterDate,
TotalEncounterService,
SESISFirstEncounterDateService,
SESISLastEncounterDateService,
FirstEncounterDate,
AssignmentStatus,
FirmName,
AgencyProvider,
EncounterProvider,
BigSixFlag,
FullEncounterFlag,
EncounterStatus,
RSRADStatus,
TotalRADAttempts,
IsRADAttemptSuccessful,
RADPrintDate,
RADDocumentIDT,
SchoolYear,
SuperintendentLocationCode,
OfficialClass,
GroupSizeDesc,
RecommendedLocationType)

SELECT *  FROM (
SELECT 
StudentID,
ProfileIDT,
OutcomeDocumentIDT,
FirstName,
LastName,
BirthDate,
AgeSchoolStart,
EnrolledDBN,
PhysicalLocation,
PhysicalLocationName,
PhysicalLocationZipCode,
SchoolDistrict,
EnrollmentStatus,
GradeLevel,
EthnicityGroupCC,
ELLStatus,
TempResFlag,
OutcomeDocumentType,
MandateType,
ServiceType,
RecommendedGroupSizeNumeric,
RecommendedFrequencyNumeric,
RecommendedDurationNumeric,
RSMandateLanguage,
IntentNoticeReceivedDate,
PriorNoticePDate,
AuthorizationPDate,
RecentAuthorizationDate,
EffectiveOutcomeDate,
FieldSupportCenterReportingName,
SuperintendentName,
EnrolledSchoolSetting,
FirstAttendDate,
FirstAttendDateService,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
AttendRate,
TotalPartialEncounters,
SESISFirstPartialEncounterDate,
SESISLastPartialEncounterDate,
TotalFullEncounters,
SESISFirstFullEncounterDate,
SESISLastFullEncounterDate,
TotalEncounterService,
SESISFirstEncounterDateService,
SESISLastEncounterDateService,
FirstEncounterDate,
AssignmentStatus,
FirmName,
AgencyProvider,
EncounterProvider,
BigSixFlag,
FullEncounterFlag,
EncounterStatus,
RSRADStatus,
TotalRADAttempts,
IsRADAttemptSuccessful,
RADPrintDate,
RADDocumentIDT,
@SCHOOLYEAR SchoolYear,
SuperintendentLocationCode,
OfficialClass,
GroupType,
RecommendedLocationType
 FROM dbo.RPT_RelatedServicesLinkage WHERE ReportingFlag='Y'

UNION ALL

SELECT
StudentID,
ProfileIDT,
OutcomeDocumentIDT,
FirstName,
LastName,
BirthDate,
AgeSchoolStart,
EnrolledDBN,
PhysicalLocation,
PhysicalLocationName,
PhysicalLocationZipCode,
SchoolDistrict,
EnrollmentStatus,
GradeLevel,
EthnicityGroupCC,
ELLStatus,
TempResFlag,
OutcomeDocumentType,
MandateType,
ServiceType,
RecommendedGroupSizeNumeric,
RecommendedFrequencyNumeric,
RecommendedDurationNumeric,
'NA' RSMandateLanguage,
IntentNoticeReceivedDate,
PriorNoticePDate,
AuthorizationPDate,
RecentAuthorizationDate,
EffectiveOutcomeDate,
FieldSupportCenterReportingName,
SuperintendentName,
EnrolledSchoolSetting,
FirstAttendDate,
FirstAttendDateService,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
MatchKey,
MatchKeyNL,
CONVERT(VARCHAR,NULL) MatchKeyDuration,
AttendRate,
TotalPartialEncounters,
SESISFirstPartialEncounterDate,
SESISLastPartialEncounterDate,
TotalFullEncounters,
SESISFirstFullEncounterDate,
SESISLastFullEncounterDate,
TotalEncounterService,
SESISFirstEncounterDateService,
SESISLastEncounterDateService,
FirstEncounterDate,
AssignmentStatus,
FirmName,
AgencyProvider,
EncounterProvider,
'N' BigSixFlag,
FullEncounterFlag,
EncounterStatus,
CONVERT(VARCHAR,NULL) RSRADStatus,
NULL TotalRADAttempts,
NULL IsRADAttemptSuccessful	,
CONVERT(DATETIME,NULL)  RADPrintDate,
NULL RADDocumentIDT,
@SCHOOLYEAR SchoolYear,
SuperintendentLocationCode,
OfficialClass,
RecommendedGroupType,
RecommendedLocationType
FROM dbo.RPT_ParaServicesLinkage where ReportingFlag='Y' and ServiceType not in ('Paraprofessional - D75 Inclusion')

UNION ALL

SELECT
StudentID,
ProfileIDT,
OutcomeDocumentIDT,
FirstName,
LastName,
BirthDate,
AgeSchoolStart,
EnrolledDBN,
PhysicalLocation,
PhysicalLocationName,
PhysicalLocationZipCode,
SchoolDistrict,
EnrollmentStatus,
GradeLevel,
EthnicityGroupCC,
ELLStatus,
TempResFlag,
OutcomeDocumentType,
MandateType,
'Assistive Technology Service' ServiceType,
CONVERT(INT,0) RecommendedGroupSizeNumeric,
CONVERT(INT,0) RecommendedFrequencyNumeric,
CONVERT(INT,0) RecommendedDurationNumeric,
'NA' RSMandateLanguage,
IntentNoticeReceivedDate,
PriorNoticePDate,
AuthorizationPDate,
RecentAuthorizationDate,
EffectiveOutcomeDate,
FieldSupportCenterReportingName,
SuperintendentName,
EnrolledSchoolSetting,
FirstAttendDate,
CONVERT(DATE,NULL) FirstAttendDateService,
PAFirstFullAttendDate,
CONVERT(DATE,NULL) PAFirstPartialAttendDate,
CONVERT(DATE,NULL) PAFirstAttendDateService,
CONVERT(VARCHAR,NULL) MatchKey,
CONVERT(VARCHAR,NULL) MatchKeyNL,
CONVERT(VARCHAR,NULL) MatchKeyDuration,
AttendRate,
CONVERT(INT,NULL) TotalPartialEncounters,
CONVERT(DATE,NULL) SESISFirstPartialEncounterDate,
CONVERT(DATE,NULL) SESISLastPartialEncounterDate,
TotalFullEncounters,
SESISFirstFullEncounterDate,
SESISLastFullEncounterDate,
CONVERT(INT,NULL) TotalEncounterService,
CONVERT(DATE,NULL) SESISFirstEncounterDateService,
CONVERT(DATE,NULL) SESISLastEncounterDateService,
FirstEncounterDate,
AssignmentStatus,
FirmName,
AgencyProvider,
EncounterProvider,
'N' BigSixFlag,
FullEncounterFlag,
EncounterStatus,
CONVERT(VARCHAR,NULL) RSRADStatus,
NULL TotalRADAttempts,
NULL IsRADAttemptSuccessful	,
CONVERT(DATETIME,NULL)  RADPrintDate,
NULL RADDocumentIDT,
@SCHOOLYEAR SchoolYear,
SuperintendentLocationCode,
OfficialClass,
RecommendedGroupType,
RecommendedLocationType
FROM dbo.RPT_AssistiveTechnology where ReportingFlag='Y') UN 

END;


----------------------- Archive RS Provisioning data ------------------------------------



BEGIN

INSERT INTO  arch.RPT_RSProvisioning 
(StudentID,
ProfileIDT,
OutcomeDocumentIDT,
FirstName,
LastName,
BirthDate,
AgeSchoolStart,
EnrolledDBN,
PhysicalLocation,
PhysicalLocationName,
PhysicalLocationZipCode,
SchoolDistrict,
EnrollmentStatus,
GradeLevel,
EthnicityGroupCC,
ELLStatus,
TempResFlag,
OutcomeDocumentType,
MandateType,
ServiceType,
RecommendedGroupSizeNumeric,
RecommendedFrequencyNumeric,
RecommendedDurationNumeric,
RSMandateLanguage,
IntentNoticeReceivedDate,
PriorNoticePDate,
AuthorizationPDate,
RecentAuthorizationDate,
EffectiveOutcomeDate,
FieldSupportCenterReportingName,
SuperintendentName,
EnrolledSchoolSetting,
FirstAttendDate,
FirstAttendDateService,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
AttendRate,
TotalPartialEncounters,
SESISFirstPartialEncounterDate,
SESISLastPartialEncounterDate,
TotalFullEncounters,
SESISFirstFullEncounterDate,
SESISLastFullEncounterDate,
TotalEncounterService,
SESISFirstEncounterDateService,
SESISLastEncounterDateService,
FirstEncounterDate,
AssignmentStatus,
FirmName,
AgencyProvider,
EncounterProvider,
BigSixFlag,
FullEncounterFlag,
EncounterStatus,
RSRADStatus,
TotalRADAttempts,
IsRADAttemptSuccessful,
SchoolYear,
RADPrintDate,
RADDocumentIDT,
SuperintendentLocationCode,
OfficialClass,
GroupSizeDesc,
RecommendedLocationType,
ProcessedDate,
ProcessedDateTime,
ArchiveDateTime
)

SELECT
StudentID,
ProfileIDT,
OutcomeDocumentIDT,
FirstName,
LastName,
BirthDate,
AgeSchoolStart,
EnrolledDBN,
PhysicalLocation,
PhysicalLocationName,
PhysicalLocationZipCode,
SchoolDistrict,
EnrollmentStatus,
GradeLevel,
EthnicityGroupCC,
ELLStatus,
TempResFlag,
OutcomeDocumentType,
MandateType,
ServiceType,
RecommendedGroupSizeNumeric,
RecommendedFrequencyNumeric,
RecommendedDurationNumeric,
RSMandateLanguage,
IntentNoticeReceivedDate,
PriorNoticePDate,
AuthorizationPDate,
RecentAuthorizationDate,
EffectiveOutcomeDate,
FieldSupportCenterReportingName,
SuperintendentName,
EnrolledSchoolSetting,
FirstAttendDate,
FirstAttendDateService,
PAFirstFullAttendDate,
PAFirstPartialAttendDate,
PAFirstAttendDateService,
MatchKey,
MatchKeyNL,
MatchKeyDuration,
AttendRate,
TotalPartialEncounters,
SESISFirstPartialEncounterDate,
SESISLastPartialEncounterDate,
TotalFullEncounters,
SESISFirstFullEncounterDate,
SESISLastFullEncounterDate,
TotalEncounterService,
SESISFirstEncounterDateService,
SESISLastEncounterDateService,
FirstEncounterDate,
AssignmentStatus,
FirmName,
AgencyProvider,
EncounterProvider,
BigSixFlag,
FullEncounterFlag,
EncounterStatus,
RSRADStatus,
TotalRADAttempts,
IsRADAttemptSuccessful,
SchoolYear,
RADPrintDate,
RADDocumentIDT,
SuperintendentLocationCode,
OfficialClass,
GroupSizeDesc,
RecommendedLocationType,
ProcessedDate,
ProcessedDateTime,
GETDATE() as ArchiveDateTime
FROM dbo.RPT_RSProvisioning


END;






GO


