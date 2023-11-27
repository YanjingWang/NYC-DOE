# print("First Module's Name: {}".format(__name__))
"""
before run any code, Python sets up special variables like __name__
when we import modules we set this named variable to the name of the file
"""
"""
below codes tell us is file run directly by Python or is it being imported
"""

# def main():
#     print("First Module's Name: {}".format(__name__))
#
#
# if __name__ == '__main__':
#     main()
#     print("run directly")
# else:
#     print("run from import")


print("this will always be run")


def main():
    print("First Module's main method")


if __name__ == '__main__':
    main()
