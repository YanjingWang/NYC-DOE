# sequential data
# unordered collections of values with no duplicates

courses = ['history', 'math', 'Physics', 'CS']
courses2 = ['Education', 'Psychology']
num = [1, 5, 9, 3]
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])  # print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)
courses.insert(0, 'Art')  # insert value to specific position
print(courses)
courses.insert(0, courses2)  # insert list in another list
print(courses)
courses.remove(courses2)  # remove values
print(courses)
courses.extend(courses2)  # multiple values to add in original list
print(courses)
courses.pop()  # remove the last value of list, use it in stack or queue
popped = courses.pop()  # keep popping until your list is empty
print(popped)
print(courses)

courses.reverse()
print(courses)
courses.sort(reverse=True)  # sort list in desc order
print(courses)
num.sort(reverse=True)
print(num)

# use sorted function to avoid changing original list
sorted(courses)
print(courses)
sorted_courses = sorted(courses)
print(sorted_courses)

print(min(num))
print(max(num))
print(sum(num))

print(courses.index('CS'))  # find the index of a value in the list
print('Art' in courses)
print('Math' in courses)
print("##############loop through each item####################")
for item in courses:
    print(item)
print("##############enumerator#################################")
for index, course in enumerate(courses, start=1):
    print(index, course)
print("##############turn list into strings separated by a certain value###################")
course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)

# tuples are immutable
# mutable issue
# list_1 = ['history', 'math', 'physics', 'CS']
# list_2 = list_1
#
# list_1[0] = 'art'
# print(list_1)
# print(list_2)
print("#############use tuple if just loop through or access########################")
# tuple_1 = ('history', 'math', 'physics', 'CS')
# tuple_2 = tuple_1
#
# tuple_1[0] = 'art'  # TypeError: 'tuple' object does not support item assignment so tuple doesn't have a lot of
# methods
# print(tuple_1)
# print(tuple_2)

print("#############sets are unordered and no duplicates##############################")
print("#######test a value is part of set or remove duplicates########################")
# each execution has different order
set_1 = {'history', 'math', 'physics', 'CS', 'math'}
print(set_1)
print('Math' in set_1)
# membership test
set_2 = {'art', 'design', 'history', 'math'}
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))

print("#######create empty lists, sets,tuples##############")
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # this is wrong, this is a dict
empty_set = set()

