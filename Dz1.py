# Option 1 Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
"""k=0
m=int(input("Enter the first number"))
if m<0: k=k+1
n=int(input("Enter the second number"))
if n<0: k=k+1
p=int(input("Enter the third number"))
if p<0: k=k+1
print('The number of negative numbers: '+str(k)"""

# Option 2 Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.
"""a=int(input("Enter the first number a: "))
b=int(input("Enter the second number b: "))
c=int(input("Enter the third number c: "))
if a==b or a==c or b==c:
    print('Among given numbers there ara equals')
else: print('Among given numbers there ara no equals')"""

# Option 3 Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.
"""a=int(input("Enter the first number a: "))
b=int(input("Enter the second number b: "))
c=int(input("Enter the third number c: "))
if a!=0 and b!=0 and c!=0:
    c=(a*b*c)**(1/3)
    print('Geometric mean is ', c)
else:
    c=(a+b+c)/3
    print('arithmetic mean is ',c)"""

# Option 4 По номеру месяца напечатать пору года.
"""n = int(input("Введите номер месяца:"))
if n>0 and n<3 or n==12:
    print("Пора года - зима")
elif n>2 and n<6:
    print("Пора года - весна")
elif n>5 and n<9:
    print("Пора года - лето")
elif n>8 and n<12:
    print("Пора года - осень")
else:
    print("Номер месяца не подходит")"""

# Option 5 Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.
"""A=int(input("Enter the first number A: "))
B=int(input("Enter the second number B: "))
C=int(input("Enter the third number C: "))
D=int(input("Enter the forth number D: "))
if A%2!=0 or B%2!=0 or C%2!=0 or D%2!=0:
    print('There is at least one odd number among the given')
else:
    print('There are no odd ones among the given numbers')"""

# Option 6 Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?
n=int(input('Enter the three-digit number n: '))
ns=
for i in range(2):
    if n%(10**i) == 0 or n%(100**i) == 9:
        k=k+1
if k!=0:
    print("There are '0' or '9' among the digits of a given three-digit number")
else:
    print("There are no '0' or '9' among the digits of a given three-digit number")


# Option 7 В переменную Y ввести номер года. Определить, является ли год високосным.
# Option 8 Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
# Option 9 Проверить, является ли дробь A / B правильной.
# Option 10 Число делится на 3 тогда, когда сумма его цифр делится на 3. Проверить этот признак на примере заданного трехзначного числа. 
# Option 11 Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
# Option 12 Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?
# Option 13 Для натурального числа К напечатать фразу «мы нашли К грибов в лесу», согласовав окончание слова «гриб» с числом К.
# Option 14 Для целого числа К от 1 до 9 напечатать фразу «мне К лет», учитывая при этом, что при некоторых значениях К слово «лет» надо заменить на слово «год» или «года».
# Option 15 Определить есть ли среди заданных целых чисел A, B, C, D хотя бы одно чётное.
# Option 16 По введенному числу (от 0 до 7) напечатать название цифры.