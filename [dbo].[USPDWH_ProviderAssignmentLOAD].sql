USE [SEO_MART]
GO

/****** Object:  StoredProcedure [dbo].[USPDWH_ProviderAssignmentLOAD]    Script Date: 12/9/2024 9:35:00 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--Exec DWH_ProviderAssignmentLOAD

CREATE  PROCEDURE [dbo].[USPDWH_ProviderAssignmentLOAD]
AS
     BEGIN
         SET XACT_ABORT ON;
         SET NOCOUNT ON;

/*********************************************************************************************************************************************************
Object Name: dbo.DWH_ProviderAssignmentLOAD
Sample call: Exec DWH_ProviderAssignmentLOAD
Purpose: It is used to populate Provider Assignment data into SEO_MART
Date Created: 07/06/2018

Modification Details:

Author					ModifiedDate		Comments
Nithya Guruprakash						Initial Draft - Populate Provider Assignment for latest 3 years
Phani Marupaka          06/13/2020		ADEmpID column is added
Raja M					10/12/2021		Added a new column CreatedBy to support a charter file issue.
Raja M					11/17/2021		Uncommented the truncate statement and commented the date filter in the where clause to account for full load
Christopher Agwu		06/13/2022		Changed all lk.ParaType to lk.ParaTypeSpecialTransportation (to fix paratype desc from Para -Transportation to ParaProfesstional - Special Transportation)
											See JIRA ticket MIS-8087
Pratap Pasam            06/02/2023		Updated ProviderAssignment_Link.ProviderAssignment.PA.ServiceTypeLookup to dbo.lk_PAServiceType
Sergey G				07/19/2023		Commented out setting of @ProcessedDate as part of rollover Automation; @ProcessedDate is not used in the code since 11/17/2021 change
***********************************************************************************************************************************************************/

         DECLARE @COUNT INT;
         DECLARE @ProcessedDate DATETIME;
		 Declare @Job_Start DateTime
         Set @Job_Start=getdate();
/*
--	commented out on 7/19/2023 by SergeyG after review as part of rollover conversion from manual to Automated state
--		because the @ProcessedDate is not used in the code since the change 11/17/2021 and this part remained not commented out 

         SET @ProcessedDate =
(
    SELECT dateadd(dd,-2,max(processeddate))-- MAX(ProcessedDate) --minus 2 days because the source table gets loaded for previous day's data after 7AM today
    FROM [dbo].[DWH_ProviderAssignment] WITH (NoLock)
);
*/
         SELECT 'step0';
--         SET @COUNT =
--(
--    SELECT COUNT(*)
--    FROM dbo.DWH_ProviderAssignment
--);
--         IF(@COUNT <> 0)
--             BEGIN
                 TRUNCATE TABLE dbo.DWH_ProviderAssignment;			--Uncommenting this section and routing for full refresh daily. It needs to be redesigned as delta load later
--             END;
         --DECLARE @School_Year DATETIME;
         --SET @School_Year = CAST('07/01/'+CONVERT(VARCHAR(4), YEAR(GETDATE()) - 3) AS DATE);
         --SET @School_Year = GETDATE() - 400;
