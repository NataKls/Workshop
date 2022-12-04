#Вариант 13. Определить наименьший элемент каждой четной строки 
#матрицы А[М, N].

if __name__ == "__main__":
    a=''
    with open('vvod.txt', 'r', encoding='utf-8-sig') as vvod:
        k=1
        for lines in vvod.readlines():
            if k%2==0:
                p = f'Наименьший элемент в строке {k}: {min(lines.split())} \n'
                a=a+p
            k+=1
    print(a)

    with open('vivod.txt', 'w', encoding='utf-8-sig') as vivod:
        vivod.write(a)

