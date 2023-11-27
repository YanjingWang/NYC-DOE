# import os
# os.rename('stringdicttuple.py', 'liststringdicttuple.py')
"""enumerate can get index and value at the same time
for (i,score) in enumerate(nums):
    print(i,score)
"""
ch = '\n'
ch1 = '\''
ch2 = '\\'
ch3 = '\t'

print(ch, ch1, ch2)
print(ord('字'))  # character -->int
print(chr(97))  # int --> character

lower_char = 'x'
print(chr(ord(lower_char) - ord('x') + ord('X')))
print(lower_char.upper())

str = 'I will cut off Carlos s dick'
print(str.find('dick'))
str.replace('dick', 'cock')
print(str)
print(len(str))

# formatting string
str = 'I am %s, and my score is %d' % ('Charlotte', 100)
print(str)

str = 'I am {}, and my score is {}'.format('Charlotte', 100)
print(str)

# F string to format easily on Python 3.6
greeting = 'hello'
name = 'charlotte'
message = f'{greeting},{name}, welcome to this world!'
message = f'{greeting},{name.upper()}, welcome to this world!'
print(message)

# message needs to be saved as another variable after replace method
message = message.replace('charlotte','carlos')
print(message)

# reverse string
# np
s = 'carlosruizisanasshole'
result = ''
for i in range(len(s) - 1, -1, -1):
    result += s[i]
print(result)

# p
print(s[::-1])

# concatenate strings
strs = ['Carlos', 'has', 'big', 'dick']
# np
result = ''
for s in strs:
    result += s + ' '
print(result)

# p
result = ' '.join(strs)
print(result)

# dir() shows all the attributes and methods available to that string
print(dir(name))
# print(help(str))
"""
update variable != update the value of variable
change index ==> change the object
change object.name ==> change the object
change a1 = a2 ==> change the variable 
"""
list1 = [1, 2, 3, 4]
list2 = list1  # list1 and ist2 use same address in memory, never change address, address pointed to the object list
list2[0] = 100  # change the object
print(list1)
print(id(list1), id(list2))

num = 10
num2 = num
num2 = 20  # num2 address changes, reference changes
print(num)
print(id(num), id(num2))

"""
every address in tuple is immutable, but when use index we change the object each address pointed to 
"""
my_tuple = (1, 2, 'abc', [6, 7], 12.3, True)
my_tuple[3].append(20)
print(my_tuple)

# my_tuple[3] = [6,7,20]  # wrong because  create a new list with new address


tuple_1 = (12, 5, 6, True, 'hello', ['a', 'b'])
tuple_2 = 1, 2, 3, 4
tuple_3 = tuple('hello')  # ('h','e','l','l','o')
tuple_4 = (1,)  # have to use , to k now it's tuple

"""
we can only READ tuple 
"""
for x in tuple_2:
    print(x, end=' ')
print(tuple_2[0])

"""
Chapter 9: List
"""
list_1 = list('hello')
print(list_1)
list_2 = [12, 5, True, 'hello', [1, 2, 3]]
print(list_2)
print(list_2.index([1, 2, 3]))
if 'hello' in list_2:
    print(list_2.index('hello'))
    print(list_2.count('hello'))

# +,*, append, insert,extend
# interation, slice, in, index, count
# sliceing assignment, indexing assignment
# pop,remove,del
# len,sort,reverse


list_2[1:3] = [20, 30, 40, 1, 2, 3, 4]
print(list_2)
list_2.pop(2)  # pop the one it's index= 2, pop accepts index
print(list_2)

list_2.remove('hello')
print(list_2)  # remove accept value

del list_2[2:4]
print(list_2)

# list generator
# np
result = []
for i in range(101):
    if i % 5 == 0:
        result.append(i)
print(result)
# p
result = [i for i in range(101) if i % 5 == 0]
print(result)


class Student():
    def __init__(self, name, score=100):
        self.name = name
        self.score = score

    def speak(self):
        print(self.name, self.score)


def run_student_example1():
    print('Student example 1')
    student_1 = Student('Tom')
    student_2 = Student('Jack')
    student_1.speak()
    student_2.speak()

    student_2.name = 'Jerry'
    student_1.speak()
    student_2.speak()


def run_student_example2():
    print('Student example 2')
    student_1 = Student('Tom')
    student_2 = student_1  # share the same address
    student_1.speak()
    student_2.speak()

    student_2.name = 'Jerry'
    student_1.speak()
    student_2.speak()


def run_student_example3():
    print('Student example 3')
    student_1 = Student('Tom')
    student_2 = Student('Jack')
    student_1.speak()
    student_2.speak()

    t1 = student_1  # exchange the value
    student_1 = student_2
    student_2 = t1

    student_1.speak()
    student_2.speak()


run_student_example1()
run_student_example2()  #
run_student_example3()

"""Python all variable is reference soring object's address, use ID() or IS"""
"""slicing has new list"""
""" =  and pass value to parameter are copying reference """
