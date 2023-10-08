from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):
    def setUp(self):
        Employee._Employee__id = 100

    def test_create(self):
        import ast

        a = Employee("Steve", "Programmer")
        b = Employee("Christine", "Project Manager")
        self.assertNotEqual(a.id, b.id, "IDs are not unique")
        self.assertEqual(a.name, "Steve")
        self.assertEqual(b.name, "Christine")
        self.assertEqual(a.job_title, "Programmer")
        self.assertEqual(b.job_title, "Project Manager")
        self.assertEqual(str(a), "ID #100: Steve(Programmer, unknown)")
        self.assertEqual(ast.literal_eval(repr(b)), {'id': 101, 'name': 'Christine', 'job_title': 'Project Manager'})

    def test_calculate_pay_not_implemented(self):
        a = Employee("Steve", "Programmer")
        with self.assertRaises(Exception) as context:
            a.calculate_pay()

        self.assertTrue(type(context.exception) is NotImplementedError)
        self.assertTrue("must implement" in context.exception.args[0])

    def test_change_job_title(self):
        a = Employee("Steve", "Programmer")
        a.job_title = 'Senior Programmer'
        self.assertEqual(a.job_title, ' Senior Programmer')
        self.assertEqual(str(a), "ID #100: Steve(Senior Programmer, unknown)")


if __name__ == '__main__':
    unittest.main(argv=['unittest', 'TestEmployee'], verbosity=2, exit=False)
