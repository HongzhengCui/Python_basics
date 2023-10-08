import unittest
from hourly_employee import HourlyEmployee
from employee import Employee


class TestHourlyEmployee(unittest.TestCase):
    def setUp(self):
        Employee._Employee__id = 100

    def test_create(self):
        a = HourlyEmployee("Max", "System Administrator", 65.0)
        self.assertEqual(a.name, "Max")
        self.assertEqual(a.job_title, "System Administrator")
        self.assertEqual(str(a), "ID #100: Max(System Administrator, hourly)")

    def test_compute_pay_no_hours(self):
        a = HourlyEmployee("Max", "System Administrator", 65.0)
        with self.assertRaises(Exception) as context:
            a.calculate_pay()

        self.assertTrue(type(context.exception) in [TypeError, AssertionError])

    def test_compute_pay(self):
        a = HourlyEmployee("Max", "System Administrator", 65.0)
        a.hours_worked = 20
        self.assertEqual(a.calculate_pay(), Decimal(1300.0), "Pay not correct")
        a.hours_worked = 40
        self.assertEqual(a.calculate_pay(), Decimal(2600.0), "Pay not correct")

    def test_compute_pay_with_overtime(self):
        a = HourlyEmployee("Max", "System Administrator", 65.0)
        a.hours_worked = 60
        self.assertEqual(a.calculate_pay(), Decimal(4550.0), "Pay not correct")

    def test_employee_types(self):
        a = HourlyEmployee("Max", "System Administrator", 65.0)
        b = Employee("Cindy", "Sales Manager")
        self.assertEqual(a.employee_type, "hourly")
        self.assertNotEqual(a.employee_type, b.employee_type)


if __name__ == '__main__':
    unittest.main(argv=['unittest', 'TestHourlyEmployee'], verbosity=2, exit=False)
