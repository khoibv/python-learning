class EmployeeClass:
    """Common base class for all employee"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        EmployeeClass.empCount += 1

    @staticmethod
    def total_emp():
        print('Total emp: %d' % EmployeeClass.empCount)

    def show(self):
        print('{name: %s, salary: %s}' % ( self.name, self.salary ))

