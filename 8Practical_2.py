#Вариант 13. Найти наибольший и наименьший элементы прямоугольной матрицы
# и поменять их местами.
 
import random
n=int(input('Указать кол-во строк и столбцов: '))

a=[[random.randrange(10) for i in range(n)] for j in range(n)]
for row in a:
    print(*map('{:2d}'.format, row))


maximum = max(map(max, a))
i_maximim1 = a.index(max(a))
i_maximim2 = a[i_maximim1].index(maximum)
 
minimum = min(min(a))
i_minimum1 = a.index(min(a))
i_minimum2 = a[i_minimum1].index(minimum)
 
a[i_minimum1][i_minimum2], a[i_maximim1][i_maximim2] = maximum, minimum
print()
for row in a:
    print(*map('{:2d}'.format, row))