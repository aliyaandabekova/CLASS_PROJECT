class Employee:
    """
    Описание сотрудников нашей компании!
    """
    def __init__(self,full_name:str,age:int,email:str,address:str,phone:str,position:str):
        self.full_name = full_name
        self.age = age
        self.email = email
        self.address = address
        self.phone = phone
        self.position = position
        self.salary = 0
    def __repr__(self):
        return f'Сотрудник: {self.full_name}'
    def set_salary(self):
        if self.position == 'developer':
            self.salary = 100000
        elif self.position == 'manager':
            self.salary = 90000
    def description(self):
        print(f'Имя: {self.full_name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}')
john = Employee('john snow',18,'winteriscome@gmail.com','winterfell','+123456','developer')
denis = Employee('deniska',20,'manager@gmail.com','moscow','+8999123321','manager')
list1 = [john,denis]
print(type(list1[0]))