from urllib import request
import json

urlopen = request.urlopen("http://www.google.com")
print(urlopen.getcode())
print(urlopen.read())
data = urlopen.read()
jsonData = json.loads(data)
print(json)

for j in json:
    general = j["setup"]
    punchline = j["punchline"]

 class

