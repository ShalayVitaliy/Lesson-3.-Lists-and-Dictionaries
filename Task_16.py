# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

size = int(input("Enter the legth of list: "))
n = int(input('What number do you want to count: '))
list = []
counter = 0 #Вводим счетчик числа встреч числа
for i in range(size):
    list.append(randint(0, 10))

print(list)
for i in range(size):
    if list[i] == n:        
        counter += 1
print(f'Число {n} встречается : {counter}')

