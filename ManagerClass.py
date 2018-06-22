from EmployeeClass import EmployeeClass


class ManagerClass(EmployeeClass):
    def __init__(self, name, salary, dept_name):
        super().__init__(name, salary)
        self.dept_name = dept_name

    def show(self):
        super().show()
        print('and department is %s' % self.dept_name)
