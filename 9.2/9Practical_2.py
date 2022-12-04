#Вариант 13. Найти наибольший и наименьший элементы прямоугольной матрицы
# и поменять их местами.
import numpy as np 
if __name__ == "__main__":
    a=[]
    with open('vvod.txt', 'r', encoding='utf-8-sig') as vvod:
        for lines in vvod.readlines():
            a.append(list (map(int, lines.split())))

    a=np.array(a)
    print(a)
    print(a.min(),a.max())
    max_a, min_a = a.max(), a.min()
    for lines in range(len(a)):
        for row in range(len(a[lines])):
            if a[lines][row]==max_a:
                a[lines][row]=min_a
            elif a[lines][row]==min_a:
                a[lines][row]=max_a    
    print(a)

    with open('vivod.txt', 'w', encoding='utf-8-sig') as vivod:
        for line in a:
            vivod.write(' '.join(map(str, line))+'\n')

