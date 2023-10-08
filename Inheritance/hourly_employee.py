from decimal import Decimal
from employee import Employee


class HourlyEmployee(Employee):
    """Hourly Employee"""

    def __init__(self, name, job_title, hourly_rate):
        super().__init__(name, job_title)
        self.__hourly_rate = Decimal(hourly_rate)
        self.__hours_worked = None

    @property
    def employee_type(self):
        return "hourly"

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        self.__hourly_rate = new_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, new_hours):
        self.__hours_worked = Decimal(new_hours)

    def calculate_pay(self):
        assert type(self.hours_worked) is Decimal, "Hours worked not established"
        hours = self.hours_worked
        overtime_hours = Decimal(0)
        if hours > 40:
            overtime_hours = hours - Decimal(40.0)
            hours = Decimal(40.0)
        return hours * self.hourly_rate + overtime_hours * self.hourly_rate * Decimal(1.5)
