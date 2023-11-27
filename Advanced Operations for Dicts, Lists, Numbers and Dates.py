# import os
# os.rename('SortClassObjects.py', 'Advanced Operations for Dicts, Lists, Numbers and Dates.py')

person = {'name':'John','age':23}

sentence = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} yars old.'.format(person)
print(sentence)
# number the placeholders
sentence = 'My name is {1} and I am {0} years old.'.format(person['name'],person['age'])
print(sentence)

tag = 'Hi'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)


l = ['Jennifer',23]
sentence  = 'My name is {0[0]} and I am {0[1]}'.format(l)
print(sentence)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack',33)
sentence  = 'My name is {0.name} I AM {0.age} years old'.format(p1)
print(sentence)

for i in range(1,11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

pi = 3.1415926
sentence = 'Pi is equal tp {:2f}'.format(pi)
print(sentence)

sentence = '1MB is equal tp {:,}'.format(100000**2)
print(sentence)

sentence = '1MB is equal tp {:,.2f}'.format(100000**2)
print(sentence)

import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)

my_date = datetime.datetime(2016,9,24,12,30,45)
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# day of the year
sentence  =  '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
