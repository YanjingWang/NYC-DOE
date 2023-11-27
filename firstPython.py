# print("hello world")
def greet(name, age):
    print(f"hello {name} how are you?")
    print(f"I know your age = {age}")


# greet("Charlotte Wang",28)

def greet(name, age=22):
    print(f"hello {name} how are you?")
    print(f"I know your age = {age}")


# greet("Yanjing Wang")

def is_adult(age):
    if age >= 18:
        print(":)")
    else:
        print(":(")


is_adult(10)


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False  # Can return anything [], "", variable...


is_adult(10)  # the value can't be T or F
result = is_adult(10)
print(result)


def is_adult(age):
    return age >= 18


result = is_adult(20)
print(result)


def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return gender


print(convertGender('F'))


def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"gender {gender} is unknown"


print(convertGender('trans'))

# []. "".
# import math #import module
# print(math.log2(50))
# from math import isqrt

import calculator

print(calculator.add(2, 2))
print(calculator.subtract(2, 2))
print(calculator.multiply(2, 2))
print(calculator.divide(2, 2))

from calculator import divide

print(divide(9, 3))
