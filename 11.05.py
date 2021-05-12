class Employee:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name
        self.age = age
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.getter
    def salary(self):
        return f'Зарплата сотрудника {self.full_name}: {self.__salary}'

    @salary.setter
    def salary(self, summ):
        if isinstance(summ,(int,float)) and summ > 0:
            self.__salary = summ
        else:
            print('summ - параметр имеет недопустимый вид!')

    @salary.deleter
    def salary(self):
        self.__salary = None


aliya = Employee('aliya', 'andabekova', 18)

print(aliya.salary)

print(aliya.__dict__)
del aliya.salary
print(aliya.__dict__)

