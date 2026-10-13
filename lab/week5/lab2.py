#직원과 매니저 (p.562)

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def getSalary(self):
        salary = super().getSalary()
        return salary + self.bonus

    def __str__(self):
        return f"이름 : {self.name}; 월급 : {self.salary}; 보너스 : {self.bonus}"

def test():
    kim = Manager("Kim", 2000000, 1000000)
    print(kim)

if __name__ == "__main__":
    test()