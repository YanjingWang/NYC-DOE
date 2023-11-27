language = 'Java'
if False:
    print('conditional was true')

if language == 'Python':
    print('language is Python')
elif language == 'Java':
    print('language is Java')
else:
    print('No match')
# and or not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('bad creds')

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)  # two different memory
b = a
print(id(a))
print(id(b))
print(a is b)


# false condition:
# false
# None
# Zero of numeric value type
# Any empty sequences. Eg. '', (), []
# Any empty mapping. Eg. {}



