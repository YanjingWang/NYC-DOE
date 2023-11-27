class Employee:

    def __init__(self, first, last):
        # init func is like constructor
        # call instance self now #arguments
        # we can create email by first and last name
        # set the instance variable inside init func
        self.first = first  # self.fname = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def fullname(self):  # each func takes self as first argument
        # apply to all instance
        # this is a method instead of attribute
        return '{} {}'.format(self.first, self.last)

    @property  # use decorator to use it as attribute so when value changes it all changes everywhere
    def email(self):  # each func takes self as first argument
        # apply to all instance
        # this is a method instead of attribute
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name!")
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)  # Jim
# print(emp_1.email)  # John.Smith@gmail.com
# print(emp_1.fullname())  # Jim Smith

print("###################compare method and attributes###############################")

print(emp_1.first)  # JIm
# print(emp_1.email())  # John.Smith@gmail.com
# print(emp_1.fullname())  # Jim Smith

print("###################use email as attribute-->decorator @property###############################")

print(emp_1.first)  # Jim
print(emp_1.email)  # Jim.Smith@gmail.com
# print(emp_1.fullname())  # Jim Smith

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print("########################deleter################################################")
del emp_1.fullname
