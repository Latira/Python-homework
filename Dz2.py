# Task 1 "Задачи на одномерные списки"
# Option 2 "Введите одномерный целочисленный список. Найдите наибольший нечетный элемент."
# "Найдите минимальный по модулю элемент списка."
n = int(input('Enter the size of the list: '))
A=[]
for i in range(n):
    a=int(input('Enter the '+ str(i+1) +' element of the list: '))
    A.append(a)
for i in range(n):
    if A[i]%2 == 1:
        loe=A[i]   # наибольший нечетный элемент. По умолчанию присваиваем значение первого нечетного элемента в списке.
        break
    else: loe=0
mme=abs(A[0])   # минимальный по модулю элемент. По умолчанию присваиваем значение первого элемента списка
for i in range(n):
    print(A[i])
    if A[i]%2 == 1 and A[i]>loe:
        loe=A[i]
    if abs(A[i])<mme:
        mme=abs(A[i])
if loe != 0:
    print('The largest odd element: ',loe)
else: print('The largest odd element was not found') # если в списке только четные элементы
print('The minimum modulo element: ',mme)

# Task 2 "Задачи на многомерные списки"
# Option 3 "Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме элементов, стоящих на том же месте в 1-й и 2-й таблицах."
import numpy as np
print('First array')
I=int(input('Enter the number of rows: '))
J=int(input('Enter the number of columns: '))
A=[]
for i in range(I):
    a=[]
    for j in range (J):
        b=int(input('Enter the ' + str(i+1) + ', ' + str(j+1) + ' element of the list '))
        a.append(b)
    A.append(a)
print()
print('First original array')
for i in range(len(A)):
    for j in range (len(A[i])):
        print(str(A[i][j]) + ' ', end=''),
    print()
print()
print()
print('Second array')
I=int(input('Enter the number of rows: '))
J=int(input('Enter the number of columns: '))
C=[]
for i in range(I):
    c=[]
    for j in range (J):
        d=int(input('Enter the ' + str(i+1) + ', ' + str(j+1) + ' element of the list '))
        c.append(d)
    C.append(c)
print()
print('Second original array')
for i in range(len(C)):
    for j in range (len(C[i])):
        print(str(C[i][j]) + ' ', end=''),
    print()
An = np.array(A)
Cn = np.array(C)
E = An+Cn
print()
print()
print('Third array')
for i in range(len(E)):
    for j in range (len(E[i])):
        print(str(E[i][j]) + ' ', end=''),
    print()