n = input()
 
suma = 0
mult = 1
 
for digit in n:
    if digit.isdigit():
        suma += int(digit)
 
print("Сумма цифр:", suma)
