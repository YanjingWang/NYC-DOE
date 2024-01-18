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

Row based masking:
Secondary mask: for all the 3 column subtotal calculation, if there is only one masked data (<=5 or >5) in this row, mask the smallest data of the rest unmasked data . If there are two or more masked data, no need to data masking.


Row based masking:
for all the 5 column subtotal calculation, if there is only one masked data in the row, mask the smallest data of the rest unmasked data. If there are two or more masked data, no need to do data masking.

Why always mask the smallest of rest unmasked data? Avoid overredaction. For example, in the secondary masking, if we masked E5 and G5, since G5 being to G +   = , it may trigger third masking and more data will be masked. However, if we mask E5 and F5 no need to mask G5 and it won't trigger third layer masking.

For overredaction, if there are more than two` >5 ` within the same group the same row or there are two `>5` within the same group the same row but also has at least one `<=5`  within the same group the same row and this `>5` is not the only `>5` in the column within its range it belongs to,  its' an overredaction, the first`>5` within the same group should be highlighted as green, but here my code the overredacted value has not been highlighted as green, for example, E89 needs to be highlighted as green since E89 + F89 = G89 and there are already two `>5` within the same group, then the first `>5` which is E89 needs to be highlighted as green and unmasked later. For example, check attached picture, for tab `Reports 1-4 = Initials`, D89 is the only `>5 ` of its column within its range it belongs to avoid the back track D90, D89's range is   (78, 3, 91, 13) according to redaction_config.py
For underredaction,  interate each row and for the same row if there is only one masked cell within the same group then highlight this cell, for example, H89 + I89 = J89, since there is only J89 was masked as `>5` we need to mask the smallest value within this group which is I89 here, I89 is 16 so it should be masked as `>5`.   
"""
import openpyxl
import os, shutil
from redaction_config import REPORTS_CONFIG
from redaction_config_SY23 import REPORTS_CONFIG_SY23
from redaction_config_SY24 import REPORTS_CONFIG_SY24
class Solution:
    def copyonefile(src,dst):
        shutil.copy(src,dst)
        print('copying one file from {0} to {1} is compelte'.format(src,dst)) 
    mylocalCCfolder = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CityCouncil\CCUnredacted'   
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY21\Annual Reports\Annual Special Education Data Report Unredacted SY21.xlsx', mylocalCCfolder)
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY21\Annual Reports\Annual Special Education Data Report Unredacted SY21.xlsx',"C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop")
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY22\Annual Reports\Non-Redacted Annual Special Education Data Report SY22.xlsx', mylocalCCfolder)
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY22\Annual Reports\Non-Redacted Annual Special Education Data Report SY22.xlsx',"C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop")
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY23\Annual Reports\Non-Redacted Annual Special Education Data Report SY23.xlsx', mylocalCCfolder)
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY23\Annual Reports\Non-Redacted Annual Special Education Data Report SY23.xlsx',"C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop")
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Non-Redacted Annual Special Education Data Report SY24.xlsx', mylocalCCfolder)
    copyonefile(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Non-Redacted Annual Special Education Data Report SY24.xlsx',"C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop")
    def is_percentage(self, cell):
        if isinstance(cell.value, float) and '0%' in cell.number_format:
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
                if not self.is_percentage(cell):
                    cell.value = self.mask_value_initial(cell.value)
        
        # Mask smallest if only one '<=5' in column
        for col in ws.iter_cols(min_row=start_row, max_row=end_row, min_col=start_col, max_col=end_col):
            valid_vals = [cell.value for cell in col if isinstance(cell.value, (int, float)) and cell.value != '<=5']
            if sum([cell.value == '<=5' for cell in col]) == 1 and valid_vals:
                min_val = min(valid_vals)
                # if min_val == 0 then skip it and mask the next smallest value
                if min_val == 0:
                    continue
                for cell in col:
                    if cell.value == min_val:
                        cell.value = '>5'
                        break


    # Step 2: Secondary Masking
    def secondary_mask(self, ws, start_row, end_row, groups):
        # groups = [(5, 6, 7), (8, 9, 10), (7, 10, 11)]  # E,F,G and H,I,J and G,J,K respectively

        for group in groups:
            for row_num in range(start_row, end_row + 1):
                masked_vals = [col for col in group if ws.cell(row=row_num, column=col).value in ['<=5', '>5']]
                if len(masked_vals) == 1:  # If only one value in the group is masked
                    numeric_vals = [ws.cell(row=row_num, column=col).value for col in group if isinstance(ws.cell(row=row_num, column=col).value, (int, float)) and not self.is_percentage(ws.cell(row=row_num, column=col))]
                    if numeric_vals:  # Ensure there are numeric values
                        min_val = min(numeric_vals)
                        for col in group:
                            if ws.cell(row=row_num, column=col).value == min_val:
                                if min_val == 0:
                                    ws.cell(row=row_num, column=col).value = self.mask_value_zero(min_val)
                                else:
                                    ws.cell(row=row_num, column=col).value = self.mask_value_secondary(min_val)
                                break

                elif len(masked_vals) >= 2: # Two or more values are already masked, no action needed
                    continue


    # Step 3: Masking based on Subtotals        
    def third_mask(self,ws, start_row, end_row,groups):
        # groups = [(3,4,11,12)]  # C,D,K,L
        for group in groups:
            for row_num in range(start_row, end_row + 1):
                masked_vals = [col for col in group if ws.cell(row=row_num, column=col).value in ['<=5', '>5']]
                if len(masked_vals) == 1:  # If only one value in the group is masked, need to mask the smallest of the unmasked values
                    numeric_vals = [ws.cell(row=row_num, column=col).value for col in group if isinstance(ws.cell(row=row_num, column=col).value, (int, float)) and not self.is_percentage(ws.cell(row=row_num, column=col))]
                    if numeric_vals:  # Ensure there are numeric values
                        min_val = min(numeric_vals)
                        for col in group:
                            if ws.cell(row=row_num, column=col).value == min_val:
                                if min_val == 0:
                                    ws.cell(row=row_num, column=col).value = self.mask_value_zero(min_val)
                                else:
                                    ws.cell(row=row_num, column=col).value = self.mask_value_secondary(min_val)
                                break
                elif len(masked_vals) >= 2:  # Two or more values are already masked, so no action needed
                    continue


    # def highlight_overredaction(self, ws, start_row, end_row, groups):
    #     for group in groups:
    #         for row_num in range(start_row, end_row + 1):
    #             gt5_cells = []
    #             lte5_exists = False
    #             # Check each cell in the group for the current row
    #             for col_index in group:
    #                 cell = ws.cell(row=row_num, column=col_index)
    #                 if cell.value == '>5':
    #                     gt5_cells.append(cell)
    #                 elif cell.value == '<=5':
    #                     lte5_exists = True
    #             # Determine if overredaction rules are met
    #             if len(gt5_cells) > 2 or (len(gt5_cells) == 2 and lte5_exists):
    #                 # Highlight the first '>5' cell in green
    #                 self.green_cell(gt5_cells[0])
    #                 # Optionally, here you could unmask the green cell if needed
    #                 # gt5_cells[0].value = 'Unmasked Value'
    #                 print(ws.title, f"Overredaction: Highlighting cell {gt5_cells[0].coordinate} in green")
    # def highlight_overredaction(self, ws, groups, ranges):
    #     for group in groups:
    #         for (start_row, start_col, end_row, end_col) in ranges:  # Extracting the range from the tuple
    #             for row_num in range(start_row, end_row + 1):
    #                 gt5_cells = []
    #                 lte5_exists = False
    #                 for col_index in group:
    #                     cell = ws.cell(row=row_num, column=col_index)
    #                     if cell.value == '>5':
    #                         gt5_cells.append(cell)
    #                     elif cell.value == '<=5':
    #                         lte5_exists = True

    #                 # Check if the first '>5' is not the only one in its column within the range
    #                 if gt5_cells and (len(gt5_cells) > 2 or (len(gt5_cells) == 2 and lte5_exists)):
    #                     first_gt5_cell = gt5_cells[0]
    #                     col_values = [ws.cell(row=r, column=first_gt5_cell.column).value for r in range(start_row, end_row + 1)]
    #                     print(col_values)
    #                     if col_values.count('>5') > 1:
    #                         self.green_cell(first_gt5_cell)
    #                         print(ws.title, f"Overredaction: Highlighting cell {first_gt5_cell.coordinate} in green")
    def highlight_overredaction(self, ws, groups, ranges, unredacted_ws):
        for group in groups:
            for (start_row, start_col, end_row, end_col) in ranges:  # Extracting the range from the tuple
                for row_num in range(start_row, end_row + 1):
                    gt5_cells = []
                    lte5_exists = False
                    for col_index in group:
                        cell = ws.cell(row=row_num, column=col_index)
                        if cell.value == '>5':
                            gt5_cells.append(cell)
                        elif cell.value == '<=5':
                            lte5_exists = True

                    # Check if the first '>5' is not the only one in its column within the range
                    if gt5_cells and (len(gt5_cells) > 2 or (len(gt5_cells) == 2 and lte5_exists)):
                        first_gt5_cell = gt5_cells[0]
                        col_values = [ws.cell(row=r, column=first_gt5_cell.column).value for r in range(start_row, end_row + 1)]
                        if col_values.count('>5') > 1:
                            # self.green_cell(first_gt5_cell) # Highligh the overredaction cell in green
                            # Get the original value from the unredacted worksheet
                            original_value = unredacted_ws.cell(row=first_gt5_cell.row, column=first_gt5_cell.column).value
                            # Unmask the cell by setting its value to the original value
                            first_gt5_cell.value = original_value
                            print(ws.title, f"Unmasking overredacted cell {first_gt5_cell.coordinate} with original value")

    def highlight_underredaction(self, ws, start_row, end_row, groups):
        for group in groups:
            for row_num in range(start_row, end_row + 1):
                masked_cells = [ws.cell(row=row_num, column=col) for col in group if ws.cell(row=row_num, column=col).value in ['<=5', '>5']]
                if len(masked_cells) == 1:
                    # Find the smallest unmasked value within the group
                    unmasked_cells = [(cell, cell.value) for cell in [ws.cell(row=row_num, column=col) for col in group] if cell not in masked_cells]
                    if unmasked_cells:
                        smallest_cell = min(unmasked_cells, key=lambda x: x[1])
                        # Mask the smallest cell based on its value, if <=5, mask as <=5, otherwise mask as >5
                        if smallest_cell[1] == 0:
                            smallest_cell[0].value = self.mask_value_zero(smallest_cell[1])
                        else:
                            smallest_cell[0].value = self.mask_value_secondary(smallest_cell[1])
                        # self.yellow_cell(smallest_cell[0])  # Highlight this cell
                        print(ws.title, f"Underredaction: Highlighting cell {smallest_cell[0].coordinate} in yellow")

    def green_cell(self, cell):
        cell.fill = openpyxl.styles.PatternFill(start_color='00ff15', end_color='00ff15', fill_type='solid')
    def yellow_cell(self, cell):
        cell.fill = openpyxl.styles.PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')

    def mask_excel_file(self,filename,tab_name,configurations):
        # Load the workbook
        wb = openpyxl.load_workbook(filename)
        try:
            ws = wb[tab_name]
        except KeyError:
            print(f"Warning: Worksheet {tab_name} does not exist in the file {filename}. Skipping...") #SWDs by School is not in SY23
            return

        # Convert string to int where possible
        for r in configurations['ranges']:
            for row in ws.iter_rows(min_row=r[0], max_row=r[2], min_col=r[1], max_col=r[3]):
                for cell in row:
                    if isinstance(cell.value, str):
                        try:
                            cell.value = int(cell.value)
                        except ValueError:
                            # If the value cannot be converted to int, keep the original value
                            pass
                        
        # Mask data for the specific ranges
        for r in configurations['ranges']:
            self.initial_mask(ws, *r)
            
        # Invoke secondary masking if present in configurations, otherwise skip
        if 'secondary_mask' in configurations and 'secondary_mask_kwargs' in configurations:
            self.secondary_mask(ws, *configurations['secondary_mask'], **configurations.get('secondary_mask_kwargs', {}))
        
        # Conditionally invoke third masking if present in configurations
        if 'third_mask' in configurations and 'third_mask_kwargs' in configurations:
            self.third_mask(ws, *configurations['third_mask'], **configurations['third_mask_kwargs'])
        # print('all masking is done, now highlight overredaction')
        # if 'total_col_indexes' in configurations and 'groups' in configurations:
        #     start_row, end_row = configurations['secondary_mask']  # Assuming secondary_mask defines the row range
        #     self.highlight_overredaction(ws, configurations['total_col_indexes'], start_row, end_row, configurations['groups'])
        #     self.highlight_underredaction(ws, start_row, end_row, configurations['groups'])
        if 'total_col_indexes' in configurations and 'groups' in configurations and 'ranges' in configurations:
            start_row, end_row = configurations['secondary_mask']  # Assuming secondary_mask defines the row range
            # self.highlight_overredaction(ws, start_row, end_row, configurations['groups'], configurations['ranges'])
            # self.highlight_overredaction(ws, configurations['groups'], configurations['ranges'])
            self.highlight_underredaction(ws, start_row, end_row, configurations['groups'])
        # print('highlight overredaction is done')

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
    def print_cell_formats(file_name, sheet_name, cell_range):
        wb = openpyxl.load_workbook(file_name)
        ws = wb[sheet_name]
        for row in ws[cell_range]:
            for cell in row:
                print(f"Cell {cell.coordinate} - Value: {cell.value} - Type: {type(cell.value)} - Format: {cell.number_format}")

    # Example usage
    print_cell_formats(r'R:\SEO Analytics\Reporting\City Council\City Council SY24\Annual Reports\Non-Redacted Annual Special Education Data Report SY24.xlsx', 'Reports 5-7 = Reevaluations', 'C5:M37')


# Call the function with your filename
if __name__ == "__main__":
    processor = Solution()
    ##SY21 and SY22
    filenames = [
        'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Annual Special Education Data Report Unredacted SY21.xlsx',
        'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted Annual Special Education Data Report SY22.xlsx'
    ]
    
    for fname in filenames:
        for report, config in REPORTS_CONFIG.items():
            processor.mask_excel_file(fname, report, config)

    redacted_filenames = [
        'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Annual Special Education Data Report Unredacted SY21.xlsx',
        'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted Annual Special Education Data Report SY22.xlsx'
    ]
    unredacted_filenames = [
        'C:\\Users\\Ywang36\OneDrive - NYCDOE\\Desktop\\CityCouncil\CCUnredacted\\Annual Special Education Data Report Unredacted SY21.xlsx',
        'C:\\Users\\Ywang36\OneDrive - NYCDOE\\Desktop\\CityCouncil\\CCUnredacted\\Non-Redacted Annual Special Education Data Report SY22.xlsx'
    ]

    for redacted_file, unredacted_file in zip(redacted_filenames, unredacted_filenames):
        redacted_wb = openpyxl.load_workbook(redacted_file, data_only=True)
        unredacted_wb = openpyxl.load_workbook(unredacted_file, data_only=True)

        for report, config in REPORTS_CONFIG.items():
            if 'groups' in config and 'ranges' in config:  # Ensure both 'groups' and 'ranges' keys exist
                ws = redacted_wb[report]
                unredacted_ws = unredacted_wb[report]
                processor.highlight_overredaction(ws, config['groups'], config['ranges'], unredacted_ws)

        # Save the redacted workbook after unmasking green cells
        redacted_wb.save(redacted_file)
        redacted_wb.close()
    ##SY23
    filename_SY23 = 'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted Annual Special Education Data Report SY23.xlsx'
    for report, config in REPORTS_CONFIG_SY23.items():
        processor.mask_excel_file(filename_SY23, report, config)

    redacted_filenames_SY23 = [ 'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted Annual Special Education Data Report SY23.xlsx']
    unredacted_filenames_SY23 = ['C:\\Users\\Ywang36\OneDrive - NYCDOE\\Desktop\\CityCouncil\\CCUnredacted\\Non-Redacted Annual Special Education Data Report SY23.xlsx']
    for redacted_file, unredacted_file in zip(redacted_filenames_SY23, unredacted_filenames_SY23):
        redacted_wb = openpyxl.load_workbook(redacted_file, data_only=True)
        unredacted_wb = openpyxl.load_workbook(unredacted_file, data_only=True)

        for report, config in REPORTS_CONFIG_SY23.items():
            if 'groups' in config and 'ranges' in config:  # Ensure both 'groups' and 'ranges' keys exist
                ws = redacted_wb[report]
                unredacted_ws = unredacted_wb[report]
                processor.highlight_overredaction(ws, config['groups'], config['ranges'], unredacted_ws)

        # Save the redacted workbook after unmasking green cells
        redacted_wb.save(redacted_file)
        redacted_wb.close()
    #SY24
    filename_SY24 = 'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted Annual Special Education Data Report SY24.xlsx'
    for report, config in REPORTS_CONFIG_SY24.items():
        processor.mask_excel_file(filename_SY24, report, config)
    redacted_filenames_SY24 = [ 'C:\\Users\\Ywang36\\OneDrive - NYCDOE\\Desktop\\Non-Redacted Annual Special Education Data Report SY24.xlsx']
    unredacted_filenames_SY24 = ['C:\\Users\\Ywang36\OneDrive - NYCDOE\\Desktop\\CityCouncil\\CCUnredacted\\Non-Redacted Annual Special Education Data Report SY24.xlsx']
    for redacted_file, unredacted_file in zip(redacted_filenames_SY24, unredacted_filenames_SY24):
        redacted_wb = openpyxl.load_workbook(redacted_file, data_only=True)
        unredacted_wb = openpyxl.load_workbook(unredacted_file, data_only=True)

        for report, config in REPORTS_CONFIG_SY24.items():
            if 'groups' in config and 'ranges' in config:  # Ensure both 'groups' and 'ranges' keys exist
                ws = redacted_wb[report]
                unredacted_ws = unredacted_wb[report]
                processor.highlight_overredaction(ws, config['groups'], config['ranges'], unredacted_ws)

        # Save the redacted workbook after unmasking green cells
        redacted_wb.save(redacted_file)
        redacted_wb.close()