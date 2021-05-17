import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee('Anna', 'Black', 10000)

    def test_email(self):
        self.assertEqual(self.classTest.email, 'Anna.Black@email.com')

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, 'Anna Black')

    def test_apply_raise(self):
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 10500)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock1):
        mock1.return_value.ok = True
        self.assertEqual(self.classTest.monthly_schedule('May'), mock1().text)
        mock1.return_value.ok = False
        self.assertEqual(self.classTest.monthly_schedule('June'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
