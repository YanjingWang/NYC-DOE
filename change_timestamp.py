import os
import time
from datetime import datetime
### change the timestamp of the file
# Replace with the path to the directory containing your files
directory_path = 'C:\PA_DISTRIBUTION_PDF_Charter'

# Specify the old and new dates in the format 'mm-dd-yyyy'
old_date_str = '04-03-2024'
new_date_str = '03-11-2024'

# Parse the date strings to datetime objects
old_date = datetime.strptime(old_date_str, '%m-%d-%Y')
new_date = datetime.strptime(new_date_str, '%m-%d-%Y')

# Convert the new datetime to a timestamp
new_timestamp = time.mktime(new_date.timetuple())

# Walk through the directory and update file timestamps
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if old_date_str in file:
            file_path = os.path.join(root, file)
            os.utime(file_path, (new_timestamp, new_timestamp))
            print(f"Updated timestamp for: {file}")


import os
### change the name of the file
# Replace this with the actual path to your directory containing the files
directory_path = 'C:\PA_DISTRIBUTION_PDF_Charter'

# The date strings to be replaced and their replacements
old_date_str = '04-03-2024'
new_date_str = '03-11-2024'

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    if old_date_str in filename:
        # Create the new file name by replacing the old date with the new date
        new_filename = filename.replace(old_date_str, new_date_str)
        # Construct the full old and new file paths
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed "{filename}" to "{new_filename}"')





