# regular methods automatically take the instance as the first argument --self
# how to chang it and let methods take class as first argument?
# use Class method, turn a regular method into a class method add decorator at the top @classmethod CLS
# static methods don't pass anything automatically, so they behave like function

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # return to receive this object

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




emp_1 = Employee('Corey', 'Schafer', 50000)  # instance of class, unique locations in memory
emp_2 = Employee('test', 'user', 60000)
print("################################ class method to parse strings ###############################################")
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1)

print("################################### alternative constructor ###################################################")

new_emp_1 = Employee.from_string((emp_str_1))
print(new_emp_1)


print(new_emp_1.email)
print(new_emp_1.pay)

print("###############################################")

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

print(emp_1.__dict__)

Employee.set_raise_amt(1.05)  # classmethod, class is higher than instance, use it as alternative constructor
# Employee.raise_amount = 1.05 does the same
# emp_1.raise_amount = 1.05

print(Employee.raise_amount)  # 1.04 --> 1.05
print(emp_1.raise_amount)  # 1.04 -->1.05
print(emp_2.raise_amount)  # 1.04 --> 1.05

# if I only want to change instance attribute or only apply to subclasses


print(Employee.num_of_emps)

print("########################static methods don't operate on the instance or the class #############################")
import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
