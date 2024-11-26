import pandas as pd
import pyodbc
import smtplib
from email.message import EmailMessage
import os
from datetime import datetime, timedelta
import shutil
import win32com.client as win32
class Solution:
    def __init__(self):
        self.recordcount = 77 # Record count for the request file and change it every week
        self.schoolyear = 'SY25'
        # Get today's date
        today = datetime.today()
        
        # Format this week and last week dates as strings (e.g., "11182024")
        self.thisweek = today.strftime("%m%d%Y")
        self.lastweek = (today - timedelta(days=7)).strftime("%m%d%Y")
        self.today = today.strftime("%m/%d/%y")
        
        # Print to verify the values
        print(f"This week: {self.thisweek}")
        print(f"Last week: {self.lastweek}")
        print(f"Today: {self.today}")
        # Database connection setup 'DRIVER=SQL SERVER;SERVER=ES00VPADOSQL180,51433;DATABASE=SEO_MART'
        self.connection_string = (
            "DRIVER=SQL Server;"
            "SERVER=ES00VPADOSQL180,51433;"
            "DATABASE=SEO_MART;"
            "Trusted_Connection=yes;"
        )
        self.conn = pyodbc.connect(self.connection_string)

        # Queries for validation
        self.queries = {
            "HouseNumber": """
                SELECT w.StudentID, w.ProcessedDatetime, w.HouseNumber, r.HouseNumber, c.HouseNumber
                FROM INT_T5WaveEligibleStudents w WITH (NOLOCK)
                LEFT JOIN RPT_T5StudentRegister r WITH (NOLOCK) ON r.StudentID = w.StudentID
                LEFT JOIN DWH_T5CAPExtract c WITH (NOLOCK) ON c.StudentID = w.StudentID
                WHERE w.IsSibling = 0
                AND LTRIM(RTRIM(r.HouseNumber)) <> LTRIM(RTRIM(w.HouseNumber))
                AND w.WaveID IS NULL
            """,
            "Street": """
                SELECT w.StudentID, w.ProcessedDatetime, w.Street, r.Street, c.Street
                FROM INT_T5WaveEligibleStudents w WITH (NOLOCK)
                LEFT JOIN RPT_T5StudentRegister r WITH (NOLOCK) ON r.StudentID = w.StudentID
                LEFT JOIN DWH_T5CAPExtract c WITH (NOLOCK) ON c.StudentID = w.StudentID
                WHERE w.IsSibling = 0
                AND LTRIM(RTRIM(r.Street)) <> LTRIM(RTRIM(w.Street))
                AND w.WaveID IS NULL
            """,
            "BoroughCode": """
                SELECT w.StudentID, w.ProcessedDatetime, w.BoroughCode, r.BoroughCode, c.BoroughCode
                FROM INT_T5WaveEligibleStudents w WITH (NOLOCK)
                LEFT JOIN RPT_T5StudentRegister r WITH (NOLOCK) ON r.StudentID = w.StudentID
                LEFT JOIN DWH_T5CAPExtract c WITH (NOLOCK) ON c.StudentID = w.StudentID
                WHERE w.IsSibling = 0
                AND r.BoroughCode <> w.BoroughCode
                AND w.WaveID IS NULL
            """,
            "ZipCode": """
                SELECT w.StudentID, w.ProcessedDatetime, w.ZipCode, r.ZipCode, c.ZipCode
                FROM INT_T5WaveEligibleStudents w WITH (NOLOCK)
                LEFT JOIN RPT_T5StudentRegister r WITH (NOLOCK) ON r.StudentID = w.StudentID
                LEFT JOIN DWH_T5CAPExtract c WITH (NOLOCK) ON c.StudentID = w.StudentID
                WHERE w.IsSibling = 0
                AND r.ZipCode <> w.ZipCode
                AND w.WaveID IS NULL
            """
        }

    def copy_file_to_archive(self, source_file, destination_dir):        
        # Ensure the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        # Build destination file path
        destination_file = os.path.join(destination_dir, os.path.basename(source_file))
        try:
            # Copy the file
            shutil.copy2(source_file, destination_file)  # copy2 preserves metadata
            print(f"File copied successfully to {destination_file}")
        except FileNotFoundError:
            print(f"Source file not found: {source_file}")
        except Exception as e:
            print(f"Error while copying file: {e}")

    def delete_file(self, file_path):        
        try:
            # Check if the file exists
            if os.path.exists(file_path):
                # Delete the file
                os.remove(file_path)
                print(f"File successfully deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error occurred while deleting the file: {e}")

    # Validation function
    def validate_data(self):
        issues = {}
        for check, query in self.queries.items():
            df = pd.read_sql(query, self.conn)
            if not df.empty:
                issues[check] = df
        return issues

    # Email preparation
    def t5Monday_send_outlook_email(self):
        # construct Outlook application instance
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        # construct the email item object
        mailItem = olApp.CreateItem(0)
        mailItem.Subject = "T5 ZONED SCHOOL REQUEST (Pre Wave Test 4)"
        mailItem.BodyFormat = 1
        mailItem.Body = f"""
        Hope all is well! Please see the latest LCGMS Geocoding and Zoning file request.

        Attached:

        {self.today} LCGMS Geocoding and Zoning Request file
        Zoned file output template
        Error file output template

        Request file details:

        Format: .xlsx
        Record Count: {self.recordcount}
        Field Count: 8

        StudentID
        IsSibling
        SiblingKey
        HouseNumber
        Street
        HouseNumberStreet
        BoroughCode
        ZipCode

        Return Zoned file details:

        Format: .csv
        Zoned Data: Current Zone ({self.schoolyear})
        Field count: 24

        GBATId
        StudentID
        IsSibling
        SiblingKey
        HouseNumber
        Street
        HouseNumberStreet
        BoroughCode
        ZipCode
        WA2_F1EX_XCoordinate
        WA2_F1EX_YCoordinate
        WA2_F1EX_ZipCode
        WA2_F1EX_CommunitySchoolDistrict
        WA2_F1EX_USPScityname
        WA2_F1EX_Latitude
        WA2_F1EX_Longitude
        WA2_F1AX_Latitude
        WA2_F1AX_Longitude
        WA2_F1AX_XCoordinate
        WA2_F1AX_YCoordinate
        ESNotes
        ESDBN
        ESID_NO
        ESZONED_DI

        Return Error file details:

        Format: .txt
        Field count: 13

        GRC
        ReasonCode
        GRC2
        ReasonCode2
        BadRecordId
        StudentID
        IsSibling
        SiblingKey
        HouseNumber
        Street
        HouseNumberStreet
        BoroughCode
        ZipCode

        Please let us know if you have any questions or concerns.

        Best,
        Charlotte
        """
        # mailItem.To = 'ywang36@schools.nyc.gov'
        # mailItem.CC = 'ywang36@schools.nyc.gov'
        # Recipients
        mailItem.To = 'Alvarez Steven <SAlvarez27@schools.nyc.gov>; Hall James <JHall@schools.nyc.gov>; Yu Peng <PYu3@schools.nyc.gov>'
        mailItem.CC = 'Hermitt Ariel <AHermitt@schools.nyc.gov>; Rajyalakshmi Munnangi <rmunnangi@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>; \
            Joshi Manasi <MJoshi5@schools.nyc.gov>; Boompagh Prem Wilfred <PBoompagh@schools.nyc.gov>; Agwu Christopher <CAgwu2@schools.nyc.gov>; \
            Deshpande Vaishali <VDeshpande2@schools.nyc.gov>; Gavryushenko Sergey <SGavryushenko@schools.nyc.gov>; Pasam Pratap Vardhan <PPasam@schools.nyc.gov>'
        mailItem.Attachments.Add(rf"R:\SEO Analytics\Share\Turning 5\SourceFiles\T5WaveEligibleStudents\{self.thisweek}LCGMSGeocodingandZoningRequest.xlsx",)
        mailItem.Attachments.Add(r"R:\SEO Analytics\Share\Turning 5\SourceFiles\Student Zoning File\Template\Zoned.YYYYMMDDSS_LCGMSGeocodingandZoningRequest.csv.csv")
        mailItem.Attachments.Add(r"R:\SEO Analytics\Share\Turning 5\SourceFiles\Student Zoning File\Template\YYYYMMDDSS_GBATErr.txt.txt")
        mailItem.Display()

        mailItem.Save()
        mailItem.Send()
        print(f"{self.thisweek} Email sent successfully.")

    # Email preparation
    def prepare_and_send_email_Chris(self,issues):
        # construct Outlook application instance
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        # construct the email item object
        mailItem = olApp.CreateItem(0)
        mailItem.Subject = "T5 ZONED SCHOOL REQUEST (Pre Wave Test 4) Validation issues found"
        mailItem.BodyFormat = 1
        mailItem.Body = f"""
        Hope all is well! Please see the latest LCGMS Geocoding and Zoning file request.

        Attached are the validation reports for the following issues:
        """
        for check in issues.keys():
            mailItem.Body += f"\n- {check} validation found discrepancies."
            # Save discrepancy reports
            issues[check].to_excel(f"R:\\SEO Analytics\\Share\\Turning 5\\SourceFiles\\Discrepancy_{check}.xlsx", index=False)

        mailItem.Body += "\n\nBest regards,\nYour Team"

        # mailItem.To = 'ywang36@schools.nyc.gov'
        # mailItem.CC = 'ywang36@schools.nyc.gov'
        # Email recipients
        mailItem.To = ["CAgwu2@schools.nyc.gov"]
        mailItem.CC = ["PCissthomas@schools.nyc.gov"]

        mailItem.Display()

        mailItem.Save()
        mailItem.Send()


    # Main function
    def main(self):
        self.copy_file_to_archive(rf"R:\SEO Analytics\Share\Turning 5\SourceFiles\T5WaveEligibleStudents\{self.lastweek}LCGMSGeocodingandZoningRequest.xlsx", r"R:\SEO Analytics\Share\Turning 5\SourceFiles\T5WaveEligibleStudents\Archive")
        self.delete_file(rf"R:\SEO Analytics\Share\Turning 5\SourceFiles\T5WaveEligibleStudents\{self.lastweek}LCGMSGeocodingandZoningRequest.xlsx")
        issues = self.validate_data()
        if issues:
            self.prepare_and_send_email_Chris(issues)
            print("Validation issues found and email sent.")
        else:
            print("No validation issues found.")
            self.t5Monday_send_outlook_email()

if __name__ == "__main__":
    T5Automation = Solution()
    T5Automation.main()