/*
--	commented out on 7/19/2023 by SergeyG after review as part of rollover conversion from manual to Automated state
--		because the @ProcessedDate is not used in the code since the change 11/17/2021 and this part remained not commented out 
         IF @ProcessedDate IS NULL
             SET @ProcessedDate = '2014-08-01';--once the process is tested, get this value from lk table
*/
If Object_ID('tempdb..#ProviderAssignment') is not null 
Drop Table #ProviderAssignment

         SELECT 'step1';
         SELECT distinct m.studentid,
                m.mandateStatusID,
                mstatus.mandatestatusname,
                stl.serviceTypeCode,
                --stl.serviceTypeName,
                --Isnull(lk.ParaType, stl.serviceTypeName) AS serviceTypeName,
				
				CASE WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.SEOServiceType) = 'S.E. Teacher Support Service (SETSS)' THEN 'Special Education Teacher Support Services (SETSS)'
				WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.SEOServiceType) = 'Hearing  Education Services' THEN 'Hearing Education Services'
				ELSE Isnull(lk.ParaTypeSpecialTransportation, stl.SEOServiceType) END AS serviceTypeName,
                Lang.LanguageCode PALanguage,
                lang.Description PALanguageDesc,
                DWH_Lang.SESISDescr SESISLanguageDesc,
                m.recommendedfrequency,
                m.recommendedgroupsize,
                m.RecommendedDuration,
                m.attendingAdminDBN,
                m.attendingPhysicalLocationDBN,
                m.authorizedadmindbn,
                m.AuthPhysicallocationDBN,
                a.firstattenddelayreason,
                a.firstattenddelayflag,
                astatus.AssignmentstatusID,
                astatus.Assignmentstatusname,
                a.FirstAttendDate,
                p.[Firm Name] FirmName,
                       --st.ssn AS [Actual Provider ID],
                st.[HRHubID] HRHubID,
				st.ADEmpID,
                st.LastName AS ProviderLastName,
                st.FirstName AS ProviderFirstName,
                SEO_MART.dbo.fn_SY(M.CreatedDate) AS SchoolYear,
                CAST(m.fiscalYear - 1 AS VARCHAR(4))+'-'+CAST(m.fiscalYear AS VARCHAR) fiscalYear,
                m.mandateId,
                m.MandateStartDate,
                M.MandateEndDate,
                M.CreatedDate MandateCreatedDate,
                a.serviceStartDate,
                A.ServiceEndDate,
				A.AssignmentID as AssignmentID,0 as IsDelete,'Merge' ProcessedUser,
               -- CAST(CONVERT(VARCHAR(8), GETDATE(), 112) AS DATE) AS ProcessedDate,
			   @Job_Start processedDate,--GETDATE() ProcessedDate,
                CONVERT(VARCHAR(9), M.StudentId)+' '+CASE
                                                         WHEN lk.ParaTypeSpecialTransportation IS NOT NULL
                                                         THEN lk.ParaTypeSpecialTransportation
                                                         --WHEN Isnull(lk.ParaType, stl.serviceTypeName) = 'S.E. Teacher Support Service (SETSS)'
                                                        -- THEN 'S.E. Teacher Support Service (SETSS)'+' '+isnull(dwh_lang.SESISDescr, '')
														--THEN 'Special Education Teacher Support Services (SETSS)'+' '+isnull(dwh_lang.SESISDescr, '')
                                                         WHEN m.recommendedgroupsize = 1
                                                         THEN CASE
                                                                  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'Hearing  Education Services'
                                                                  THEN 'Hearing Education Services'
																  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'S.E. Teacher Support Service (SETSS)'
																  THEN 'Special Education Teacher Support Services (SETSS)'
                                                                  ELSE Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName)
                                                              END+' '+'Individual'+' '+isnull(dwh_lang.SESISDescr, '')
                                                         WHEN m.recommendedgroupsize > 1
                                                         THEN CASE
                                                                  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'Hearing  Education Services'
                                                                  THEN 'Hearing Education Services'
																  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'S.E. Teacher Support Service (SETSS)'
																  THEN 'Special Education Teacher Support Services (SETSS)'
                                                                  ELSE Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName)
                                                              END+' '+'Group'+' '+isnull(dwh_lang.SESISDescr, '')
                                                         ELSE ' '
                                                     END AS MatchKey,
													 
													 CONVERT(VARCHAR(9), M.StudentId)+' '+CASE
                                                         WHEN lk.ParaTypeSpecialTransportation IS NOT NULL
                                                         THEN lk.ParaTypeSpecialTransportation
                                                         --WHEN Isnull(lk.ParaType, stl.serviceTypeName) = 'S.E. Teacher Support Service (SETSS)'
                                                        -- THEN 'S.E. Teacher Support Service (SETSS)'+' '+isnull(dwh_lang.SESISDescr, '')
														--THEN 'Special Education Teacher Support Services (SETSS)'+' '+isnull(dwh_lang.SESISDescr, '')
                                                         WHEN m.recommendedgroupsize = 1
                                                         THEN CASE
                                                                  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'Hearing  Education Services'
                                                                  THEN 'Hearing Education Services'
																  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'S.E. Teacher Support Service (SETSS)'
																  THEN 'Special Education Teacher Support Services (SETSS)'
                                                                  ELSE Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName)
                                                              END+' '+'Individual'
                                                         WHEN m.recommendedgroupsize > 1
                                                         THEN CASE
                                                                  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'Hearing  Education Services'
                                                                  THEN 'Hearing Education Services'
																  WHEN Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName) = 'S.E. Teacher Support Service (SETSS)'
																  THEN 'Special Education Teacher Support Services (SETSS)'
                                                                  ELSE Isnull(lk.ParaTypeSpecialTransportation, stl.serviceTypeName)
                                                              END+' '+'Group'
                                                         ELSE ' '
                                                     END AS MatchKeyNL,
													 M.CreatedBy
     
         INTO #ProviderAssignment
         FROM ProviderAssignment_Link.ProviderAssignment.pa.Mandates AS M WITH (NoLock)
              LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.Assignment A WITH (NoLock) ON(A.MandateId = M.MandateId
                                                                                                                 --AND FirstAttendDate > @school_year
                                                                                                                 --AND FirstAttendDate <= GETDATE()
              )
              --LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.ServiceTypeLookup STL WITH (NoLock) ON M.RecommendedServiceType = STL.servicetypecode
			  LEFT OUTER JOIN SEO_MART.dbo.lk_PAServiceType STL WITH (NoLock) ON M.RecommendedServiceType = STL.servicetypecode
              LEFT OUTER JOIN SEO_MART.dbo.lk_ParaType lk WITH (NoLock) ON lk.PAServiceTypeName = STL.ServiceTypeName
              LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.Language Lang WITH (NoLock) ON M.RecommendedLanguageCode = Lang.LanguageCode
              LEFT OUTER JOIN
