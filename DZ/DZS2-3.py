#Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

import random

list_number_of_elements = int(input("Количество элементов (целое положительное число): \n"))
if list_number_of_elements <= 0:
    print("Введено отрицательное число")

random_list = []
for i in range(0, list_number_of_elements):
    random_number = random.randint(-100, 100)
    random_list.append(random_number)
print(random_list)

new_random_list = []
for each in random_list:
    new_random_list.append(each)
    if each < 0:
        new_random_list.append(0)
print(new_random_list)