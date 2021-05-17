import unittest
from homeworks.hw4_tests.hw4_tests_employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee('Anna', 'Black', 10000)

    def test_email(self):
        self.assertEqual(self.classTest.email, 'Anna.Black@email.com')

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, 'Anna', 'Black')

    def test_apply_raise(self):
        self.assertEqual(self.classTest.apply_raise, 10500)

    @patch('employee.requests.get')


