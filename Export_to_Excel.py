import pandas as pd

# Define file paths
stufile = 'R:\\SEO Analytics\\Reporting\\City Council SY22\\Annual Reports'

# Read Excel file
xls = pd.ExcelFile(stufile + '\\your_input_filename.xlsx')

# Extract data from Excel into dataframes (for example)
ini_dist = xls.parse('Initials', usecols="C:L", skiprows=4, nrows=32)
ini_eth = xls.parse('Initials', usecols="C:L", skiprows=40, nrows=5)
#... so on for other ranges

# Process data if necessary
#...

# Output to new Excel file
with pd.ExcelWriter(stufile + '\\your_output_filename.xlsx') as writer:
    ini_dist.to_excel(writer, sheet_name='Initials', startrow=4, startcol=2, index=False)
    ini_eth.to_excel(writer, sheet_name='Initials', startrow=40, startcol=2, index=False)
    #... so on for other dataframes
