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


emp1 = EmployeeClass("khoibv", 100)
emp2 = EmployeeClass("tuannm", 200)
emp3 = EmployeeClass("trungpt", 300)


emp1.show()
emp2.show()
emp2.show()
EmployeeClass.total_emp()
emp1.age = 40
if hasattr(emp2, 'age'):
    print('age: %d' % emp2.age)
else:
    print('Not found age information')
print(dir(emp1))
