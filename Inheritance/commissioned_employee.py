from decimal import Decimal
from salaried_employee import SalariedEmployee

class CommissionedEmployee(SalariedEmployee):
    def __init__(self, name, job_title, annual_pay_rate, period_gross_sales):
        super().__init__(name, job_title, annual_pay_rate)
        self.__period_gross_sales = Decimal(str(period_gross_sales))

    def calculate_pay(self):
        salaried_pay = super().calculate_pay()
        commission = Decimal('0.05') * self.__period_gross_sales
        return salaried_pay + commission

    @property
    def employee_type(self):
        return "commissioned"

    @property
    def period_gross_sales(self):
        return self.__period_gross_sales
