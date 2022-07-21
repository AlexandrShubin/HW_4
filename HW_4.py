# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141

from decimal import Decimal, getcontext
number = Decimal("3.1415926535")

print(number.quantize(Decimal('0.001')))

# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список 
# простых множителей числа N.

number=int(input("Integer: "))
for i in range(1, number+1):
    if(number%i==0):
        print(i)

# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

lst = [8, 3, 4, 5, 7, 3, 5, 2]

used = set()
unique = [x for x in lst if x not in used and (used.add(x) or True)]
print(unique)

from collections import Counter
counter = Counter(lst)

unique = list(counter)
print(unique)

single = [x for x,n in counter.items() if n==1]
print(single)

# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# class Polynomial:
#     def __init__(self, koef):
#         self.koef = koef
 
#     def __call__(self, x):
#         s = 0
#         for i in range(len(self.koef)):
#             s += self.koef[i] * pow(x, i)
#         return s
 
#     def __add__(self, other):
#         st = []
#         k = Polynomial(st)
#         if len(self.koef) < len(other.koef):
#             m = len(self.koef)
#         else:
#             m = len(other.koef)
#         for i in range(m):
#             st.append(self.koef[i] + other.koef[i])
#         if len(self.koef) > m:
#             st += self.koef[m::]
#         else:
#             st += other.koef[m::]
#         k.koef = st
#         return k

# 5. Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

