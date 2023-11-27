
# firstPython.py is no longer being run directly by Python
import firstmodule

firstmodule.main()

print("Second module's name: {}".format(__name__))

