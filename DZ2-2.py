# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

number = int(input('введите число N'))
count = 1
sum = 1
while count <= number:
    for i in range(1,number+1):
        sum = sum*i
        print(sum)
        count += 1