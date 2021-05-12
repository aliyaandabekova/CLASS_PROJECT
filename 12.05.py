class Employee(object):
    id = 0

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.email = f'{self.first}-{self.last}@saturnsoft.sat'
        self.age = age
        Employee.id += 1
        self.emp_id = Employee.id


    def desc(self):
        print('emp desc')


class Developer(Employee):

    def __init__(self,first:str,last:str,age:int,
                 work_exp:int,exp:list,prog_lang:str,position:str):
        super().__init__(first,last,age)
        self.work_exp = work_exp
        self.exp = exp
        self.prog_lang = prog_lang
        self.__position = position
        self.__salary = 50001


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,new_salary:int):
        if new_salary >= 50000:
            self.__salary = new_salary
        else:
            print('Введите значение больше 50.000')

    @salary.deleter
    def salary(self):
        self.__salary = 50000


    @property
    def position(self):
        return self._position

    @position.setter


import random

erbol = Developer('Erbol','Esenbaev',9999,0,[],'python','team lead')
cholpon = Developer('Cholpon','Kaimova',9999,0,[],'python','team lead')
aliya = Developer('Aliya','Andabekova',9999,0,[],'python','senior')
begimai = Developer('Begimai','Zhumakova',9999,0,[],'python','intern')
zinko = Developer('Vova','Zinkovsky',9999,0,[],'python','intern')
list1 = [erbol,cholpon,aliya,begimai,zinko]
for i in list1:
    random_salary = random.randint(50001,400000)
    i.salary = random_salary
dict1 = {erbol:'399K',cholpon:'209K',aliya:'100K',begimai:'70K',zinko:'60K'}


for obj in dict1:
    dict1[obj] = int(dict1[obj].replace('K','000'))
    if dict1[obj] != obj.salary:
        dict1[obj] = obj.salary
        if obj.salary > 300000:
            obj.position = 'team lead'
        elif  150000 <= obj.salary  <= 220000:
            obj.position = 'senior'
        elif 100000 <= obj.salary <= 150000:
            obj.position = 'middle'
        elif 50001 <= obj.salary <= 100000:
            obj.position = 'junior'
print(dict1)
print(erbol.__dict__)













