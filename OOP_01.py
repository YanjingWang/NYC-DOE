"""
class Employee:
    pass  # leave it empty for time being skip that for now


emp_1 = Employee()  # instance of class, unique locations in memory
emp_2 = Employee()

print(emp_1)
print(emp_2)

# instance variable and class variables
# manually set variables everytime, prone the mistake, a lot of codes

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'CSchafer@gmail.com'
emp_1.pay = 50000

emp_2.first = 'test'
emp_2.last = 'user'
emp_2.email = 'tuser@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

"""


#######################################################################################################################
class Employee:
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


emp_1 = Employee('Corey', 'Schafer', 50000)  # instance of class, unique locations in memory
emp_2 = Employee('test', 'user', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(' {} {} '.format(emp_1.first, emp_1.last))  # two placeholders
print(emp_1.fullname())  # this is a method instead of attribute
print(Employee.fullname(emp_1)) # need to declare which instance to pass in

# how to love type error: https://careerkarma.com/blog/python-typeerror-object-takes-no-arguments/
