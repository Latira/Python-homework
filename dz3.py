# Task 3 "Задачи на многомерные списки" with functions
# Option 2 Симметричная матрица. Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

import numpy as np

def array_input(I):
    A=[]
    for i in range(I):
        a = []
        for j in range(I):
            b = int(input(f'Enter the {str(i + 1)},{str(j + 1)} element of the list '))
            a.append(b)
        A.append(a)
    return A
def array_print(*args):
    for argument in args:
        print(argument)
def symmetry_check(I):
    def sum_for_check(num):
        if num==2:
            return 1
        else:
            return num-1 + sum_for_check(num-1)
    n=0
    for i in range(I):
        for j in range(I):
            if i!=j and A[i,j]==A[j,i]:
                n=n+0.5
    if sum_for_check(I) == n:
        return f'The square array \n {A} \n is symmetrical'
    else:
        return f'The square array \n {A} \n  is not symmetrical'

A=np.array(array_input(int(input('Enter the number of rows/columns: '))))
print()
if len(A) < 2:
    array_print('Square array is not found')
else:
    array_print('Square array', A)
    print()
    print(symmetry_check(len(A)))