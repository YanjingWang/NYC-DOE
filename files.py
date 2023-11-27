# file = open("./machine-readable-business-employment-data-mar-2022-quarter.csv", "w")
# file = open("./data.csv", "w")
# w writing a appending r reading r+ for reading and writing

file = open("./data.csv", "r+")  # reading and writing
file.write("id,name,email\n")
file.write("1,Jamila,jamila@gmail.com\n")
file.write("2,Jamila,jamila@gmail.com\n")
file.close()  # everytime after write a file you have to close it

file = open("./data.csv", "r")
print(file.read())
file.close()

file = open("./data.csv", "r")
print(file.readline())
file.close()

file = open("./data.csv", "r")
for line in file:
    print(line)
file.close()

file = open("./data.csv", "r")
print(file.readlines())
file.close()

import os.path  # check file exists or not

filename = "./datatatata.csv"
if os.path.isfile(filename):
    with open(filename, "r") as file:  # avoid forgetting close file
        print(file.read())
else:
    print(f"filename {filename} doesn't exist")

"""
file objects
"""
f = open('data.csv', 'r')  # r+ read and write
print(f.name)
print(f.mode)
f.close()  # Close the file!!!

# context manager
with open('data.csv', 'r') as f:
    f_context = f.readline()
    for i in f:
        print(i)  # avoid memory issue
    # print(f_context)
print(f.close())
# print(f.read())

with open('data.csv', 'r') as f:
    f = f.read(5)
    print(f, end=' ')
