# class variable shared among all instances
"""
class Employee:
    raise_amount = 1.04  # class variable, avoid changing multiple locations

    def __init__(self, first, last, pay):
        # init func is like constructor
        # call instance self now #arguments
        # we can create email by first and last name
        # set the instance variable inside init func
        self.first = first  # self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):  # each func takes self as first argument
        # apply to all instance
        # this is a method instead of attribute
        return ' {} {} '.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)  # access through class or instance self.raise_amount


emp_1 = Employee('Corey', 'Schafer', 50000)  # instance of class, unique locations in memory
emp_2 = Employee('test', 'user', 60000)

print(emp_1.pay)  # 50000
emp_1.apply_raise()
print(emp_1.pay)  # 52000

print(emp_1.raise_amount)  # 1.04 access the class's raisemount attribute
print(emp_2.raise_amount)
print(Employee.raise_amount)

# when we try to access to an attribute, first it will check if an instance contain that attribute then a class
# or any class that it inherits from contains this attribute
# emp_1.raise_amount
# Employee.raise_amount

print(emp_1.__dict__)
print(Employee.__dict__)


Employee.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)  # 1.05
print(emp_1.raise_amount)  # 1.05
print(emp_2.raise_amount)  # 1.05

"""


class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # class variable, avoid changing multiple locations

    def __init__(self, first, last, pay):
        # init func is like constructor
        # call instance self now #arguments
        # we can create email by first and last name
        # set the instance variable inside init func
        self.first = first  # self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):  # each func takes self as first argument
        # apply to all instance
        # this is a method instead of attribute
        return ' {} {} '.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # access through class or instance self.raise_amount


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)  # instance of class, unique locations in memory
emp_2 = Employee('test', 'user', 60000)

print(emp_1.pay)  # 50000
emp_1.apply_raise()
print(emp_1.pay)  # 52000

print(emp_1.raise_amount)  # 1.04 access the class's raisemount attribute
print(emp_2.raise_amount)
print(Employee.raise_amount)

# when we try to access to an attribute, first it will check if an instance contain that attribute then a class
# or any class that it inherits from contains this attribute
# emp_1.raise_amount
# Employee.raise_amount

print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)  # 1.04
print(emp_1.raise_amount)  # 1.05
print(emp_2.raise_amount)  # 1.04

# if I only want to change instance attribute or only apply to subclasses


print(Employee.num_of_emps)
