Li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_Li = sorted(Li)  # sorted func, returns a new sorted list, so we can assign it to a variable
# print('Sorted Variable:\t',s_Li)
print(
    Li.sort(reverse=True))  # None sort method ust sort the list in place and return None, don't expect a list returned
print('Original Variable:\t', Li)
s_Li = sorted(Li, reverse=True)
print('Sorted Variable:\t', s_Li)

"""sorted func is better because we can pass in any iterable, sort method works specifically o  the list """

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort()
# print(tup.sort())  # wrong

s_tup = sorted(tup)
print('Tuple\t', s_tup)

dict = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_dict = sorted(dict)
print('Dict\t', s_dict)  ## just sort the keys

# sort list as absolute value
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs, reverse=True)
print('Abs value\t', s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):  # hww we want this func represented print out the screen
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


# s_employees = sorted(employees.name) doesn't work don't know how to sort, we need key to sort these on
# key takes a func that takes each element of our list and returns what we want to sort on, above we used build-in func
# below we use custom function
def e_sort(emp):
    return emp.salary


s_employees = sorted(employees, key=e_sort)
print(s_employees)

s_employees = sorted(employees, key=lambda e: e.age)
print(s_employees)

from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('name'))
print(s_employees)
