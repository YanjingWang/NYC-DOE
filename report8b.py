import openpyxl
from openpyxl.styles import Font, Border, Side, Alignment, PatternFill, colors
from openpyxl.utils import get_column_letter
import pyodbc
class Solution:
    # Existing code...
    # Function to format headers
    def get_column_index_from_string(self, column_letter):
        return openpyxl.utils.column_index_from_string(column_letter)
    def format_header(self,ws, header_start_cell, header_title, columns, column_letters, row_height, header_fill_color, column_fill_color, border_style, font_style):
        # Set title, font, border, alignment, fill, row dimensions, and merge cells for the main header
        ws[header_start_cell] = header_title
        ws[header_start_cell].font = font_style
        ws[header_start_cell].border = border_style
        ws[header_start_cell].alignment = Alignment(horizontal='center', vertical='center')  
        ws[header_start_cell].fill = PatternFill(start_color=header_fill_color, end_color=header_fill_color, fill_type="solid")
        ws.row_dimensions[int(header_start_cell[1:])].height = row_height
        # ws.merge_cells(header_start_cell + ':' + chr(ord(column_letters[-1]) + 1) + str(int(header_start_cell[1:])+1))
        # Merge the header_start_cell with the cell directly below it
        ws.merge_cells(start_row=ws[header_start_cell].row,
                    start_column=ws[header_start_cell].column,
                    end_row=ws[header_start_cell].row + 1,
                    end_column=ws[header_start_cell].column)

        print('headercell:'+header_start_cell)
        print('mergecell:'+ header_start_cell + ':' +str(int(header_start_cell[1:])+1))
        
        # Apply formatting to the sub headers
        for col, title in zip(column_letters, columns):
            cell_number = str(int(header_start_cell[1:])) #don't +3 here
            ws[col + cell_number] = title
            ws[col + cell_number].font = font_style
            ws[col + cell_number].border = border_style
            ws[col + cell_number].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            ws[col + cell_number].fill = PatternFill(start_color=column_fill_color, end_color=column_fill_color, fill_type="solid")
            ws[col + str(int(cell_number)+1)] = '#'
            ws[col + str(int(cell_number)+1)].font = font_style
            ws[col + str(int(cell_number)+1)].border = border_style
            ws[col + str(int(cell_number)+1)].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True) 
            ws[col + str(int(cell_number)+1)].fill = PatternFill(start_color=column_fill_color, end_color=column_fill_color, fill_type="solid")
            ws[chr(ord(col) + 1) + str(int(cell_number)+1)] = '%'
            ws[chr(ord(col) + 1) + str(int(cell_number)+1)].font = font_style
            ws[chr(ord(col) + 1) + str(int(cell_number)+1)].border = border_style
            ws[chr(ord(col) + 1) + str(int(cell_number)+1)].alignment = Alignment(horizontal='center', vertical='center')
            ws[chr(ord(col) + 1) + str(int(cell_number)+1)].fill = PatternFill(start_color=column_fill_color, end_color=column_fill_color, fill_type="solid")
            # Merge header cells for '%' and '#' under each main column
            ws.merge_cells(col + cell_number + ':' + chr(ord(col) + 1) + cell_number)
            print('col: '+col)
            print('col+cell_number: '+col + cell_number) 
            print('#: '+ col + str(int(cell_number)+1))
            print('%: '+chr(ord(col) + 1) + str(int(cell_number)+1))
            print('Sub mergecell:'+ col + cell_number + ':' + chr(ord(col) + 1) + cell_number)

        # Apply borders to all the cells in the header
        for col in [header_start_cell[0]] + column_letters + [chr(ord(c) + 1) for c in column_letters]:
            ws[col + cell_number].border = border_style
            ws[col + str(int(cell_number)+1)].border = border_style



    # Create Excel Report Template
    def create_excel_report_template(self, title_cells, subtitle_cells, column_widths):
        # wb = openpyxl.Workbook()
        # ws = wb.active
        # ws.title = "Report 8b = IEP Service Recs"
        wb = openpyxl.load_workbook(r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\Non-Redacted Annual Special Education Data Report.xlsx')
        ws = wb.create_sheet("Report 8b = IEP Service Recs")


        # Set fill color for cells from A1 to Zn to white
        white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
        for row in ws.iter_rows(min_row=1, max_row=120, min_col=1, max_col=26):
            for cell in row:
                cell.fill = white_fill

        black_border, black_border_thick, _, _ = self.create_border_styles()

        # Add report title and merge cells
        for cell_info in title_cells:
            cell = ws[cell_info["cell"]]
            cell.value = cell_info["value"]
            ws.merge_cells(cell_info["merge_cells"])  # Merge cells outside the loop
            cell.border = black_border

        for cell_info in subtitle_cells:
            cell = ws[cell_info["cell"]]
            cell.value = cell_info["value"]
            ws.merge_cells(cell_info["merge_cells"])  # Merge cells outside the loop
            cell.border = black_border_thick

        # Style and align the merged title and subtitle
        for cell_info in title_cells + subtitle_cells:
            cell = ws[cell_info["cell"]]
            cell.font = Font(bold=True, size=12)
            cell.alignment = Alignment(wrap_text=True)

        # Adjust column widths
        for col, width in enumerate(column_widths, start=1):
            column_letter = get_column_letter(col)
            ws.column_dimensions[column_letter].width = width

        # Call the header formatting function for each header section
        columns = ['Related services only', 'Special Education Teacher Support Services (SETSS)',
                'Integrated Co-Teaching Services', 'Integrated Co-Teaching Services', 'Special Class in a Community School', 
                'Special Class in a District 75 school', 'Special Class in a Non-public School Placement']
        column_letters = ['C', 'E', 'G', 'I', 'K', 'M']
        # You need to pass the correct parameters to the format_header function
        # For example, for the 'District' header starting at row 4
        # ... You would repeat the above line for each section (Ethnicity, Meal Status, Gender) with the appropriate start_row
        # Define the styles outside of the function calls to avoid recreation every time
        header_font = Font(bold=True, size=12)
        border_bottom_thin = Border(bottom=Side(style='thin'))
        header_fill_color = "B8CCE4"
        column_fill_color = "E0F0F8"
        self.format_header(ws, 'B4', 'District', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B41', 'Ethnicity', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B51', 'Meal Status', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B58', 'Gender', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B66', 'ELL Status', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B73', 'Language of Instruction', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B84', 'Grade Level', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B103', 'Temporary Housing Status', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)
        self.format_header(ws, 'B111', 'Foster Care Status', columns, column_letters, 30, header_fill_color, column_fill_color, border_bottom_thin, header_font)

        
        # Deleting the default created sheet
        if "Sheet" in wb.sheetnames:
            del wb["Sheet"]

        return wb, ws



    def create_border_styles(self):
        black_border_side = Side(style='thin', color='000000')
        black_border_thickside = Side(style='thick', color='000000')

        black_border = Border(top=black_border_side, left=black_border_side, right=black_border_side, bottom=black_border_side)
        black_border_thick = Border(top=black_border_thickside, left=black_border_thickside, right=black_border_thickside, bottom=black_border_thickside)
        black_border_no_bottom = Border(left=black_border_thickside, right=black_border_thickside)
        black_boarder_all = Border(top=black_border_thickside, left=black_border_thickside, right=black_border_thickside, bottom=black_border_thickside)

        return black_border, black_border_thick, black_border_no_bottom, black_boarder_all

    # Step 2: Connect to the database
    def connect_to_database(self):
        conn_str = 'DRIVER=SQL SERVER;SERVER=ES00VPADOSQL180,51433;DATABASE=SEO_REPORTING' #;UID=your_username;PWD=your_password
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        params = ('CC_StudentRegisterR814_0615', 'RPT_StudentRegister_0615')
        cursor.execute("EXEC [dev].[USPCCAnnaulReport8b] @tableNameCCStudentRegisterR814=?, @tableNameRptStudentRegister0615=?", params)
        return cursor
    # Fetch data for "Report 8b = IEP Service Recs by Race"
    def fetch_data_by_race(self,cursor):
        query_byRace = '''
        WITH CTE_byRace AS (
        SELECT EthnicityGroupCC, 
            FORMAT(sum(RSOnly), '#,##0') as c1,
            CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2 ,
            FORMAT(sum(SETSS), '#,##0') as c3 ,
            CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4 ,
            FORMAT(sum(ICT), '#,##0') as c5 ,
            CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6 ,
            FORMAT(sum(SpecialClass), '#,##0') as c7 ,
            CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8 ,
            FORMAT(sum(SpecialClassD75), '#,##0') as c9 ,
            CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10 ,
            FORMAT(sum(SpecialClassNPS), '#,##0') as c11 ,
            CONCAT(CAST((SUM(SpecialClassNPS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c12,
            EthnicityGroupCC_sort -- Add this column here
        FROM ##Report 
        GROUP BY EthnicityGroupCC, EthnicityGroupCC_sort -- Group by this column as well

        UNION ALL

        SELECT 'Total' as EthnicityGroupCC,
            FORMAT(SUM(RSOnly), '#,##0') as c1,
            CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2 ,
            FORMAT(sum(SETSS), '#,##0') as c3 ,
            CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4 ,
            FORMAT(sum(ICT), '#,##0') as c5 ,
            CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6 ,
            FORMAT(sum(SpecialClass), '#,##0') as c7 ,
            CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8 ,
            FORMAT(sum(SpecialClassD75), '#,##0') as c9 ,
            CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10 ,
            FORMAT(sum(SpecialClassNPS), '#,##0') as c11 ,
            CONCAT(CAST((SUM(SpecialClassNPS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c12,
            6 as EthnicityGroupCC_sort -- This is for the 'Total' row, you can use NULL or any suitable placeholder
        FROM ##Report 

        --ORDER BY EthnicityGroupCC_sort -- Now, you can order by this column
        )
        SELECT EthnicityGroupCC,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12 FROM CTE_byRace
        ORDER BY EthnicityGroupCC_sort
        '''  # the byRace SQL query goes here
        cursor.execute(query_byRace)
        results_byRace = cursor.fetchall()
        return results_byRace

    # Fetch data for "Report 8b = IEP Service Recs by District"
    def fetch_data_by_district(self,cursor):
        query_byDistrict = '''
        Select  ReportingDistrict,FORMAT(sum(RSOnly), '#,##0') as c1 ,
        CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2 ,
        FORMAT(sum(SETSS), '#,##0') as c3 ,CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4 ,
        FORMAT(sum(ICT), '#,##0') as c5 ,CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6 ,
        FORMAT(sum(SpecialClass), '#,##0') as c7 ,
        CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8 ,FORMAT(sum(SpecialClassD75), '#,##0') as c9 ,
        CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10 ,FORMAT(sum(SpecialClassNPS), '#,##0') as c11 ,
        CONCAT(cast((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c12  FROM ##Report group by ReportingDistrict 
        UNION ALL  SELECT 'Total' as ReportingDistrict, FORMAT(SUM(RSOnly), '#,##0') as c1 , 
        CONCAT(CAST((SUM(RSOnly)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c2 , 
        FORMAT(SUM(SETSS), '#,##0') as c3 , CONCAT(CAST((SUM(SETSS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c4 , 
        FORMAT(SUM(ICT), '#,##0') as c5 , CONCAT(CAST((SUM(ICT)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c6 , FORMAT(SUM(SpecialClass), '#,##0') as c7 , 
        CONCAT(CAST((SUM(SpecialClass)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c8 , FORMAT(SUM(SpecialClassD75), '#,##0') as c9 , 
        CONCAT(CAST((SUM(SpecialClassD75)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c10 , FORMAT(SUM(SpecialClassNPS), '#,##0') as c11 , 
        CONCAT(CAST((SUM(SpecialClassNPS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c12 FROM ##Report order by ReportingDistrict
        '''  # the byDistrict SQL query goes here
        cursor.execute(query_byDistrict)
        results_byDistrict = cursor.fetchall()
        return results_byDistrict

    def fetch_data_by_mealstatus(self,cursor):
        query_byMealStatus = '''
        Select  MealStatusGrouping,FORMAT(sum(RSOnly), '#,##0') as c1 ,CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2 ,
        FORMAT(sum(SETSS), '#,##0') as c3 ,CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4 ,
        FORMAT(sum(ICT), '#,##0') as c5 ,CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6 ,
        FORMAT(sum(SpecialClass), '#,##0') as c7 ,CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8 ,
        FORMAT(sum(SpecialClassD75), '#,##0') as c9 ,CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10 ,
        FORMAT(sum(SpecialClassNPS), '#,##0') as c11 ,CONCAT(cast((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c12  FROM ##Report 
        group by MealStatusGrouping UNION ALL  SELECT 'Total' as MealStatusGrouping, FORMAT(SUM(RSOnly), '#,##0') as c1 , CONCAT(CAST((SUM(RSOnly)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c2 , 
        FORMAT(SUM(SETSS), '#,##0') as c3 , CONCAT(CAST((SUM(SETSS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c4 , 
        FORMAT(SUM(ICT), '#,##0') as c5 , CONCAT(CAST((SUM(ICT)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c6 , 
        FORMAT(SUM(SpecialClass), '#,##0') as c7 , CONCAT(CAST((SUM(SpecialClass)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c8 , 
        FORMAT(SUM(SpecialClassD75), '#,##0') as c9 , CONCAT(CAST((SUM(SpecialClassD75)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c10 , 
        FORMAT(SUM(SpecialClassNPS), '#,##0') as c11 , CONCAT(CAST((SUM(SpecialClassNPS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c12 FROM ##Report order by MealStatusGrouping
        '''  # the byMealStatus SQL query goes here
        cursor.execute(query_byMealStatus)
        results_byMealStatus = cursor.fetchall()
        return results_byMealStatus
    
    def fetch_data_by_gender(self,cursor):
        query_byGender = '''
        Select  Gender,FORMAT(sum(RSOnly), '#,##0') as c1 ,CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2 ,
        FORMAT(sum(SETSS), '#,##0') as c3 ,CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4 ,
        FORMAT(sum(ICT), '#,##0') as c5 ,CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6 ,
        FORMAT(sum(SpecialClass), '#,##0') as c7 ,CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8 ,
        FORMAT(sum(SpecialClassD75), '#,##0') as c9 ,CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10 ,
        FORMAT(sum(SpecialClassNPS), '#,##0') as c11 ,CONCAT(cast((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c12  
        FROM ##Report group by Gender UNION ALL  SELECT 'Total' as Gender, FORMAT(SUM(RSOnly), '#,##0') as c1 , CONCAT(CAST((SUM(RSOnly)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c2 , 
        FORMAT(SUM(SETSS), '#,##0') as c3 , CONCAT(CAST((SUM(SETSS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c4 , 
        FORMAT(SUM(ICT), '#,##0') as c5 , CONCAT(CAST((SUM(ICT)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c6 , 
        FORMAT(SUM(SpecialClass), '#,##0') as c7 , CONCAT(CAST((SUM(SpecialClass)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c8 , 
        FORMAT(SUM(SpecialClassD75), '#,##0') as c9 , CONCAT(CAST((SUM(SpecialClassD75)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c10 , 
        FORMAT(SUM(SpecialClassNPS), '#,##0') as c11 , CONCAT(CAST((SUM(SpecialClassNPS)*100.0)/(SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c12 FROM ##Report order by Gender
        '''  # the byGender SQL query goes here
        cursor.execute(query_byGender)
        results_byGender = cursor.fetchall()
        return results_byGender
    
    def fetch_data_by_ellstatus(self,cursor):
        query_byELLStatus = '''
        Select 
            ELLStatus,
            FORMAT(sum(RSOnly), '#,##0') as c1,
            CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2,
            FORMAT(sum(SETSS), '#,##0') as c3,
            CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4,
            FORMAT(sum(ICT), '#,##0') as c5,
            CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6,
            FORMAT(sum(SpecialClass), '#,##0') as c7,
            CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8,
            FORMAT(sum(SpecialClassD75), '#,##0') as c9,
            CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10,
            FORMAT(sum(SpecialClassNPS), '#,##0') as c11,
            CONCAT(cast((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c12
        FROM ##Report 
        GROUP BY ELLStatus

        UNION ALL

        Select 
            'Total' as ELLStatus,
            FORMAT(sum(RSOnly), '#,##0') as c1,
            CONCAT(cast((sum(RSOnly)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c2,
            FORMAT(sum(SETSS), '#,##0') as c3,
            CONCAT(cast((sum(SETSS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c4,
            FORMAT(sum(ICT), '#,##0') as c5,
            CONCAT(cast((sum(ICT)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c6,
            FORMAT(sum(SpecialClass), '#,##0') as c7,
            CONCAT(cast((sum(SpecialClass)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c8,
            FORMAT(sum(SpecialClassD75), '#,##0') as c9,
            CONCAT(cast((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c10,
            FORMAT(sum(SpecialClassNPS), '#,##0') as c11,
            CONCAT(cast((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report) as numeric(7,1)), '%') as c12
        FROM ##Report 

        ORDER BY ELLStatus -- This will put the 'Total' row at the bottom if 'Total' is the last alphabetically.
        '''  # the byELLStatus SQL query goes here
        cursor.execute(query_byELLStatus)
        results_byELLStatus = cursor.fetchall()
        return results_byELLStatus
    
    def fetch_data_by_language(self,cursor):
        query_byLanguage = '''
        Select 
            LanguageOfInstructionCC2,
            FORMAT(sum(RSOnly), '#,##0') as c1,
            CONCAT(FORMAT((sum(RSOnly)*100.0)/(select count(*) from ##Report), '0.0'), '%') as c2,
            FORMAT(sum(SETSS), '#,##0') as c3,
            CONCAT(FORMAT((sum(SETSS)*100.0)/(select count(*) from ##Report), '0.0'), '%') as c4,
            FORMAT(sum(ICT), '#,##0') as c5,
            CONCAT(FORMAT((sum(ICT)*100.0)/(select count(*) from ##Report), '0.0'), '%') as c6,
            FORMAT(sum(SpecialClass), '#,##0') as c7,
            CONCAT(FORMAT((sum(SpecialClass)*100.0)/(select count(*) from ##Report), '0.0'), '%') as c8,
            FORMAT(sum(SpecialClassD75), '#,##0') as c9,
            CONCAT(FORMAT((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report), '0.0'), '%') as c10,
            FORMAT(sum(SpecialClassNPS), '#,##0') as c11,
            CONCAT(FORMAT((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report), '0.0'), '%') as c12
        FROM ##Report
        GROUP BY LanguageOfInstructionCC2, Language_Sort

        UNION ALL

        Select 
            'Total' as LanguageOfInstructionCC2,
            FORMAT(sum(RSOnly), '#,##0'),
            CONCAT(FORMAT((sum(RSOnly)*100.0)/(select count(*) from ##Report), '0.0'), '%'),
            FORMAT(sum(SETSS), '#,##0'),
            CONCAT(FORMAT((sum(SETSS)*100.0)/(select count(*) from ##Report), '0.0'), '%'),
            FORMAT(sum(ICT), '#,##0'),
            CONCAT(FORMAT((sum(ICT)*100.0)/(select count(*) from ##Report), '0.0'), '%'),
            FORMAT(sum(SpecialClass), '#,##0'),
            CONCAT(FORMAT((sum(SpecialClass)*100.0)/(select count(*) from ##Report), '0.0'), '%'),
            FORMAT(sum(SpecialClassD75), '#,##0'),
            CONCAT(FORMAT((sum(SpecialClassD75)*100.0)/(select count(*) from ##Report), '0.0'), '%'),
            FORMAT(sum(SpecialClassNPS), '#,##0'),
            CONCAT(FORMAT((sum(SpecialClassNPS)*100.0)/(select count(*) from ##Report), '0.0'), '%')
        FROM ##Report
        --ORDER BY Language_Sort

        '''  # the byLanguage SQL query goes here
        cursor.execute(query_byLanguage)
        results_byLanguage = cursor.fetchall()
        return results_byLanguage
    
    def fetch_data_by_gradelevel(self,cursor):
        query_byGradeLevel = '''
        WITH CTE AS (
        SELECT 
            GradeLevel,
            FORMAT(SUM(RSOnly), '#,##0') as c1,
            CONCAT(FORMAT(SUM(RSOnly) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c2,
            FORMAT(SUM(SETSS), '#,##0') as c3,
            CONCAT(FORMAT(SUM(SETSS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c4,
            FORMAT(SUM(ICT), '#,##0') as c5,
            CONCAT(FORMAT(SUM(ICT) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c6,
            FORMAT(SUM(SpecialClass), '#,##0') as c7,
            CONCAT(FORMAT(SUM(SpecialClass) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c8,
            FORMAT(SUM(SpecialClassD75), '#,##0') as c9,
            CONCAT(FORMAT(SUM(SpecialClassD75) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c10,
            FORMAT(SUM(SpecialClassNPS), '#,##0') as c11,
            CONCAT(FORMAT(SUM(SpecialClassNPS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c12,
            GradeLevel_Sort
        FROM ##Report
        GROUP BY GradeLevel, GradeLevel_Sort

        UNION ALL

        SELECT 
            'Total' as GradeLevel,
            FORMAT(SUM(RSOnly), '#,##0'),
            CONCAT(FORMAT(SUM(RSOnly) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SETSS), '#,##0'),
            CONCAT(FORMAT(SUM(SETSS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(ICT), '#,##0'),
            CONCAT(FORMAT(SUM(ICT) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SpecialClass), '#,##0'),
            CONCAT(FORMAT(SUM(SpecialClass) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SpecialClassD75), '#,##0'),
            CONCAT(FORMAT(SUM(SpecialClassD75) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SpecialClassNPS), '#,##0'),
            CONCAT(FORMAT(SUM(SpecialClassNPS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            999999 as GradeLevel_Sort -- Assign a high number to ensure 'Total' sorts last
        FROM ##Report

        --ORDER BY GradeLevel_Sort
        )
        SELECT GradeLevel,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12 FROM CTE
        ORDER BY GradeLevel
        '''
        cursor.execute(query_byGradeLevel)
        results_byGradeLevel = cursor.fetchall()
        return results_byGradeLevel
    
    def fetch_data_by_tempResFlag(self,cursor):
        query_byTempResFlag = '''
        SELECT 
            TempResFlag,
            FORMAT(SUM(RSOnly), '#,##0') as c1,
            CONCAT(FORMAT(SUM(RSOnly) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c2,
            FORMAT(SUM(SETSS), '#,##0') as c3,
            CONCAT(FORMAT(SUM(SETSS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c4,
            FORMAT(SUM(ICT), '#,##0') as c5,
            CONCAT(FORMAT(SUM(ICT) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c6,
            FORMAT(SUM(SpecialClass), '#,##0') as c7,
            CONCAT(FORMAT(SUM(SpecialClass) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c8,
            FORMAT(SUM(SpecialClassD75), '#,##0') as c9,
            CONCAT(FORMAT(SUM(SpecialClassD75) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c10,
            FORMAT(SUM(SpecialClassNPS), '#,##0') as c11,
            CONCAT(FORMAT(SUM(SpecialClassNPS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%') as c12
        FROM ##Report
        GROUP BY TempResFlag

        UNION ALL

        SELECT 
            'Total',
            FORMAT(SUM(RSOnly), '#,##0'),
            CONCAT(FORMAT(SUM(RSOnly) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SETSS), '#,##0'),
            CONCAT(FORMAT(SUM(SETSS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(ICT), '#,##0'),
            CONCAT(FORMAT(SUM(ICT) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SpecialClass), '#,##0'),
            CONCAT(FORMAT(SUM(SpecialClass) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SpecialClassD75), '#,##0'),
            CONCAT(FORMAT(SUM(SpecialClassD75) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%'),
            FORMAT(SUM(SpecialClassNPS), '#,##0'),
            CONCAT(FORMAT(SUM(SpecialClassNPS) * 100.0 / (SELECT COUNT(*) FROM ##Report), '0.0'), '%')
        FROM ##Report

        '''
        cursor.execute(query_byTempResFlag)
        results_byTempResFlag = cursor.fetchall()
        return results_byTempResFlag
    
    def fetch_data_by_fosterCareStatus(self,cursor):
        query_byFosterCareStatus = '''
        WITH CTE AS(
        SELECT 
            FostercareFlag,
            FORMAT(SUM(RSOnly), '#,##0') as c1,
            CONCAT(CAST((SUM(RSOnly)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c2,
            FORMAT(SUM(SETSS), '#,##0') as c3,
            CONCAT(CAST((SUM(SETSS)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c4,
            FORMAT(SUM(ICT), '#,##0') as c5,
            CONCAT(CAST((SUM(ICT)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c6,
            FORMAT(SUM(SpecialClass), '#,##0') as c7,
            CONCAT(CAST((SUM(SpecialClass)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c8,
            FORMAT(SUM(SpecialClassD75), '#,##0') as c9,
            CONCAT(CAST((SUM(SpecialClassD75)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c10,
            FORMAT(SUM(SpecialClassNPS), '#,##0') as c11,
            CONCAT(CAST((SUM(SpecialClassNPS)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%') as c12,
            FosterCareFlagSort
        FROM ##Report
        GROUP BY FostercareFlag, FosterCareFlagSort

        UNION ALL

        SELECT 
            'Total' as FostercareFlag,
            FORMAT(SUM(RSOnly), '#,##0'),
            CONCAT(CAST((SUM(RSOnly)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%'),
            FORMAT(SUM(SETSS), '#,##0'),
            CONCAT(CAST((SUM(SETSS)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%'),
            FORMAT(SUM(ICT), '#,##0'),
            CONCAT(CAST((SUM(ICT)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%'),
            FORMAT(SUM(SpecialClass), '#,##0'),
            CONCAT(CAST((SUM(SpecialClass)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%'),
            FORMAT(SUM(SpecialClassD75), '#,##0'),
            CONCAT(CAST((SUM(SpecialClassD75)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%'),
            FORMAT(SUM(SpecialClassNPS), '#,##0'),
            CONCAT(CAST((SUM(SpecialClassNPS)*100.0) / (SELECT COUNT(*) FROM ##Report) AS numeric(7,1)), '%'),
            (SELECT MAX(FosterCareFlagSort) FROM ##Report) + 1 as FosterCareFlagSort -- Ensures 'Total' row sorts last
        FROM ##Report

        --ORDER BY FosterCareFlagSort
        )
        SELECT FostercareFlag, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12  FROM CTE 

        '''
        cursor.execute(query_byFosterCareStatus)
        results_byFosterCareStatus = cursor.fetchall()
        return results_byFosterCareStatus
    
    # Step 3: Write data to Excel for "Report 8b = IEP Service Recs by Race"
    def write_data_to_excel(self, ws, data, start_row):
        black_border_side = Side(style='thin', color='000000')
        black_border_thickside = Side(style='thick', color='000000')
        black_border = Border(top=black_border_side, left=black_border_side, right=black_border_side, bottom=black_border_side)
        black_border_thick = Border(top=black_border_thickside, left=black_border_thickside, right=black_border_thickside, bottom=black_border_thickside)
        black_border_no_bottom = Border(left=black_border_thickside, right=black_border_thickside)
        black_boarder_all = Border(top=black_border_thickside, left=black_border_thickside, right=black_border_thickside, bottom=black_border_thickside)
        # Write data to Excel
        for row_num, row_data in enumerate(data, start=start_row):
            # Check if the cell is a merged cell and skip if it is
            if isinstance(ws.cell(row=row_num, column=2), openpyxl.cell.cell.MergedCell):
                continue

            ws.cell(row=row_num, column=2).value = row_data[0]  # Assuming 'B' column is not merged for data rows
            col_pointer = 3  # Start at column 'C'

            for i in range(1, len(row_data), 2):
                # Check for each cell if it's a MergedCell before writing the value
                if not isinstance(ws.cell(row=row_num, column=col_pointer), openpyxl.cell.cell.MergedCell):
                    ws.cell(row=row_num, column=col_pointer).value = row_data[i]  # Number data
                col_pointer += 1

                if not isinstance(ws.cell(row=row_num, column=col_pointer), openpyxl.cell.cell.MergedCell):
                    ws.cell(row=row_num, column=col_pointer).value = row_data[i+1]  # Percentage data
                col_pointer += 1
        
        # Apply borders to all columns
        for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M','N']:
            for row_num in range(start_row, start_row + len(data)):
                ws[col + str(row_num)].border = black_border_no_bottom

        # Update alignment for range C6:N38
        for row in ws['C6':'N38']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C43':'N48']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C53':'N55']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C60':'N63']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C68':'N70']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C75':'N79']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C86':'N99']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C105':'N107']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')

        for row in ws['C113':'N115']:
            for cell in row:
                if cell.value is not None:  # Ensure there is a value in the cell
                    cell.value = str(cell.value) + ''  # Prepend space to the value
                cell.alignment = openpyxl.styles.Alignment(horizontal='right')
        # # Update alignment for range B6:B38, B43:B48, B53:B55, B60:B63, B68:B70, B75:B80, B86:B99, B105:B107, B113:B115
        # for row in ws['B6':'B38']:
        #     for cell in row:
        #         if cell.value is not None:  # Ensure there is a value in the cell
        #             cell.value = ' ' + str(cell.value)  # Append space to the value
        #         cell.alignment = openpyxl.styles.Alignment(horizontal='left')

        # for row in ws['B43':'B48']:
        #     for cell in row:
        #         if cell.value is not None:  # Ensure there is a value in the cell
        #             cell.value = ' ' + str(cell.value)  # Append space to the value
        #         cell.alignment = openpyxl.styles.Alignment(horizontal='left')
    def main_report8b(self):
        title_cells = [
            {"cell": "B1", "value": "Report 8b IEP Service Recommendations Disaggregated by: District; Race/Ethnicity; Meal Status; Gender; ELL Status; Recommended Language of Instruction; and Grade Level.", "merge_cells": "B1:L1"},
            

        ]

        subtitle_cells = [
            {"cell": "B3", "value": "SY 2022-23 Students with IEP Recommended Services by District", "merge_cells": "B3:N3"},
            {"cell": "B40", "value": "SY 2022-23 Students with IEP Recommended Services by Ethnicity", "merge_cells": "B40:N40"},
            {"cell": "B50", "value": "SY 2022-23 Students with IEP Recommended Services by Meal Status", "merge_cells": "B50:N50"},
            {"cell": "B57", "value": "SY 2022-23 Students with IEP Recommended Services by Gender", "merge_cells": "B57:N57"},
            {"cell": "B65", "value": "SY 2022-23 Students with IEP Recommended Services by ELL Status", "merge_cells": "B65:N65"},
            {"cell": "B72", "value": "SY 2022-23 Students with IEP Recommended Services  by Recommended Language of Instruction", "merge_cells": "B72:N72"},
            {"cell": "B83", "value": "SY 2022-23 Students with IEP Recommended Services  by Grade Level", "merge_cells": "B83:N83"},
            {"cell": "B102", "value": "SY 2022-23 Students with IEP Recommended Services  by Temporary Housing", "merge_cells": "B102:N102"},
            {"cell": "B110", "value": "SY 2022-23 Students with IEP Recommended Services  by Foster Care Status", "merge_cells": "B110:N110"},
            

        ]

        column_widths = [5, 30, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
        # Step 1: Create Excel Report Template
        wb, ws = self.create_excel_report_template(title_cells, subtitle_cells, column_widths)
        
        # Step 2: Connect to the database
        cursor = self.connect_to_database()
        
        # Step 3: Fetch and write data for "Report 8b = IEP Service Recs by Race"
        results_byRace = self.fetch_data_by_race(cursor)
        self.write_data_to_excel(ws, results_byRace, start_row=43)
        
        # Step 4: Fetch and write data for "Report 8b = IEP Service Recs by District"
        results_byDistrict = self.fetch_data_by_district(cursor)
        self.write_data_to_excel(ws, results_byDistrict, start_row=6)

        # Step 5: Fetch and write data for "Report 8b = IEP Service Recs by Meal Status"
        results_byMealStatus = self.fetch_data_by_mealstatus(cursor)
        self.write_data_to_excel(ws, results_byMealStatus, start_row=53)

        # Step 6: Fetch and write data for "Report 8b = IEP Service Recs by Gender"
        results_byMealStatus = self.fetch_data_by_gender(cursor)
        self.write_data_to_excel(ws, results_byMealStatus, start_row=60)

        # Step 7: Fetch and write data for "Report 8b = IEP Service Recs by ELL Status"
        results_byELLStatus = self.fetch_data_by_ellstatus(cursor)
        self.write_data_to_excel(ws, results_byELLStatus, start_row=68)
        
        # Step 8: Fetch and write data for "Report 8b = IEP Service Recs by Language"
        results_byLanguage = self.fetch_data_by_language(cursor)
        self.write_data_to_excel(ws, results_byLanguage, start_row=75)

        # Step 9: Fetch and write data for "Report 8b = IEP Service Recs by Grade Level"
        results_byGradeLevel = self.fetch_data_by_gradelevel(cursor)
        self.write_data_to_excel(ws, results_byGradeLevel, start_row=86)

        # Step 10: Fetch and write data for "Report 8b = IEP Service Recs by Temporary Housing"
        results_byTempResFlag = self.fetch_data_by_tempResFlag(cursor)
        self.write_data_to_excel(ws, results_byTempResFlag, start_row=105)

        # Step 11: Fetch and write data for "Report 8b = IEP Service Recs by Foster Care Status"
        results_byFosterCareStatus = self.fetch_data_by_fosterCareStatus(cursor)
        self.write_data_to_excel(ws, results_byFosterCareStatus, start_row=113)
        # Step 9: Save the combined report
        save_path = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\Non-Redacted Annual Special Education Data Report.xlsx'
        wb.save(save_path)

if __name__ == "__main__":
        Tab1 = Solution()
        Tab1.main_report8b()                                                                  