#13 вариант.Дан одномерный массив целых чисел. 
# Проверить, есть ли в нем одинаковые 
# элементы. Вывести эти элементы и их индексы.

a=[1,2,3,2,4,2,5,4,15,16,15]
b = {}
for i in range(len(a)):
    if a.count(a[i]) > 1:
        if (a[i] not in b):
            b[a[i]] = [i]
        else:
            b[a[i]].append(i)
print(b)