(
Select DIstinct PACode,SESISDescr from (
       SelecT S.SourceName SESIS,P.SourceName PA,S.IDT SIDT,P.IDT PAIDT,S.CODE,P.Code PACode,S.Description SESISDescr,P.Description PAdesc from SEO_MART.dbo.lk_LanguageCodes S
       FULL JOIN (SELECT SourceName,IDT,CODE,Description  FROM SEO_MART.dbo.lk_LanguageCodes WITH (NoLock) where SourceName ='PA') P on S.IDT=P.IDT
       WHERE S.SourceName='SESIS' )X ) dwh_Lang ON M.RecommendedLanguageCode = DWH_lang.PACode
              LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.MandateStatus MStatus WITH (NoLock) ON M.MandateStatusId = MStatus.MandateStatusId
              LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.AssignmentStatus AStatus WITH (NoLock) ON A.AssignmentStatusId = AStatus.AssignmentStatusId
              LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.ContractAgencyLookup_Distinct P WITH (NoLock) ON A.VendorTaxID = p.TaxID
                     --LEFT OUTER JOIN ProviderAssignment_Link.ProviderAssignment.PA.Staff St WITH (NoLock) ON A.ActualProviderID = ST.SSN
              LEFT OUTER JOIN
(
    SELECT *
    FROM
(
    SELECT st.ssn,
			st.ADEmpID,	
           st.[HRHubID],
           st.LastName,
           st.FirstName,
           ROW_NUMBER() OVER(PARTITION BY ssn ORDER BY uniqueId DESC) AS CurrentRow
    FROM ProviderAssignment_Link.ProviderAssignment.PA.Staff St WITH (NoLock)
    WHERE ssn IS NOT NULL
) t
    WHERE currentrow = 1
) st ON A.ActualProviderID = ST.SSN

        /*																				Commenting this code block Start, on 11172021 since this is updated as a full load interim
		 WHERE(CONVERT(DATETIME, M.CreatedDate) > @ProcessedDate
               OR (M.UpdatedDate IS NOT NULL
                   AND CONVERT(DATETIME, M.UpdatedDate) > @ProcessedDate))
              OR (CONVERT(DATETIME, A.CreatedDate) > @ProcessedDate
                  OR (A.UpdatedDate IS NOT NULL
                      AND CONVERT(DATETIME, A.UpdatedDate) > @ProcessedDate))
		*/																			--Commenting this code code block End 


		 --M.CreatedDate >= @School_Year
               --AND M.CreatedDate <= GETDATE();
                     -- AND m.studentId IN(221294796, 221294796, 242286540,235274545,235603495,235248424,209623214,238356109,209854751,228883351,220555049,220070841  ,215452731 );

