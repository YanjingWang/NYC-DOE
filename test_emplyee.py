import unittest
from EmployeeClass import Employee
from unittest.mock import patch
import requests




# class TestEmployee(unittest.TestCase):
#     """setup and teardown"""
#
#     def tearDown(self) -> None:  # run after every single test
#         pass
#
#     def test_email(self):  # all test should start with test instead of something else
#         emp_1 = Employee('Corey', 'Schafer', 50000)
#         emp_2 = Employee('Sue', 'Smith', 60000)
#
#         self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
#         self.assertEqual(emp_2.email, 'Sue.Smith@email.com')
#
#         emp_1.first = 'John'
#         emp_2.first = 'Jane'
#
#         self.assertEqual(emp_1.email, 'John.Schafer@email.com')
#         self.assertEqual(emp_2.email, 'Jane.Smith@email.com')
#
#     def test_fullname(self):  # all test should start with test instead of something else
#         emp_1 = Employee('Corey', 'Schafer', 50000)
#         emp_2 = Employee('Sue', 'Smith', 60000)
#
#         self.assertEqual(emp_1.fullname, 'Corey Schafer')
#         self.assertEqual(emp_2.fullname, 'Sue Smith')
#
#         emp_1.first = 'John'
#         emp_2.first = 'Jane'
#
#         self.assertEqual(emp_1.fullname, 'John Schafer')
#         self.assertEqual(emp_2.fullname, 'Jane Smith')
#
#     def test_apply_raise(self):  # all test should start with test instead of something else
#         emp_1 = Employee('Corey', 'Schafer', 50000)
#         emp_2 = Employee('Sue', 'Smith', 60000)
#
#         emp_1.apply_raise()
#         emp_2.apply_raise()
#
#         self.assertEqual(emp_1.pay, 52500)
#         self.assertEqual(emp_2.pay, 63000)
#
#
# if __name__ == '__main__':
#     unittest.main()


class TestEmployee(unittest.TestCase):
    """setup and teardown"""

    @classmethod
    def setUpClass(cls):  # run before every single test
        print('setupClass')

    @classmethod
    def tearDown(cls):  # run after every single test, create test directory or test databases to hold files
        #  you can also delete all of those so that you have a clean slate for the next test
        print('teardownClass')

    def setUp(self):  # run before every single test
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self) -> None:  # run after every single test, create test directory or test databases to hold files
        #  you can also delete all of those so that you have a clean slate for the next test
        pass

    def test_email(self):  # all test should start with test instead of something else
        # self.emp_1 = Employee('Corey', 'Schafer', 50000)
        # self.emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'  # set these as instance attributes
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):  # all test should start with test instead of something else
        # self.emp_1 = Employee('Corey', 'Schafer', 50000)
        # self.emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):  # all test should start with test instead of something else
        # self.emp_1 = Employee('Corey', 'Schafer', 50000)
        # self.emp_2 = Employee('Sue', 'Smith', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    ## def test_monthly_schedule(self):


if __name__ == '__main__':
    unittest.main()
