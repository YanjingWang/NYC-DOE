USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPRPT_RelatedServicesLinkage]    Script Date: 12/9/2024 9:21:51 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[USPRPT_RelatedServicesLinkage]

AS
     BEGIN
         SET XACT_ABORT ON;
         SET NOCOUNT ON;
/**************************************************************************************************************************************************
Object Name: USP_RPTRelatedServicesLinkage
Purpose: Populate Related Services Linakge  data in SEO_MART database
Date Created: 06/17/2020

Modification Details:

Author					ModifiedDate		Comments
Phani Marupaka			08/26/2020			Add columns TotalEncounterService,SESISFirstEncounterDateService,SESISLastEncounterDateService,PAFirstAttendDateService,FirstAttendDateService
Phani Marupaka			10/02/2020			Add columns  RADDocumentIDT, RSRADStatus,TotalRADAttempts,IsRADAttemptSuccessful,RADPrintDate
Phani Marupaka			10/27/2020			Add MatchKeyDuration column, Include INT_EncounterAttendanceLinkage, INT_ProviderAssignmentLinkage tables for EA and PA columns	
Phani Marupaka			12/21/2020			Add TempResFlag,EthnicityGroupCC,ELLStatus columns and populated from from RPT_StudentRegister
Phani Marupaka			06/16/2021			Add SchoolYear column to RPT_RelatedServicesLinkage and arch.RPT_RelatedServicesLinkage tables
Christopher Agwu		04/20/2022			Added MatchKeyDuration to update join(s) to ensure tables are correctly joined.
Christopher Agwu		08/17/2022			Added SuperintendentLocationCode column per JIRA ticket MIS-8496
Sergey G				03/15/2023			Added SchoolYear into some to insure uniqueness 
Raji M					10/27/2024			PhysicalLocation in INT_StudentDemographics and RPT_StudentRegister is modified as "DBN@BuildingCode". 
											Prior to this, PhysicalLocation used to be a "DBN".											
											As a consequence of this chagne, the joins involving "PhysicalLocation = DBN"
												are updated to to left(PhysicalLocation, 6) = DBN
											Also, modified computation of SY and added @ETLProcessedDate and @ETLProcessedDateTime
***************************************************************************************************************************************************/

    /**** SchoolYear Calculation ****/
/*
DECLARE @FYR as Char(4) = CASE WHEN SUBSTRING(replace(convert(varchar, getdate(),101),'/','') ,1,4)<'0715' THEN Year(getdate())
ELSE Year(getdate())+1 END

DECLARE @SCHOOLYEAR as VARCHAR(9)=CAST((@FYR-1) AS VARCHAR(4))+'-'+CAST(@FYR AS VARCHAR(4))
*/
DECLARE @SCHOOLYEAR as VARCHAR(9)
set @SCHOOLYEAR = dbo.fn_DynamicSY(7, 15) 

DECLARE @ETLProcessedDate date, @ETLProcessedDateTime datetime
select @ETLProcessedDate  = cast(getdate() as date), @ETLProcessedDateTime = getdate()
DECLARE @COUNT INT;

SET @COUNT = (SELECT COUNT(*) FROM dbo.RPT_RelatedServicesLinkage);

  IF(@COUNT <> 0)

    BEGIN

    TRUNCATE TABLE dbo.RPT_RelatedServicesLinkage;

    END;


BEGIN

INSERT INTO dbo.RPT_RelatedServicesLinkage
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
RecommendedStartDate,
RecommendedEndDate,
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
MatchKey,
MatchKeyNL,
MatchKeyDuration,
AttendRate,
BigSixFlag,
ReportingFlag,
ProcessedDate,
ProcessedDateTime,
SchoolYear,
SuperintendentLocationCode,
OfficialClass,
GroupType,
RecommendedLocationType)


SELECT
IR.StudentID,
IR.ProfileIDT,
IR.OutcomeDocumentIDT,
SR.FirstName,
SR.LastName,
SR.BirthDate,
SR.AgeSchoolStart,
SR.EnrolledDBN,
SR.PhysicalLocation,
L1.LocationName PhysicalLocationName,
L1.ZipCode PhysicalLocationZipCode,
L.AdminDistrict SchoolDistrict,
SR.EnrollmentStatus,
SR.GradeLevel,
SR.EthnicityGroupCC,
SR.ELLStatus,
SR.TempResFlag,
IR.OutcomeDocumentType,
'RS' MandateType,
IR.ServiceType,
IR.RecommendedStartDate,
IR.RecommendedEndDate,
IR.RecommendedGroupSizeNumeric,
Ir.RecommendedFrequencyNumeric,
IR.RecommendedDurationNumeric,
IR.RSMandateLanguage,
IR.IntentNoticeReceivedDate,
IR.PriorNoticePDate,
IR.AuthorizationPDate,
IR.RecentAuthorizationDate,
IR.EffectiveOutcomeDate,
L.FieldSupportCenterReportingName,
L.SuperintendentName,
SR.EnrolledSchoolSetting,
IR.MatchKey,
IR.MatchKeyNL,
IR.MatchKeyDuration,
SR.AttendRate,
CASE WHEN  IR.ServiceType in( 'Speech-Language Therapy','Vision Education Services','Hearing Education Services','Physical Therapy','Occupational Therapy'
												,'Counseling Services') THEN 'Y' ELSE 'N' END AS BigSixFlag,

