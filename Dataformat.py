import openpyxl
def print_cell_formats(file_name, sheet_name, cell_range):
    wb = openpyxl.load_workbook(file_name)
    ws = wb[sheet_name]
    for row in ws[cell_range]:
        for cell in row:
            print(f"Cell {cell.coordinate} - Value: {cell.value} - Type: {type(cell.value)} - Format: {cell.number_format}")

# Example usage
# print_cell_formats(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Non-Redacted Annual Special Education Data Report SY24.xlsx', 'Reports 5-7 = Reevaluations', 'C5:M37')
# print_cell_formats(r'R:\SEO Analytics\Reporting\City Council\City Council SY23\Annual Reports\Non-Redacted Annual Special Education Data Report SY23.xlsx', 'Reports 5-7 = Reevaluations', 'C5:M37')
# print_cell_formats(r'R:\SEO Analytics\Reporting\City Council\City Council SY23\Annual Reports\Non-Redacted Annual Special Education Data Report SY23.xlsx', 'Report 14 = Programs', 'C5:H8') #Type: <class 'int'> - Format: #,##0 Cell H8 - Value: 0.016029519591 - Type: <class 'float'> - Format: 0%
# print_cell_formats(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Non-Redacted Annual Special Education Data Report SY24.xlsx', 'Report 14 = Programs', 'C5:H8') #Type: <class 'str'> - Format: General
# print_cell_formats(r'R:\SEO Analytics\Reporting\City Council\City Council SY23\Annual Reports\Non-Redacted Annual Special Education Data Report SY23.xlsx', 'Report 11 = Placement', 'C5:H8') #Type: <class 'int'> - Format: #,##0 Cell H8 - Value: 0.016029519591 - Type: <class 'float'> - Format: 0%
# print_cell_formats(r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\Non-Redacted City Council Triennial Report_CW.xlsx', 'Program Delivery by District', 'C3:H99') # Type: <class 'str'> - Format: General
print_cell_formats(r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\Nonredacted School-Age Special Education Data Report 10.31.23.xlsx', 'Program Delivery by District', 'C3:H99') # Type: <class 'int'> - Format: General Type: <class 'float'> - Format: 0%


# what is the format of 100% in cell? 
