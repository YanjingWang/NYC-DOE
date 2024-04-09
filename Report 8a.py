import pandas as pd
import pyodbc

# Setting up SQL connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ES00VPADOSQL180,51433;DATABASE=SEO_MART;Trusted_Connection=Yes;')

# Defining the SQL statement
sql = """
IF OBJECT_ID('tempdb..#CCTotaltemp') IS NOT NULL
    DROP TABLE #CCTotaltemp;
-- ... rest of the SQL code ...
select * from #CCTotaltemp;
"""

# Reading the SQL result into a pandas DataFrame
df_report = pd.read_sql(sql, conn)

# Data manipulation
# ... replicate the manipulations done in the SAS code, using pandas ...

# Using pandas for group by operations
def group_and_sum(df, by_vars):
    cols_to_sum = ['Autism', 'Deaf_Blind', ...]  # Specify the columns to sum up
    return df.groupby(by_vars)[cols_to_sum].sum().reset_index()

R8aDist = group_and_sum(df_report, ['ReportingDistrict'])
R8aMeal = group_and_sum(df_report, ['MealStatusGrouping'])
# ... repeat for the other group by operations ...

# Part1 macro equivalent in Python
def part1(df, by_var):
    # Data manipulations to replicate the logic in the macro
    df_by_var_not_missing = df.dropna(subset=[by_var])
    sum_df = df_by_var_not_missing.sum()
    total_df = df_by_var_not_missing.append(sum_df, ignore_index=True)
    total_df[by_var].fillna("Total", inplace=True)
    total_df['c14'] = total_df[['c1', 'c2', 'c3', ...]].sum(axis=1)  # Include all the columns to sum
    return total_df

Reg2Dist = part1(R8aDist, 'ReportingDistrict')
# Reg2Eth = part1(R8aEth, 'EthnicityGroupCC')
# ... repeat for the other 'part1' operations ...