CASE WHEN  EnrollmentStatus in('A') AND EnrolledSchoolSetting in('CSD','Charter') 
												AND GradeLevel Not in ('IN','PK') THEN 'Y' ELSE 'N'  END  ReportingFlag,
@ETLProcessedDate as ProcessedDate,
@ETLProcessedDateTime as ProcessedDateTime,
@SCHOOLYEAR SchoolYear,
L.SuperintendentLocationCode,
SR.OfficialClass,
IR.GroupType,
IR.RecommendedLocationType

FROM (Select * from dbo.INT_RelatedServices  where ActiveServiceFlag='Y' and ActiveDocumentFlag='Y') IR
INNER JOIN SEO_MART.dbo.RPT_StudentRegister SR on SR.StudentID=IR.StudentID
LEFT JOIN SEO_MART.dbo.RPT_Locations L on SR.EnrolledDBN=L.SchoolDBN and L.ActiveFlag='Y' 
--BEGIN: Change - Raji - 10/27/24
--LEFT JOIN SEO_MART.dbo.RPT_Locations L1 on SR.PhysicalLocation=L1.SchoolDBN and L1.ActiveFlag='Y'   
LEFT JOIN SEO_MART.dbo.RPT_Locations L1 on LEFT(SR.PhysicalLocation, 6) = L1.SchoolDBN and L1.ActiveFlag='Y'   
--END: Change - Raji - 10/27/24

END;



------- UPDATE PA columns -------

BEGIN

UPDATE RS SET PAFirstFullAttendDate=PA.PAFirstFullAttendDate,
			  AssignmentStatus=	PA.AssignmentStatusName,
			  FirmName = PA.FirmName,
			  AgencyProvider = PA.AgencyProvider
FROM dbo.RPT_RelatedServicesLinkage RS
INNER JOIN (Select * from dbo.INT_ProviderAssignmentLinkage ) PA on RS.MatchKeyDuration=PA.MatchKeyDuration and rs.SchoolYear = pa.SchoolYear -- SchoolYear added by SergeyG

END;


BEGIN

UPDATE RS SET PAFirstPartialAttendDate=PA.PAFirstPartialAttendDate
			
FROM dbo.RPT_RelatedServicesLinkage RS
INNER JOIN (Select * from dbo.INT_ProviderAssignmentLinkage) PA on RS.MatchKeyNL=PA.MatchKeyNL  and rs.SchoolYear = pa.SchoolYear -- SchoolYear added by SergeyG
and RS.MatchKeyDuration=PA.MatchKeyDuration	--added by cagwu to corretly join rows

END;


BEGIN

UPDATE RS SET PAFirstAttendDateService=PA.PAFirstPartialAttendDate
			
FROM dbo.RPT_RelatedServicesLinkage RS
INNER JOIN (Select * from dbo.INT_ProviderAssignmentLinkage) PA on RS.StudentID=PA.StudentID and RS.ServiceType=PA.ServiceType and rs.SchoolYear = pa.SchoolYear -- SchoolYear added by SergeyG
and RS.MatchKeyDuration=PA.MatchKeyDuration	--added cagwu to corretly join rows

END;


------- UPDATE EA columns -------


BEGIN

UPDATE RS SET	RS.SESISFirstFullEncounterDate=EA.SESISFirstFullEncounterDate,
				RS.SESISLastFullEncounterDate=EA.SESISLastFullEncounterDate,
				RS.TotalFullEncounters=EA.TotalFullEncounters,
				EncounterProvider=EA.EncounterProvider	
FROM dbo.RPT_RelatedServicesLinkage RS
INNER JOIN  (Select * from dbo.INT_EncounterAttendanceLinkage ) EA on RS.MatchKeyDuration=EA.MatchKeyDuration

END;


BEGIN

UPDATE RS SET	
				RS.SESISFirstPartialEncounterDate=EA.SESISFirstPartialEncounterDate,
				RS.SESISLastPartialEncounterDate=EA.SESISLastPartialEncounterDate,
				RS.TotalPartialEncounters=EA.TotalPartialEncounters,
				EncounterProvider=EA.EncounterProvider	
	
FROM dbo.RPT_RelatedServicesLinkage RS
INNER JOIN  (Select * from dbo.INT_EncounterAttendanceLinkage ) EA on RS.MatchKeyNL=EA.MatchKeyNL
and RS.MatchKeyDuration=EA.MatchKeyDuration --added cagwu to corretly join rows

