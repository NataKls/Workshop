#Вариант 13. Натуральное число, в записи которого n цифр, называется 
# числом Армстронга, если сумма его цифр, возведенная в степень n, 
# равна самому числу. Найти все числа Армстронга от 1 до к.
def arm(n):
    num=n
    a=[]
    while n>0:
        a.append(n%10)
        n=n//10
    l=len(a)
    sm=sum(map(lambda x: x**l,a))
    return num==sm
    
for i in range(1,int(input())):
    if arm(i):
         print(i)