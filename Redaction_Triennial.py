"""
Reports 1-4 = Initials subtotal calculation:
E + F = G, H + I = J, G + J = K, D + K + L + M = C
Reports 5-7 = Reevaluations subtotal calculation:
E + F = G, H + I = J, G + J = K, D + K + L  = C
Report 8 = Registers subtotal calculation:
C + D + E + F = G, H + I + J + K = L, G + L = M
SWDs by School : C4+ ...+ C1602 = C1603
Report 8a = Disability class subtotal calculation:
C + D +E + F + G + H + I + J + K + L + M + N + O = P 
Report 9 = Placement: C6+...+C37 = C38, D6+...+D37 = D38, C42+...C46 = C47, D42+...D46 = D47, C51+C52 = C53, D51+D52 = D53, C57+C58 = C59, D57+D58 = D59, C63+C64 = C65, 
D63+D64 = D65, C69+C72 = C73, D69+D72 = D73, C77+C89=D90, D77+D89=D90
Report 10 = LRE-MRE: C6+...C37=C38,D6+...D37=D38,E6+...E37=E38,F6+...F37=F38, C42+...C46=C47,D42+...D46=D47,E42+...E46=E47,F42+...F46=F47,C51+C52=C53,D51+D52=D53,E51+E52=E53,F51+F52=F53,E57+E58=E59,F57+F58=F59,C63+C64=C65,D63+D64=D65,E63+E64=E65,F63+F64=F65,C69+C72=C73,D69+D72=D73,E69+E72=E73,F69+F72=F73,C77+...+C89=C90,D77+...+D89=D90,E77+...+E89=E90,F77+...+F89=F90

Redaction rules: 
Column based masking:
Initial mask: find all data 0<data<=5 and make them as <=5
Then since there are Total calculations for every column, iterate each column if there is only one <=5 in this column to mask the smallest data of rest unmasked data for this column as >5. if min_val == 0 then skip it and mask the next smallest value

For percentage redaction, if the number is masked as `<=5` or `>5` then the adjcent percentage should be masked as `*`.

100% percentage sum redaction, if the sum of the percentage is 100% then mask the smallest numeric and percentage within the same row. Since
Tab `Report 10 = IEP Service Recs`:  D+F+H+J+L+N = 100%
Tab `Report 14 = Programs`: D+F+H = 100%
Tab `Report 14a = Bilingual Programs`: D+F+H = 100%
Tab `Report 15 = Related Services`: D+F+H = 100%
Tab `Report 15a = Transportation`: D+F+H = 100%
Tab `Report 16 = BIP`: D+F = 100% I want to change percentage redaction rule: if there is one percentage cell is redacted as `*` and its adjacent numeric cell is masked as `<=5` or `>5` , then we redact the smallest numeric cell for the rest of the same row of that `*` redacted cell belongs to based on its value, if its value >5 then mask it as `>5` if its value <=5 then mask it as `<=5` and then mask its adjacent percentage cell. For example, check attached picture, for Tab `Report 10 = IEP Service Recs` since   D21+F21+H21+J21+L21+N21 = 100% and M21 is redacted as `<=5` and N21 is redacted as `*`, we need to mask K21 as `<=5` and its adjacent percentage cell * to avoid back track. 

For overall column in every range check, if there is only one masked cell (`<=5` or `>5`) in that column then it's underredaction, we need to mask the smallest value of the rest cell in that column.For example, in tab `Report 9 = Disability class`, N102 is the only `>5 ` of its column within its range it belongs to, in order to avoid the back track we need to redact the smallest value of this column which is N100 (0), N102's range is (100, 3, 102, 16) according to redaction_config_SY24.py

For related services only Bilingual recommendations can be partially encountered. Partially encountered in that case means it was a bilingual recommendation that was provided in English. For the non-bilingual recommendations there is no such thing as "partial encounter" which is why we say "N/A" 

There is different redaction logic for bilingual and non-bilingual related services recommendations 

for the bilingual recommendations the logic is the same as the program redaction logic, for the non-bilingual recommendations (also called "monolingual recommendations") the masking value is redacted, but the percentages can remain since there are only two possible values  
"""
import openpyxl
import os, shutil
from redaction_config_triennial_SY24 import TRIENNIAL_REPORTS_CONFIG_SY24
class Solution:
    def copyonefile(src,dst):
        shutil.copy(src,dst)
        print('copying one file from {0} to {1} is compelte'.format(src,dst)) 
    mylocalCCfolder = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\CCUnredacted'   
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Triennial Reports\Non-Redacted City Council Triennial Report SY24.xlsx', mylocalCCfolder)
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Triennial Reports\Non-Redacted City Council Triennial Report SY24.xlsx',"C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop")
    # percentage redaction including 0% to 100% redaction
    def is_percentage(self, cell):
        # Check if cell's format is for percentage
        if '%' in cell.number_format:
            return True
        # Specifically check for 100% values, which might be stored as 1.0
        if cell.value == 1.0 and '%' in cell.number_format:
            return True
        return False



    
    def mask_value_initial(self,val):
        if isinstance(val, (int, float)) and 0 < val <= 5:
            return '<=5'
        return val

    def mask_value_secondary(self,val):
        if isinstance(val, (int, float)) and 0 < val <= 5:
            return '<=5'
        elif isinstance(val, (int, float)) and val > 5:
            return '>5'
        return val
    
    def mask_value_zero(self,val):
        if isinstance(val, (int, float)) and val == 0:
            return '<=5'
        return val

    def initial_mask(self,ws, start_row, start_col, end_row, end_col):
        # Step 1: Initial Masking
        for row in ws.iter_rows(min_row=start_row, max_row=end_row, min_col=start_col, max_col=end_col):
            for cell in row:
                # do not mask percentage and 100%
                if not self.is_percentage(cell):
                    cell.value = self.mask_value_initial(cell.value)
        
        # Mask smallest if only one '<=5' in column
        for col in ws.iter_cols(min_row=start_row, max_row=end_row, min_col=start_col, max_col=end_col):
            valid_vals = [cell.value for cell in col if isinstance(cell.value, (int, float)) and cell.value != '<=5']
            if sum([cell.value == '<=5' for cell in col]) == 1 and valid_vals:
                min_val = min(valid_vals)
                # if min_val == 0 then mask it as <=5 if not then mask it as >5
                if min_val == 0:
                    for cell in col:
                        if cell.value == min_val:
                            cell.value = '<=5'
                            break
                for cell in col:
                    if cell.value == min_val:
                        cell.value = '>5'
                        break



    def redact_percentage_based_on_number(self, ws, numeric_col, perc_col, start_row, end_row):
        for row in range(start_row, end_row + 1):
            number_cell = ws.cell(row=row, column=numeric_col)
            percentage_cell = ws.cell(row=row, column=perc_col)
            # Check if the numeric cell is masked and the percentage cell is not '100%'
            if number_cell.value in ['<=5', '>5']:
                # If the percentage is not '100%', redact it as '*'
                if not (percentage_cell.value == '100%' or percentage_cell.value == 1.0):
                    percentage_cell.value = '*'

                

    def apply_percentage_redaction(self,ws, config, start_row, end_row):
        for numeric_col, perc_col in config['numeric_percentage_pairs']:
            self.redact_percentage_based_on_number(ws, numeric_col, perc_col, start_row, end_row)

    def mask_smallest_numeric_and_percentage(self, ws, start_row, end_row, numeric_percentage_pairs):
        for row_num in range(start_row, end_row + 1):
            # Initialize lists to hold numeric and percentage cells
            numeric_cells = []
            percentage_cells = []

            # Gather numeric and percentage cells for the current row based on the provided pairs
            for pair in numeric_percentage_pairs:
                numeric_col, perc_col = pair  # Unpack the pair
                numeric_cell = ws.cell(row=row_num, column=numeric_col)
                percentage_cell = ws.cell(row=row_num, column=perc_col)
                if isinstance(numeric_cell.value, (int, float)):
                    numeric_cells.append(numeric_cell)
                if percentage_cell.value == '*':
                    percentage_cells.append(percentage_cell)

            # Proceed if there's at two numeric cell and one percentage cell marked with '*'
            if len(numeric_cells)>=2 and percentage_cells:
                # Filter out numeric cells that are already masked
                unmasked_numeric_cells = [cell for cell in numeric_cells if cell.value not in ['<=5', '>5']]
                print(ws.title, f"Unmasked numeric cells in row {row_num}: {[cell.coordinate for cell in unmasked_numeric_cells]}")
                if unmasked_numeric_cells:
                    # Find the smallest numeric cell by value
                    smallest_numeric_cell = min(unmasked_numeric_cells, key=lambda cell: cell.value)
                    # Mask the smallest numeric cell based on its value
                    if smallest_numeric_cell.value <= 5:
                        smallest_numeric_cell.value = '<=5'
                    else:
                        smallest_numeric_cell.value = '>5'
                    # Mask the adjacent percentage cell
                    adjacent_percentage_cell = ws.cell(row=row_num, column=smallest_numeric_cell.column + 1)
                    adjacent_percentage_cell.value = '*'







    def mask_excel_file(self,filename,tab_name,configurations):
        # Load the workbook
        wb = openpyxl.load_workbook(filename)
        try:
            ws = wb[tab_name]
        except KeyError:
            print(f"Warning: Worksheet {tab_name} does not exist in the file {filename}. Skipping...") #SWDs by School is not in SY23
            return

        # # Convert string to int where possible
        # for r in configurations['ranges']:
        #     for row in ws.iter_rows(min_row=r[0], max_row=r[2], min_col=r[1], max_col=r[3]):
        #         for cell in row:
        #             if isinstance(cell.value, str):
        #                 try:
        #                     cell.value = int(cell.value)
        #                 except ValueError:
        #                     # If the value cannot be converted to int, keep the original value
        #                     pass
                        
        # Mask data for the specific ranges
        for r in configurations['ranges']:
            self.initial_mask(ws, *r)
                       
        # Apply the percentage redaction based on configuration if the key exists
        for r in configurations['ranges']:
            if 'numeric_percentage_pairs' in configurations:
                self.apply_percentage_redaction(ws, configurations, r[0], r[2])

        # In your mask_excel_file function
        for r in configurations['ranges']:
            if '100_percentage_sum' in configurations:
                # Retrieve the correct numeric_percentage_pairs for the current tab
                numeric_percentage_pairs = configurations['numeric_percentage_pairs']
                # Call the function with the correct pairs
                self.mask_smallest_numeric_and_percentage(ws, r[0], r[2], numeric_percentage_pairs)


        # # Mask underredacted columns
        # for r in configurations['ranges']:
        #     self.check_and_mask_underredacted_columns(ws, r[0], r[2], r[1], r[3])
        # Save the modified workbook
        wb.save(filename) # Adjust the range if necessary
        wb.close()
    def unmask_green_cells(self, redacted_filename, unredacted_filename, tab_name):
        # Load both workbooks
        redacted_wb = openpyxl.load_workbook(redacted_filename, data_only=True)
        unredacted_wb = openpyxl.load_workbook(unredacted_filename, data_only=True)

        # Access the specific tab in both workbooks
        redacted_ws = redacted_wb[tab_name]
        unredacted_ws = unredacted_wb[tab_name]
        print(f"Unmasking green cells in {tab_name}...")
        # Iterate through the worksheet and find green cells
        for row in redacted_ws.iter_rows():
            for cell in row:
                if cell.fill.start_color.index == '00ff15':  # Check if the cell is highlighted in green
                    # Get the corresponding cell from the unredacted worksheet
                    original_cell = unredacted_ws[cell.coordinate]
                    print(f"Found green cell {cell.coordinate} with value {cell.value}")
                    # Replace the value in the redacted worksheet with the original value
                    cell.value = original_cell.value
                    print(f"Unmasking cell {cell.coordinate} with value {cell.value}")
                    # Remove the green fill
                    cell.fill = openpyxl.styles.PatternFill(fill_type=None)
                else:
                    print("No green cells found in this worksheet")
                    continue

        # Save the modified redacted workbook
        redacted_wb.save(redacted_filename)

    # Helper function to print cell values, types, and formats
    def print_cell_formats(file_name, sheet_name, cell_range):
        wb = openpyxl.load_workbook(file_name)
        ws = wb[sheet_name]
        for row in ws[cell_range]:
            for cell in row:
                print(f"Cell {cell.coordinate} - Value: {cell.value} - Type: {type(cell.value)} - Format: {cell.number_format}")


    def check_and_mask_underredacted_columns(self, ws, start_row, end_row, start_col, end_col):
        # Iterate over columns within the specified range
        for col_index in range(start_col, end_col + 1):
            column_cells = [ws.cell(row=row_index, column=col_index) for row_index in range(start_row, end_row + 1)]
            masked_cells = [cell for cell in column_cells if cell.value in ['<=5', '>5']]
            unmasked_cells = [cell for cell in column_cells if cell not in masked_cells and isinstance(cell.value, (int, float))]

            # If there is only one masked cell in the column
            if len(masked_cells) == 1 and unmasked_cells:
                # Find the smallest unmasked value
                smallest_unmasked_cell = min(unmasked_cells, key=lambda cell: cell.value)
                # Mask it based on its value
                if 0 <= smallest_unmasked_cell.value <= 5:
                    smallest_unmasked_cell.value = '<=5'
                elif smallest_unmasked_cell.value > 5:
                    smallest_unmasked_cell.value = '>5'
                # Optionally highlight the cell
                # self.yellow_cell(smallest_unmasked_cell)
                print(ws.title,f"Underredaction: Masking cell {smallest_unmasked_cell.coordinate} with {'<=5' if smallest_unmasked_cell.value == '<=5' else '>5'}")




