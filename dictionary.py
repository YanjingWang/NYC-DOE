# hashmap associate array
student = {'name': 'john', 'age': 25, 'courses': ['math', 'CS']}
print(student)
print(student['name'])
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'not found'))

student['phone'] = '555-555-5555'
student['name'] = 'Jane'
print(student)

student.update({'name': 'Jennifer', 'age': 26, 'phone': '123-456-7890'})
print(student)

# del student['age']
# print(student)
#
# afterpop = student.pop('phone')
# print(afterpop)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)
for key, value in student.items():
    print(key, value)
