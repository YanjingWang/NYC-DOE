# City Council triennial non-redacted report generation

This guidance will help you understand how to run the provided Python script, which creates and formats an Excel report by connecting to a SQL Server database, fetching data, and writing it into an Excel template.

Order to run:

Report_Program_Delivery.py

Report_Program_Delivery_by_District.py

Report_Program_Delivery_by_Supt.py

Report_Program_Delivery_by_School.py

Report_Related_Service_Delivery.py

Report_RS_Delivery_by_District.py

Report_Program_Delivery_by_Supt.py

Report_RS_Delivery_by_School.py

Report_Transportation_by_District.py

Report_Transportatiion_by_School.py

## Prerequisites:

* **Python Environment** : Ensure you have Python installed. This script is compatible with Python 3.x.
* **Required Libraries** : The script uses the following libraries:
* `openpyxl`: For working with Excel files.
* `pandas`: (Imported but not used in the provided script, so it's not required for execution)
* `pyodbc`: For connecting to a SQL Server database.

  Install the necessary libraries using pip:

```
pip install openpyxl pyodbc
```

* **Database Access** : Ensure you have access to the SQL Server database (`SEO_MART`) and the required stored procedure (`USPCCTriannualReportPSSchoolLevel`) that fetches the data.
* **Excel Template** : The script expects an Excel template at `C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\Non-Redacted City Council Triennial Report_CW.xlsx`. Ensure this file exists or modify the script to point to the correct file path.
* **File Paths** : Adjust file paths if necessary to reflect your local file structure.

## Steps to Run the Script:

### * **Setup the Script** :

* Open a text editor or an IDE (such as VSCode, PyCharm) and copy the provided code into a Python file. Name the file `main_program_delivery.py`.

### * **Modify Parameters** :

* The script is designed with a `lastrow, datestamp` and `date` parameters. These are set to   `4042, "06152024"` and `"June 15, 2024"`, respectively. Adjust these parameters in the `__init__` method of the `Solution` class if needed.

### * **Run the Script** :

* Open a terminal or command prompt.
* Navigate to the directory where your `main_program_delivery.py` is located.
* Run the script using the command

  ```
  python Report_Program_Delivery_by_School.py
  ```
* ### **Expected Output** :
* The script will connect to the SQL Server database and execute the stored procedure to fetch data.
* It will then create an Excel report with the title `"Program Delivery by School"` on a new worksheet.
* The data fetched from the database will be written to this worksheet, formatted according to the script's logic.
* The final Excel file will be saved at `C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\Non-Redacted City Council Triennial Report_CW.xlsx`.
* ### **Closing the Connection** :
* The script will close the database connection after processing.
* Check lastrow in report and adjust the number in code if lastrow changes and delete the tab with wrong lastrow in excel report and rerun it after adjust `lastrow`
* After `lastrow` is correct for all tabs, close excel report and rename it as `Non-Redacted City Council Triennial Report_MMDDYYYY.xlsx` and copy it to R:\SEO Analytics\Reporting\City Council\City Council SY24\MM.DD.YY Triannual Report
