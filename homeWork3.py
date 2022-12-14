#1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# numbers = [2, 3, 5, 9, 3, 3]

i = 0
summa = 0
for numbers[i] in numbers:
    i+=1
    if i % 2 != 0:
       summa = summa + int(numbers[i])       
print(f'Сумма цифр на нечётных позициях = {summa}')


#2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6]
multy_numbers = []
for i in range((len(numbers)+1)//2):
    multy_numbers.append(numbers[i]*numbers[len(numbers)-1-i])
print(multy_numbers)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

my_list = [1.11, 1.02, 3.1, 5.12]
min = 1
max = 0
for i in my_list:
    i+= 1
    if min >= i - int(i):
        min = i - int(i)
    if max <= i - int(i):
        max = i - int(i)  
res = max - min    
print(f'Разность между максимальной дробной частью {round(max, 2)} и минимальной дробной частью {round(min, 2)} = {round(res, 2)}')


#4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

binary = ''
n = int(input('Введите десятичное число: '))
while n != 0:
    binary = str(n % 2) + binary
    n //= 2
print(f'Двоичное число: {binary}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите длину ряда: '))
x = k
f1 = 0
f2 = 1
fi = []
j = 1            
fib1 = 0
fib2 = 1
while j < x:
  fib1, fib2 = fib2, fib1 - fib2 
  fi.append(fib2)
  j += 1
fi.reverse()
i = 2
while i < k + 1:
  f1, f2 = f2, f1 + f2 
  fi.append(f2)
  i += 1
fi.insert(k-1, 1)
fi.insert(k, 0)
fi.insert(k+1, 1)
print(fi)
