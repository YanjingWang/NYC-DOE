import re
# literal search
text_to_search = """
abcdefghigklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
haha HaHa
MetaCharacers (nEED TO BE ESCAPED):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com

321-555-4321
123.555.1234
123--555--1234
800-555-4321
900-555-4321


Mr.Shafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr.T

cat
mat
pat
bat
"""

urls = """
https://youtube.com
https://www.nasa.gov
https://www.google.com
http://coreyms.com
"""

sentence = 'Start a sentence and then bring it to an end'

print('\tTab')
print(r'\tTab')
# pattern = re.compile(r'abc')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\bHa')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#
# print(text_to_search[1:4])


pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

print(sentence[0:5])

pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

print(sentence[41:44])

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[1-5]')
pattern = re.compile(r'[a-zA-Z]')
pattern = re.compile(r'[^a-zA-Z]')
pattern = re.compile(r'[^b]at')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'Mr\.?')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print(text_to_search[153:165])
print(text_to_search[166:178])

with open('email.csv','r',encoding='utf-8') as f:
    contents = f.read()
    pattern = re.compile(r'\.com')
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)

with open('email.csv','r',encoding='utf-8') as f:
    contents = f.read()
    pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
# group method
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))  # entire url match
    print(match.group(1))  # optional www
    print(match.group(2))  # domain name
    print(match.group(3))   # top level domain name


# reformat
subbed_urls = pattern.sub(r'\2\3',urls)  # substitute out group2 and group3 for
# all of our matches in urls so every time it finds a match it will replace that match
# with group2 domain name and group 3 top level domain name
print(subbed_urls)

"""
methods: 
findall
match
search
flag
"""

pattern = re.compile(r'start',re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)
