
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name :{self.name}\nSalary :{self.salary}"

    def __eq__(self, other):                # even works for not equal
        return self.salary == other.salary

    def __gt__(self, other):                # even works for less than
        return self.salary > other.salary


emp1 = Employee("Jack", 90000)
print(emp1)

print("-" * 40)
emp2 = Employee("Jane", 95000)
print(emp2)

print("-" * 40)
if emp1 == emp2:
    print("{} salary of {} is equal to {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))
else:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))

print("-" * 40)
if emp1 != emp2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary,
                                                                emp2.name, emp2.salary))
else:
    print("{} salary of {} is equal to {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))

print("-" * 40)
if emp1 > emp2:
    print("{} salary of {} is Greater Than {} salary of {}".format(emp1.name, emp1.salary,
                                                                emp2.name, emp2.salary))
else:
    print("{} salary of {} is Less Than {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))

print("-" * 40)
if emp1 < emp2:
    print("{} salary of {} is Less Than {} salary of {}".format(emp1.name, emp1.salary,
                                                                emp2.name, emp2.salary))
else:
    print("{} salary of {} is Greater Than {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))
