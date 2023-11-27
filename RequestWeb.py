# pip install requests
import requests

# # r = requests.get('https://xkcd.com/353/')
# # r = requests.get('https://imgs.xkcd.com/comics/python.png')
# payload = {'page': 2, 'count': 25}
# # r = requests.get('https://httpbin.org/get?page=2&count=25')  # url parameter
# r = requests.get('https://httpbin.org/get', params=payload)  # url parameter
#
# print(r)
# print(dir(r))
# print(help(r))
#
# print(r.text)  # get html , html parser
# print(r.content)  # bytes of images
#
# # download images
# with open('comic.png', 'wb') as f:
#     f.write(r.content)
#
# print(r.status_code)  # 200 are success, 300 redirect, 400 client error, 500 server error
# print(r.ok)
# print(r.headers)
# print(r.url)

# httpbin.org
payload = {'username':'charlotte','password':'testing'}
r = requests.get('https://httpbin.org/post', data=payload)  # 405 error
r_dict = r.json()
print(r.text)
# print(r.json())
print(r_dict['form'])
