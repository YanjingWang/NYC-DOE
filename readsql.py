import pandas as pd
import pyodbc

# Set up your database connection
conn = pyodbc.connect('DRIVER=SQL SERVER;SERVER=ES00VPADOSQL180,51433;DATABASE=SEO_REPORTING')

# Define the query (use the modified query provided above)
query = """
select * from  (  Select   EthnicityGroupCC_sort as sort , EthnicityGroupCC	,FORMAT(sum(STUDENTS_WITH_REF), '#,##0') as c1     ,FORMAT(sum(CLOSED_WITHOUT_IEP), '#,##0') as c2 	,
FORMAT(sum(INELIGIBLE_LESS_60), '#,##0') as c3     ,FORMAT(sum(INELIGIBLE_MORE_60), '#,##0') as c4 	,
FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0)), '#,##0') as c5     ,FORMAT(sum(CLASSIFIED_LESS_60), '#,##0') as c6     ,
FORMAT(sum(CLASSIFIED_MORE_60), '#,##0') as c7     ,FORMAT(sum(CLASSIFIED_LESS_60 + CLASSIFIED_MORE_60), '#,##0') as c8 	,
FORMAT(sum(COALESCE(INELIGIBLE_LESS_60,0) + COALESCE(INELIGIBLE_MORE_60,0) + COALESCE(CLASSIFIED_LESS_60,0) + COALESCE(CLASSIFIED_MORE_60,0)), '#,##0') as c9 	,FORMAT(sum(TOTAL_AWAITING), '#,##0') as c10			,
FORMAT(sum(TOTAL_OPEN), '#,##0') as c11  FROM ##Report_Final   group by EthnicityGroupCC, EthnicityGroupCC_sort ) a  union all  select * from ##TotalRow_Sort  order by sort 
"""

# Read the query result into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# df now contains your data
# print(df)
df_byRace = df[['EthnicityGroupCC', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11']]
print(df_byRace)