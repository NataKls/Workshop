#По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов
u = int(input())
a = ''
for i in range(1,u+1):
    a += str(i)
    u-=1
    print((u)*' '+a+a[::-1][1:])