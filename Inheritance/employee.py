class Employee:
    """Employee"""
    __id = 100  # must change name otherwise a recursive overflow error occurs

    def __init__(self, name, job_title):
        self.__id = Employee.__id
        Employee.__id += 1
        self.__name = name
        self.__job_title = job_title

    def __str__(self):
        return "ID #{:d}: {:s}({:s}, {:s})".format(self.id, self.name, self.job_title, self.employee_type)

    def __repr__(self):
        return str({"id": self.id, "name": self.name, "job_title": self.job_title})

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, new_title):
        self.__job_title = new_title

    @property
    def employee_type(self):
        return "unknown"

    def calculate_pay(self):
        raise NotImplementedError("Employee subclasses must implement calculate_pay()")