--         INSERT INTO dbo.DWH_ProviderAssignment
--(StudentId,
-- mandateStatusID,
-- mandatestatusname,
-- serviceTypeCode,
-- serviceTypeName,
-- PALanguage,
-- PALanguageDesc,
-- SESISLanguageDesc,
-- recommendedfrequency,
-- recommendedgroupsize,
-- RecommendedDuration,
-- attendingAdminDBN,
-- attendingPhysicalLocationDBN,
-- authorizedadmindbn,
-- AuthPhysicallocationDBN,
-- firstattenddelayreason,
-- firstattenddelayflag,
-- AssignmentstatusID,
-- Assignmentstatusname,
-- FirstAttendDate,
-- FirmName,
-- --ActualProviderID,
-- HRHubID,
-- ProviderLastName,
-- ProviderFirstName,
-- SchoolYear,
-- FiscalYear,
-- mandateId,
-- MandateStartDate,
-- MandateEndDate,
-- MandateCreatedDate,
-- ServiceStartDate,
-- ServiceEndDate,
-- ProcessedDate,
-- MatchKey
--)
--                SELECT StudentId,
--                       mandateStatusID,
--                       mandatestatusname,
--                       serviceTypeCode,
--                       serviceTypeName,
--                       PALanguage,
--                       PALanguageDesc,
--                       SESISLanguageDesc,
--                       recommendedfrequency,
--                       recommendedgroupsize,
--                       RecommendedDuration,
--                       attendingAdminDBN,
--                       attendingPhysicalLocationDBN,
--                       authorizedadmindbn,
--                       AuthPhysicallocationDBN,
--                       firstattenddelayreason,
--                       firstattenddelayflag,
--                       AssignmentstatusID,
--                       Assignmentstatusname,
--                       FirstAttendDate,
--                       FirmName,
-- --ActualProviderID,
--                       HRHubID,
--                       ProviderLastName,
--                       ProviderFirstName,
--                       SchoolYear,
--                       FiscalYear,
--                       mandateId,
--                       MandateStartDate,
--                       MandateEndDate,
--                       MandateCreatedDate,
--                       ServiceStartDate,
--                       ServiceEndDate,
--                       ProcessedDate,
--                       MatchKey
--                FROM #ProviderAssignment;

         BEGIN TRAN;
         MERGE dbo.DWH_ProviderAssignment WITH(HOLDLOCK) AS PA_Tgt
         USING #ProviderAssignment AS PA_Source
         ON(PA_Tgt.StudentID = PA_Source.StudentID
            AND PA_Tgt.mandateID = PA_Source.mandateID
            --AND isnull(PA_Tgt.assignmentStatusid,-1) = isnull(PA_Source.assignmentStatusid,-1)
            --AND isnull(PA_Tgt.ProviderFirstName,'xxx') = isnull(PA_Source.ProviderFirstName,'xxx')
            --AND isnull(PA_Tgt.ProviderLastName,'xxx') = isnull(PA_Source.ProviderLastName,'xxx')
            --AND isnull(PA_Tgt.firstAttendDelayFlag,'xxx') = isnull(PA_Source.firstAttendDelayFlag,'xxx')
            --AND isnull(PA_Tgt.FirstAttendDelayReason,'xxx') = isnull(PA_Source.FirstAttendDelayReason,'xxx')
            --AND isnull(PA_Tgt.FirstAttendDate,'1888-08-02') = isnull(PA_Source.FirstAttendDate,'1888-08-02')
			--AND isnull(PA_Tgt.firmName,'xxx')=isnull(PA_Source.firmName,'xxx')
			--AND isnull(PA_Tgt.ServiceStartDate,'1888-08-02')=isnull(PA_Source.ServiceStartDate,'1888-08-02')
			AND PA_Tgt.assignmentID=PA_Source.AssignmentID)
             WHEN MATCHED
             THEN UPDATE SET
                             --PA_Tgt.StudentId = PA_Source.StudentId,
                             PA_Tgt.mandateStatusID = PA_Source.mandateStatusID,
                             PA_Tgt.mandatestatusname = PA_Source.mandatestatusname,
                             PA_Tgt.serviceTypeCode = PA_Source.serviceTypeCode,
                             PA_Tgt.serviceTypeName = PA_Source.serviceTypeName,
                             PA_Tgt.PALanguage = PA_Source.PALanguage,
                             PA_Tgt.PALanguageDesc = PA_Source.PALanguageDesc,
                             PA_Tgt.SESISLanguageDesc = PA_Source.SESISLanguageDesc,
                             PA_Tgt.recommendedfrequency = PA_Source.recommendedfrequency,
                             PA_Tgt.recommendedgroupsize = PA_Source.recommendedgroupsize,
                             PA_Tgt.RecommendedDuration = PA_Source.RecommendedDuration,
                             PA_Tgt.attendingAdminDBN = PA_Source.attendingAdminDBN,
                             PA_Tgt.attendingPhysicalLocationDBN = PA_Source.attendingPhysicalLocationDBN,
                             PA_Tgt.authorizedadmindbn = PA_Source.authorizedadmindbn,
                             PA_Tgt.AuthPhysicallocationDBN = PA_Source.AuthPhysicallocationDBN,
                             PA_Tgt.firstattenddelayreason = PA_Source.firstattenddelayreason,
                             PA_Tgt.firstattenddelayflag = PA_Source.firstattenddelayflag,
                             PA_Tgt.AssignmentstatusID = PA_Source.AssignmentstatusID,
                             PA_Tgt.Assignmentstatusname = PA_Source.Assignmentstatusname,
                             PA_Tgt.FirstAttendDate = PA_Source.FirstAttendDate,
                             PA_Tgt.FirmName = PA_Source.FirmName,
                             PA_Tgt.HRHubID = PA_Source.HRHubID,
							 PA_Tgt.ADEmpID = PA_Source.ADEmpID,
                             PA_Tgt.ProviderLastName = PA_Source.ProviderLastName,
                             PA_Tgt.ProviderFirstName = PA_Source.ProviderFirstName,
                             PA_Tgt.SchoolYear = PA_Source.SchoolYear,
                             PA_Tgt.FiscalYear = PA_Source.FiscalYear,
                             --PA_Tgt.mandateId = PA_Source.mandateId,
                             PA_Tgt.MandateStartDate = PA_Source.MandateStartDate,
                             PA_Tgt.MandateEndDate = PA_Source.MandateEndDate,
                             PA_Tgt.MandateCreatedDate = PA_Source.MandateCreatedDate,
                             PA_Tgt.ServiceStartDate = PA_Source.ServiceStartDate,
                             PA_Tgt.ServiceEndDate = PA_Source.ServiceEndDate,
                             PA_Tgt.ProcessedDate = PA_Source.ProcessedDate,
                             PA_Tgt.MatchKey = PA_Source.MatchKey,
							 PA_Tgt.MatchKeyNL = PA_Source.MatchKeyNL,
							 PA_Tgt.IsDelete=PA_Source.IsDelete,
							 PA_Tgt.ProcessedUser=PA_Source.ProcessedUser,
							 PA_tgt.CreatedBy = PA_Source.CreatedBy
             WHEN NOT MATCHED
             THEN
               INSERT(StudentId,
                      mandateStatusID,
                      mandatestatusname,
                      serviceTypeCode,
                      serviceTypeName,
                      PALanguage,
                      PALanguageDesc,
                      SESISLanguageDesc,
                      recommendedfrequency,
                      recommendedgroupsize,
                      RecommendedDuration,
                      attendingAdminDBN,
                      attendingPhysicalLocationDBN,
                      authorizedadmindbn,
                      AuthPhysicallocationDBN,
                      firstattenddelayreason,
                      firstattenddelayflag,
                      AssignmentstatusID,
                      Assignmentstatusname,
                      FirstAttendDate,
                      FirmName,
 --ActualProviderID,
                      HRHubID,
					  ADEmpID,
                      ProviderLastName,
                      ProviderFirstName,
                      SchoolYear,
                      FiscalYear,
                      mandateId,
                      MandateStartDate,
                      MandateEndDate,
                      MandateCreatedDate,
                      ServiceStartDate,
                      ServiceEndDate,
					  AssignmentID,
                      ProcessedDate,
                      MatchKey,
					  MatchKeyNL,
					  IsDelete,
					  ProcessedUser, 
					  CreatedDate,
					  CreatedBy)
               VALUES
