import os
import time
from datetime import datetime
# ### change the timestamp of the file
# # Replace with the path to the directory containing your files
# directory_path = 'C:\PA_DISTRIBUTION_PDF_Charter'

# # Specify the old and new dates in the format 'mm-dd-yyyy'
# old_date_str = '04-03-2024'
# new_date_str = '03-11-2024'

# # Parse the date strings to datetime objects
# old_date = datetime.strptime(old_date_str, '%m-%d-%Y')
# new_date = datetime.strptime(new_date_str, '%m-%d-%Y')

# # Convert the new datetime to a timestamp
# new_timestamp = time.mktime(new_date.timetuple())

# # Walk through the directory and update file timestamps
# for root, dirs, files in os.walk(directory_path):
#     for file in files:
#         if old_date_str in file:
#             file_path = os.path.join(root, file)
#             os.utime(file_path, (new_timestamp, new_timestamp))
#             print(f"Updated timestamp for: {file}")


# import os
# ### change the name of the file
# # Replace this with the actual path to your directory containing the files
# directory_path = 'C:\PA_DISTRIBUTION_PDF_Charter'

# # The date strings to be replaced and their replacements
# old_date_str = '04-03-2024'
# new_date_str = '03-11-2024'

# # Iterate over all files in the directory
# for filename in os.listdir(directory_path):
#     if old_date_str in filename:
#         # Create the new file name by replacing the old date with the new date
#         new_filename = filename.replace(old_date_str, new_date_str)
#         # Construct the full old and new file paths
#         old_file_path = os.path.join(directory_path, filename)
#         new_file_path = os.path.join(directory_path, new_filename)
#         # Rename the file
#         os.rename(old_file_path, new_file_path)
#         print(f'Renamed "{filename}" to "{new_filename}"')





# ### change the timestamp of the file
# # Replace with the path to the directory containing your files
# directory_path = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CS6501\HW12'

# # Specify the old and new dates in the format 'mm/dd/yyyy 11:00 AM'
# old_date_str = '04/10/2024 09:25 PM'
# new_date_str = '07/12/2022 11:19 PM'

# # Parse the date strings to datetime objects
# old_date = datetime.strptime(old_date_str, '%m/%d/%Y %I:%M %p')
# new_date = datetime.strptime(new_date_str, '%m/%d/%Y %I:%M %p')

# # Convert the new datetime to a timestamp
# new_timestamp = time.mktime(new_date.timetuple())

# # Walk through the directory and update file named "HW12" timestamps
# for root, dirs, files in os.walk(directory_path):
#     for file in files:
#         if "HW12" in file:
#             file_path = os.path.join(root, file)
#             os.utime(file_path, (new_timestamp, new_timestamp))
#             print(f"Updated timestamp for: {file}")
import os
from datetime import datetime

# Specify the file path
file_path = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CS6501\HW12'

# Get the timestamps
creation_time = os.path.getctime(file_path)
modification_time = os.path.getmtime(file_path)

# Convert timestamps to readable format
creation_date = datetime.fromtimestamp(creation_time).strftime('%m/%d/%Y %I:%M %p')
modification_date = datetime.fromtimestamp(modification_time).strftime('%m/%d/%Y %I:%M %p')

print(f"Creation date and time: {creation_date}")
print(f"Modification date and time: {modification_date}")

# import os
# import datetime
# from datetime import timedelta

# # Path to the directory containing files
# directory_path = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CS6501\6501\screenshot for lecture\16'

# # Navigate to the directory
# os.chdir(directory_path)

# # Function to modify date in filename and timestamp
# def modify_dates(file_name):
#     # Extract the date part from the filename
#     old_date_str = file_name[12:22]
#     new_date_str = '2024-04-30'  # New date part to replace in filename
    
#     # Replace the year in the filename
#     new_file_name = file_name.replace(old_date_str, new_date_str)
    
#     # Parse the old date
#     old_date = datetime.datetime.strptime(old_date_str, '%Y-%m-%d')
    
#     # Calculate new date for the timestamp
#     # Example adds a fixed interval, you can adjust as necessary
#     new_date = datetime.datetime(2024, 4, 30, old_date.hour, old_date.minute, old_date.second)
    
#     # Rename the file
#     os.rename(file_name, new_file_name)
    
#     # Modify the timestamp of the file
#     # Convert datetime to time in seconds
#     mod_time = new_date.timestamp()
#     os.utime(new_file_name, (mod_time, mod_time))

# # Loop through all files in the directory
# for filename in os.listdir(directory_path):
#     if filename.startswith("Screen Shot 2021"):
#         modify_dates(filename)


# import os
# import time
# from datetime import datetime

# # Directory containing the files
# directory = r'C:\Users\Ywang36\OneDrive - NYCDOE\Desktop\CS6501\6501\screenshot for lecture\2.1 SVM and scaling'

# # Iterate over each file in the directory
# for filename in os.listdir(directory):
#     if "Screen Shot 2024" in filename:
#         # Construct the full file path
#         file_path = os.path.join(directory, filename)
        
#         # Extract the date and time from the filename
#         date_str = filename.split(' at ')[0].replace('Screen Shot ', '')  # "2024-03-25"
#         time_str = filename.split(' at ')[1].split('.')[0] + ":" + filename.split('.')[1]  # "20:02"
#         date_time_str = date_str + ' ' + time_str  # "2024-03-25 20:02"
        
#         # Convert the date and time string to a datetime object
#         date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        
#         # Convert datetime object to desired format
#         formatted_date_time = date_time_obj.strftime("%m/%d/%Y %I:%M %p")
#         print(formatted_date_time)  # Output: "03/25/2024 08:02 PM"
        
#         # Update the last modification time and the last accessed time
#         # Convert datetime object to POSIX timestamp
#         newtimestamp = time.mktime(date_time_obj.timetuple())
#         print(newtimestamp)
        
#         # Update the last modification time and the last accessed time
#         os.utime(file_path, (newtimestamp, newtimestamp))

#         print("Filenames and timestamps updated successfully.")





