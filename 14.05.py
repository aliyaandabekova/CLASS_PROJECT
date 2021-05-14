"""

Быки и коровы

Загадывается четырехзначное случайное число - программой.
Пользователю дается шанс угадать это число.
Если угадана и цифра и позиция - 1 бык
Если угадана только цифра - 1 корова
Всего 5 попыток угадать число


"""

import random



list1 = random.sample([0,1,2,3,4,5,6,7,8,9],4)
print(list1)

# list_input = input().split()
# new_list_input = []
#
# for i in list_input:
#     i = int(i)
#     new_list_input.append(i)
# print(new_list_input)

# for index,number in enumerate(list_input):
#     list_input[index] = int(number)
for t in range(5):
    bulls_count = 0
    cows_count = 0
    list_input = input().split()
    new_list_input = []

    for i in list_input:
        i = int(i)
        new_list_input.append(i)


    for n1 in list1:
        for n2 in new_list_input:
            if n1 == n2 and list1.index(n1) != new_list_input.index(n2):
                cows_count += 1
            if n1 == n2 and list1.index(n1) == new_list_input.index(n2):
                bulls_count += 1
    print('коров = ',cows_count)
    print('быков = ',bulls_count)

