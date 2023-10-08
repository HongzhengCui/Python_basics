from employee import Employee
from decimal import Decimal

class SalariedEmployee(Employee):
    def __init__(self, name, job_title, annual_pay_rate):
        super().__init__(name, job_title)
        self.__annual_pay_rate = Decimal(annual_pay_rate)

    @property
    def employee_type(self):
        return "salaried"

    @property
    def annual_pay_rate(self):
        return self.__annual_pay_rate

    def calculate_pay(self):
        return self.__annual_pay_rate / 24