#Вариант 13. Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и
# Z(z1, z2). Найти и напечатать координаты точки, для которой угол между
#осью абсцисс и лучом, соединяющим начало координат с точкой,минимальный. 
#Вычисления оформить в виде процедуры.
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input('Введите x(x1,x2): ').split())
y1, y2 = map(float,input('Введите y(y1,y2): ').split())
z1, z2 = map(float,input('Введите z(z1,z2): ').split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print('\nКоординаты точки: ',*res)