(PA_Source.StudentId,
 PA_Source.mandateStatusID,
 PA_Source.mandatestatusname,
 PA_Source.serviceTypeCode,
 PA_Source.serviceTypeName,
 PA_Source.PALanguage,
 PA_Source.PALanguageDesc,
 PA_Source.SESISLanguageDesc,
 PA_Source.recommendedfrequency,
 PA_Source.recommendedgroupsize,
 PA_Source.RecommendedDuration,
 PA_Source.attendingAdminDBN,
 PA_Source.attendingPhysicalLocationDBN,
 PA_Source.authorizedadmindbn,
 PA_Source.AuthPhysicallocationDBN,
 PA_Source.firstattenddelayreason,
 PA_Source.firstattenddelayflag,
 PA_Source.AssignmentstatusID,
 PA_Source.Assignmentstatusname,
 PA_Source.FirstAttendDate,
 PA_Source.FirmName,
 PA_Source.HRHubID,
 PA_Source.ADEmpID,
 PA_Source.ProviderLastName,
 PA_Source.ProviderFirstName,
 PA_Source.SchoolYear,
 PA_Source.FiscalYear,
 PA_Source.mandateId,
 PA_Source.MandateStartDate,
 PA_Source.MandateEndDate,
 PA_Source.MandateCreatedDate,
 PA_Source.ServiceStartDate,
 PA_Source.ServiceEndDate,
 PA_Source.AssignmentID,
 PA_Source.ProcessedDate,
 PA_Source.MatchKey,
 PA_Source.MatchKeyNL,
 PA_Source.IsDelete,
 PA_Source.ProcessedUser,
 PA_Source.processedDate,
 PA_Source.CreatedBy
);
COMMIT TRAN;

  BEGIN TRAN 
update  tgt
set 
IsDelete=1,
ProcessedUser='Inactive',
ProcessedDate=getdate()
from dbo.dwh_providerassignment  tgt with(nolock)
where NOT EXISTS (select 1 from ProviderAssignment_Link.ProviderAssignment.pa.Mandates  src with(nolock) where src.mandateid=tgt.mandateid)
  COMMIT TRAN;

         SELECT 'step 99';
     END;

	 

GO


