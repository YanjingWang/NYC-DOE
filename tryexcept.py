# f = open('data_.csv')

try:
    f = open('data.csv')
    if f.name == 'data_.csv':
        raise Exception  # manually raise exception
    # var = bad_var
except Exception as e:  # catch a lot of error
    print(e, "Error: this file doesn't exist")  # specific error goes first
except Exception as e:
    print(e, "sorry.Something went wrong")
else:  # if try block doesn't raise any error, it executes else block
    print(f.read())
    f.close()
finally:  # finally runs whatever happens
    print("executing finally.close database")

# raise error on your own