# Call the function with your filename
if __name__ == "__main__":
    processor = Solution()
    #SY24
    filename_SY24 = 'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted City Council Triennial Report SY24.xlsx'
    for report, config in TRIENNIAL_REPORTS_CONFIG_SY24.items():
        processor.mask_excel_file(filename_SY24, report, config)
    redacted_filenames_SY24 = [ 'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted City Council Triennial Report SY24.xlsx']
    unredacted_filenames_SY24 = ['C:\\Users\\Ywang36\OneDrive - NYCDOE\\Desktop\\CityCouncil\\CCUnredacted\\Non-Redacted City Council Triennial Report SY24.xlsx']
    for redacted_file, unredacted_file in zip(redacted_filenames_SY24, unredacted_filenames_SY24):
        redacted_wb = openpyxl.load_workbook(redacted_file, data_only=True)
        unredacted_wb = openpyxl.load_workbook(unredacted_file, data_only=True)

        for report, config in TRIENNIAL_REPORTS_CONFIG_SY24.items():
            if 'groups' in config and 'ranges' in config:  # Ensure both 'groups' and 'ranges' keys exist
                ws = redacted_wb[report]
                unredacted_ws = unredacted_wb[report]
                processor.highlight_overredaction(ws, config['groups'], config['ranges'], unredacted_ws)

        # Save the redacted workbook after unmasking green cells
        redacted_wb.save(redacted_file)
        redacted_wb.close()