END;



BEGIN

UPDATE RS SET	RS.SESISFirstEncounterDateService=EA.SESISFirstEncounterDateService,
				RS.SESISLastEncounterDateService=EA.SESISLastEncounterDateService,
				RS.TotalEncounterService=EA.TotalEncounterService				
FROM dbo.RPT_RelatedServicesLinkage RS
INNER JOIN  (Select * from dbo.INT_EncounterAttendanceLinkage) EA on RS.StudentID=EA.StudentID and RS.ServiceType=EA.ServiceType
and RS.MatchKeyDuration=EA.MatchKeyDuration --added by cagwu to corretly join rows

END;

BEGIN

UPDATE dbo.RPT_RelatedServicesLinkage  SET	FirstAttendDate= CASE WHEN SESISFirstFullEncounterDate IS NOT NULL THEN SESISFirstFullEncounterDate  ELSE PAFirstFullAttendDate END

END


BEGIN

UPDATE dbo.RPT_RelatedServicesLinkage  SET	FirstAttendDateService= CASE WHEN SESISFirstEncounterDateService IS NOT NULL THEN SESISFirstEncounterDateService  ELSE PAFirstAttendDateService END

END



------- UPDATE RPT RS Linkage columns -------

BEGIN

UPDATE dbo.RPT_RelatedServicesLinkage SET FirstEncounterDate= CASE WHEN FirstAttendDate IS NULL THEN SESISFirstPartialEncounterDate
														 WHEN 	SESISFirstPartialEncounterDate<FirstAttendDate THEN SESISFirstPartialEncounterDate ELSE FirstAttendDate END,

							EncounterStatus= CASE WHEN FirstAttendDate Is Not Null then 'Full Encounter'
									WHEN FirstAttendDate Is  Null and SESISFirstPartialEncounterDate Is Not Null And (ServiceType='Counseling Services' And RSMandateLanguage<>'English'
											Or ServiceType='Speech-Language Therapy' And RSMandateLanguage<>'English') THEN  'Partial Encounter' ELSE  'No Encounter' END						


END;

BEGIN

UPDATE dbo.RPT_RelatedServicesLinkage SET FullEncounterFlag= CASE WHEN FirstAttendDate Is Not Null THEN 'Y' ELSE 'N' END


END;


------- UPDATE RS RAD columns -------

BEGIN

UPDATE RPT SET  RPT.RSRADStatus = INT.RSRADStatus,
				RPT.TotalRADAttempts = INT.TotalRADAttempts,
				RPT.IsRADAttemptSuccessful = INT.IsRADAttemptSuccessful,
				RPT.RADPrintDate = INT.RADPrintDate,
				RPT.RADDocumentIDT	= INT.DocumentIDT			
 FROM dbo.RPT_RelatedServicesLinkage RPT
INNER JOIN  ( Select * from (
Select MatchKey,DocumentIDT,LatestConfDocIDT,Row_Number() Over (Partition By MatchKey Order By DocStatus DESC,
 DocumentCreatedDateTime Desc, ISNULL(DocumentModifiedDateTime, CAST('1900-01-01' as DATETIME)) desc,ISNULL(DocumentFinalizedDateTime, CAST('1900-01-01' as DATETIME)) desc) RNK,
 RSRADStatus,TotalRADAttempts,IsRADAttemptSuccessful,RADPrintDate from dbo.INT_RSRADProfiles ) A where RNK=1) INT on RPT.MatchKey=INT.MatchKey and INT.LatestConfDocIDT=RPT.OutcomeDocumentIDT



END;

END;


------ Archiev Data -------

BEGIN

INSERT INTO Arch.RPT_RelatedServicesLinkage
(
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
RecommendedStartDate,
RecommendedEndDate,
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
ReportingFlag,
FullEncounterFlag,
EncounterStatus,
RADDocumentIDT,
RSRADStatus,
TotalRADAttempts,
IsRADAttemptSuccessful,
RADPrintDate,
SchoolYear,
SuperintendentLocationCode,
OfficialClass,
GroupType,
RecommendedLocationType,
ProcessedDate,
ProcessedDateTime,
ArchiveDateTime)



SELECT  StudentID,
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
RecommendedStartDate,
RecommendedEndDate,
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
ReportingFlag,
FullEncounterFlag,
EncounterStatus,
RADDocumentIDT,
RSRADStatus,
TotalRADAttempts,
IsRADAttemptSuccessful,
RADPrintDate,
SchoolYear,
SuperintendentLocationCode,
OfficialClass,
GroupType,
RecommendedLocationType,
ProcessedDate,
ProcessedDateTime,
@ETLProcessedDateTime as ArchiveDateTime FROM dbo.RPT_RelatedServicesLinkage

END;
GO


