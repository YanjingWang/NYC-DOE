# def hello_func():
#     pass
#
#
# hello_func()
# print(hello_func)  # in certain location in memory
# print(hello_func())  # no return value


def hello_func():
    print('hello function!')


hello_func()  # reuse code, keeping your code dry


def hola_function():
    return 'hola function.'


hola_function()  # just give string instead of doing anything else
print(hola_function().upper())  # just give string instead of doing anything else, so we need print to execute it


# we treat return value as datetype it is

def ciao_function(greeting, name='you'):
    return '{}, {} function.'.format(greeting, name)


print(ciao_function('ciao'))
print(ciao_function('ciao', name='Corey'))


def student_ifo(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # keyword dictionary


courses = ['math', 'art']
info = {'name': 'john', 'age': 22}
student_ifo('math', 'art', name='John', age=22)

student_ifo(*courses, **info)  # unpack the list and dictionary value

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(2017))
print(days_in_month(2017, 2))
