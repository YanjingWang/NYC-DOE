import pandas as pd
import pyodbc

# Establishing the connection to SQL Server
conn_str = "Driver={SQL Server};Server=ES00VPADOSQL180,51433;Database=SEO_REPORTING;Trusted_Connection=yes;"

# Connecting to different schemas within the same server
conn_seo_rep = pyodbc.connect(conn_str, schema='dbo')
conn_seo_snap = pyodbc.connect(conn_str, schema='snap')
conn_seo_mart = pyodbc.connect(conn_str, schema='dbo')

# Reading from the SQL Server into pandas DataFrame
query = """
SELECT a.*, 
       CASE WHEN b.studentid IS NOT NULL THEN 'Y' ELSE 'N' END AS FosterCareFlag,
       ...
       LEFT JOIN SEO_Mart.lk_FosterCare b ON a.studentid=b.studentid
       LEFT JOIN SEO_Snap.RPT_StudentRegister_061523 c ON a.studentid=c.studentid;
"""
pre_report = pd.read_sql(query, conn_seo_snap)

# More transformations with pre_report
...

# Creating the report DataFrame
...

# Aggregation function for the macros
def sque(data, byvar):
    return data.groupby(byvar).agg({
        'RSOnly': ['sum', lambda x: x.sum() / len(data)],
        ...
    })

reporta = sque(report, 'ReportingDistrict')
report2a = sque(report, 'MealStatusGrouping')
...

# Additional functions for que_srt and part1
...

# Closing the connections
conn_seo_rep.close()
conn_seo_snap.close()
conn_seo_mart.close()
