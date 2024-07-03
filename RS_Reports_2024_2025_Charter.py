import pyodbc
import pandas as pd
import os
from datetime import datetime
import openpyxl
from openpyxl import load_workbook
class RSCharter():
#************************************************************************************************
#                            
#                         RUN TIME : 20 MINS 
# 
#                       
#
#************************************************************************************************

#########################################################
#  ODBC DRIVERS NEEDED TO RUN PROGRAM 
######################################################### 
#  SEO_MART --> ES00VPADOSQL180,51433
#  MUST HAVE RTOOLS DOWNLOADED
#########################################################
    def __init__(self,schoolyear="SY 24-25"):
        self.schoolyear = schoolyear
    def RSWeeklyCharterExcel(self):
        start = datetime.now()

        # Establish a connection to the database
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ES00VPADOSQL180,51433;DATABASE=SEO_MART;Trusted_Connection=yes;')

        ##################################################################################
        # DATA PREP FOR REPORTS
        ##################################################################################

        # Fetch data from the database
        qry_report = "SELECT * FROM [SEO_MART].[dbo].[RPT_RSProvisioning] WHERE LEFT(EnrolledDBN, 2) = '84'"
        comp_report = """
            SELECT
                R.EnrolledDBN,
                R.EnrolledSchoolSetting,
                R1.FieldSupportCenterReportingName,
                SuperintendentName,
                Counseling,
                NotEncounteredCounsel,
                EncounteredCounsel,
                PercentageNotEncounteredCounsel,
                PercentageEncounteredCounsel,
                AllOtherMajorServices,
                NotEncounteredMajor,
                EncounteredMajor,
                PercentageNotEncounteredMajor,
                PercentageEncounteredMajor,
                AllRSServices,
                NotEncounteredAllRS,
                EncounteredAllRS,
                PercentageNotEncounteredAllRS,
                PercentageEncounteredAllRS,
                ProcessedDate,
                ProcessedDateTime,
                SchoolDistrict
            FROM
                (SELECT DISTINCT EnrolledDBN, EnrolledSchoolSetting FROM [SEO_MART].[dbo].[RPT_RSProvisioning] WHERE LEFT(EnrolledDBN, 2) = '84') R
                LEFT JOIN (SELECT * FROM [SEO_MART].[dbo].[RPT_RSCompliance] WHERE SchoolDistrict = 84) R1 ON R.EnrolledDBN = R1.EnrolledDBN
            ORDER BY R.EnrolledDBN ASC
        """
        comp_report2 = "SELECT * FROM [SEO_MART].[dbo].[RPT_RSCompliancebyGroup]"

        report_RS = pd.read_sql(qry_report, conn)
        report_citywide = pd.read_sql(comp_report, conn)
        report_citywide2 = pd.read_sql(comp_report2, conn)
        conn.close()

        # Debugging: Print column names
        print("report_RS columns:", report_RS.columns)

        # Check if the required columns are present
        required_columns = ['LastName', 'FirstName', 'AttendRate', 'EnrolledDBN']
        missing_columns = [col for col in required_columns if col not in report_RS.columns]
        if missing_columns:
            print("Missing columns in report_RS:", missing_columns)
        else:
            # Convert dates from SQL to m/d/y format
            report_RS['ProcessedDate'] = pd.to_datetime(report_RS['ProcessedDate'])

            # Replace original table
            report_RS_p2 = report_RS.copy()

            # Create temporary tables with transformations
            report_RS_Temp1 = report_RS_p2.copy()
            report_RS_Temp1['STUDENTNAME'] = report_RS_Temp1['LastName'] + ', ' + report_RS_Temp1['FirstName']
            report_RS_Temp1['Attendrate'] = (report_RS_Temp1['AttendRate'] * 100).round(0).astype(str) + '%'
            report_RS_Temp1['district'] = report_RS_Temp1['EnrolledDBN'].str[:2]

            report_RS_Temp = report_RS_Temp1[report_RS_Temp1['district'] == '84']

            report_RS_comp = report_citywide[['EnrolledDBN', 'FieldSupportCenterReportingName', 'SuperintendentName', 'NotEncounteredCounsel', 'EncounteredCounsel', 'PercentageEncounteredCounsel', 'NotEncounteredMajor', 'EncounteredMajor', 'PercentageEncounteredMajor', 'PercentageEncounteredAllRS']]

            # Creating different tables for various levels
            report_RS_dbn = report_RS_comp.copy()
            report_RS_dst = report_citywide2[report_citywide2['ReportGroupDesc'] == 'SchoolDistrict'].sort_values('SchoolDistrict')
            report_RS_sup = report_citywide2[report_citywide2['ReportGroupDesc'] == 'Superintendent'].sort_values('SuperintendentName')
            report_RS_fsc = report_citywide2[report_citywide2['ReportGroupDesc'] == 'FieldSupportCenter'].sort_values('FieldSupportCenterReportingName')

            report_asofdt = report_RS['ProcessedDate'].iloc[0]

            # Output Excel reports - WEEKLY SCHOOL LEVEL WITH 2 TABS
            dt = datetime.now().strftime("%Y%m%d")
            pth2 = f"R:/SEO Analytics/Reporting/Related Services/Output Files/{self.schoolyear} Charter/MandatedServicesCharter_{dt}"
            os.makedirs(pth2, exist_ok=True)

            for dbn in report_RS_comp['EnrolledDBN'].unique():
                print(dbn)
                mydata2 = report_RS_Temp[report_RS_Temp['EnrolledDBN'] == dbn]
                mycomp2 = report_RS_comp[report_RS_comp['EnrolledDBN'] == dbn]

                wb = load_workbook("C:/Template/RS_Template_new.xlsx")

                # Writing data to the workbook
                writer = pd.ExcelWriter("C:/Template/RS_Template_new.xlsx", engine='openpyxl')
                writer.book = wb

                mydata2.to_excel(writer, sheet_name='Data', startrow=5, index=False, header=False)
                pd.DataFrame([report_asofdt]).to_excel(writer, sheet_name='Data', startcol=1, startrow=0, index=False, header=False)
                mycomp2.to_excel(writer, sheet_name='Completion Reports', startrow=4, index=False, header=False)
                pd.DataFrame([report_asofdt]).to_excel(writer, sheet_name='Completion Reports', startcol=2, startrow=0, index=False, header=False)

                writer.save()

                pth = f"{pth2}/{dbn}_MandatedServices_{dt}.xlsx"
                wb.save(pth)

            end = datetime.now()
            print(start)
            print(end)

            # Mandated Services Charter report
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ES00VPADOSQL180,51433;DATABASE=SEO_MART;Trusted_Connection=yes;')
            Mandated_Charter = pd.read_sql("""
                SELECT 
                    STUDENTID as [STUDENT ID],
                    LastName + ', ' + FirstName as [STUDENT NAME],
                    ATTENDRATE as [ATTEND RATE],
                    ServiceType,
                    RecommendedGroupSizeNumeric as [GROUP SIZE], 
                    RecommendedFrequencyNumeric, 
                    RecommendedDurationNumeric, 
                    RSMandateLanguage, 
                    EnrolledDBN as [ATS DBN],
                    GradeLevel, 
                    BIRTHDATE as [BIRTH DATE],
                    EffectiveOutcomeDate as [IEP CONFERENCE DATE],
                    RECENTAUTHORIZATIONDATE as [RECENT AUTHORIZATION DATE],
                    PhysicalLocation as [SESIS PHYSICAL LOCATION],
                    PhysicalLocationNAME as [PHYSICAL LOCATION NAME],
                    PhysicalLocationZIPCODE AS [PHYSICAL LOCATION ZIPCODE],
                    MANDATETYPE as [MANDATE TYPE], 
                    FIRSTENCOUNTERDATE as [FIRST ENCOUNTER DATE],
                    PAFirstPartialAttendDate as [PA FIRST ATTEND DATE], 
                    SESISFirstPartialEncounterDate as [SESIS FIRST ENCOUNTER DATE],
                    TotalPartialEncounters as [TOTAL ENCOUNTERS ENTERED],
                    SESISLastPartialEncounterDate as [SESIS LAST ENCOUNTER DATE], 
                    ProcessedDate as [ASOFDATE]
                FROM SEO_MART.dbo.RPT_RSProvisioning WITH (NOLOCK)
                WHERE LEFT(EnrolledDBN, 2) = '84' AND [EnrollmentStatus] = 'A' 
                ORDER BY EnrolledDBN
            """, conn)
            conn.close()

            # Export to Excel
            pth9 = f"R:/SEO Analytics/Reporting/Related Services/Output Files/{self.schoolyear} Charter/MandatedServicesCharter_{dt}"
            pth10 = f"{pth9}/MandatedServicesCharter_{dt}.csv"
            Mandated_Charter.to_csv(pth10, index=False)

            print("Mandated Services Charter report completed")
            print("Time taken:", end - start)


if __name__ == "__main__":
    rs = RSCharter()
    rs.RSWeeklyCharterExcel()

