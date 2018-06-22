from EmployeeClass import EmployeeClass
from ManagerClass import ManagerClass
from Database import DatabaseConnect

def test_employee():
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

    print("Employee.__doc__:", EmployeeClass.__doc__)
    print("Employee.__module__:", EmployeeClass.__module__)
    print("Employee.__name__:", EmployeeClass.__name__)
    print("Employee.__bases__:", EmployeeClass.__bases__)
    print("Employee.__dict__:", EmployeeClass.__dict__)


def test_manager():
    mgr1 = ManagerClass('tungnk', 1000, 'OSD')
    mgr1.show()
    print(dir(mgr1))

def test_database():
    db = DatabaseConnect()
    db.work_with_ddl()


# test_employee()
# test_manager()
test_database()