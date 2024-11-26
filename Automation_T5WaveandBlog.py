import os
import pandas as pd
import pyodbc
from datetime import datetime
class Automation_T5WaveandBlog:
    def __init__(self):
        # Current date
        self.today = datetime.today()
        self.formatted_date = self.today.strftime("%m-%d-%Y")
        self.current_date = self.today.strftime("%Y-%m-%d")  # For SQL comparison
    # Database connection setup
    def create_db_connection(self):
        conn_str = (
            "DRIVER=SQL Server;"
            "SERVER=ES00VPADOSQL180,51433;"  # Replace with your server name
            "DATABASE=SEO_MART;"
            "Trusted_Connection=yes;"
        )
        return pyodbc.connect(conn_str)

    # Fetch Wave Date from INT_T5WaveSchedule table
    def is_wave_date(self, conn, current_date):
        query = """
            SELECT WaveDate 
            FROM SEO_MART.dbo.INT_T5WaveSchedule
            WHERE CAST(WaveDate AS DATE) = ?
        """
        cursor = conn.cursor()
        cursor.execute(query, current_date)
        result = cursor.fetchone()
        return result is not None

    # Fetch data from SQL query and save as Excel
    def fetch_and_save(self,query, output_file, folder_path):
        conn = self.create_db_connection()
        df = pd.read_sql(query, conn)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        output_path = os.path.join(folder_path, output_file)
        df.to_excel(output_path, index=False)
        print(f"Saved file: {output_path}")
        conn.close()

    def main(self):
        # Paths for saving files
        wave_folder = r"C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\T5\Wave"
        biog_folder = r"C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\T5\Blog"

        # Database connection
        conn = self.create_db_connection()

        # Check if today is a WaveDate
        wave_date = self.is_wave_date(conn, self.current_date)

        # Process WAVE File
        if wave_date:
            wave_query = "SELECT * FROM SEO_REPORTING.BI.vw_T5Report_WAVE"
            wave_output_file = f"(TEST - CAP) T5 WAVE File SY25 - {self.formatted_date}.xlsx"
            self.fetch_and_save(wave_query, wave_output_file, wave_folder)

        # Process BIOG File
        if wave_date:
            biog_query = "SELECT * FROM SEO_REPORTING.BI.vw_T5Report_BIOG"
        else:
            biog_query = "SELECT * FROM SEO_REPORTING.BI.vw_T5Report_BIOG_noWave"
        biog_output_file = f"(TEST - CAP) T5 BIOG File SY25 - {self.formatted_date}.xlsx"
        self.fetch_and_save(biog_query, biog_output_file, biog_folder)

        conn.close()

if __name__ == "__main__":
    obj = Automation_T5WaveandBlog()
    obj.main()
