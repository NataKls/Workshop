#Вариант 13. Определить наименьший элемент каждой четной строки 
#матрицы А[М, N].
import random
n=int(input('Указать кол-во строк и столбцов: '))

A=[[random.randrange(9) for i in range(n)] for j in range(n)]
for row in A:
    print(*map('{:2d}'.format, row))
print()
for i in range(len(A)):
    if (i+1)%2==0:
        print('Наименьший элемент в', i, 'строке: ', min(A[i]))