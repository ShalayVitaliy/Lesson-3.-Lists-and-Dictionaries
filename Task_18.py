# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


Ai = input("Enter integers: ").split()
A = list(map(int, Ai))
print(A)
X = int(input("Enter what number you want to find: "))
min = abs(X - A[0])
index = 0
for i in range(1, len(A)):
    counter = abs(X - A[i])
    if counter < min:
        min = counter
        index = i
print(f'Число {A[index]} в списке list наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')

