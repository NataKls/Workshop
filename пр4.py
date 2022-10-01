'''a=3
b=10
while a<=b:
    print(a)
    a+=1'''

'''a=15
b=10
if a < b:
    for i in range(a, b):
        print(i)
else: 
    for i in range(a, b, -1):
        print(i)'''


'''a=20
b=15
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i)'''

#Сумма введенных чисел
num = input()
num = num.split()
print(num)
for i in range(len(num)):
    num[i] = (int(num[i]))

print(sum(num))

#Либо так
'''sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)'''

#Лесенка
'''u = int(input())
a = ''
for i in range(1,u+1):
    a += str(i)
    u-=1
    print((u)*' '+a+a[::-1][1:])'''

