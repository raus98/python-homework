class Employee():
    def __init__(self, code, name, salary):
        self._code = code
        self._name = name
        self._salary = salary

    def get_code(self):
        return self._code

    def set_code(self, x):
        self._code = x

    def get_name(self):
        return self._name

    def set_name(self, x):
        self._name = x

    def get_salary(self):
        return self._salary

    def set_salary(self, x):
        self._salary = x

    def raiseSalary(self, amount: float):
        self._salary += amount
        print("Da tang luong")

    def showInfo(self):
        print("ID: " + str(self._code), end="  |  ")
        print("Ho va ten: " + str(self._name), end="  |  ")
        print("Luong: " + str(self._salary))

def create(n, main_list: list):
    for i in range(0, n):
        main_list.append(Employee(int(input("ID: ")),
                                  str(input("Name: ")),
                                  int(input("Salary: "))))

def showAll(n, main_list: list):
    for i in main_list:
        i.showInfo()
    print("//////////////////////////////////////////////")

def takeThird(val):
    return val[2]

def sorter(n, main_list: list):
    sorted_list = sorted(main_list, key=lambda employee: employee._salary, reverse=True)
    return sorted_list





