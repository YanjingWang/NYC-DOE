import os
import base64
import requests
import datetime
from ms_graph import generate_access_token
import win32com.client as win32


# print(dir(os))
# print(os.getcwd())
# os.chdir("R:/SEO Analytics/Reporting/Critical Processes/Related Services/SY22-23")
# os.chdir("R:\SEO Analytics\Processing\Data Mart Files\Templates\SESIS Mandated Services Report")
# os.chdir("R:\SEO Analytics\Reporting\Critical Processes\Related Services\SY22-23")
os.startfile(r'R:\SEO Analytics\Reporting\Critical Processes\Related Services\SY22-23')
# print(os.getcwd())
# print(os.listdir())
file = 'R:\SEO Analytics\Processing\Data Mart Files\Templates\SESIS Mandated Services Report\SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm'
# os.popen(file, 'r')
print("Click Enable Enable in the ribbon-->Developer tab: Click Macros button-->Click Run-->Wait for 4 mins")


# def draft_attachment(file_path):
#     if not os.path.exists(file_path):
#         print('file is not found')
#         return
#
#     with open(file_path, 'rb') as upload:
#         media_content = base64.b64encode(upload.read())
#
#     data_body = {
#         '@odata.type': '#microsoft.graph.fileAttachment',
#         'contentBytes': media_content.decode('utf-8'),
#         'name': os.path.basename(file_path)
#     }
#     return data_body
#
#
# APP_ID = '<app id>'
# SCOPES = ['Mail.Send', 'Mail.ReadWrite']
#
# access_token = generate_access_token(app_id=APP_ID, scopes=SCOPES)
# headers = {
#     'Authorization': 'Bearer ' + access_token['access_token']
# }
#
# request_body = {
#     'message': {
#         # recipient list
#         'toRecipients': [
#             {
#                 'emailAddress': {
#                     'address': 'gnutter@schools.nyc.gov'
#                 }
#             }
#         ],
#         # email subject
#         'subject': 'Mandated Services updates for {0}'.format(datetime.date.today()),
#         'importance': 'normal',
#         'body': {
#             'contentType': 'HTML',
#             'content': '<b>Be Awesome</b>'
#         },
#         # include attachments
#         'attachments': [
#             draft_attachment(r'C:\Users\Ywang36\Desktop\PythonPractice\fibonacci.py'),
#             # draft_attachment('image.png')
#         ]
#     }
# }
#
# GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'
# endpoint = GRAPH_ENDPOINT + '/me/sendMail'
#
# response = requests.post(endpoint, headers=headers, json=request_body)
# if response.status_code == 202:
#     print('Email sent')
# else:
#     print(response.reason)



