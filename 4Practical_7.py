# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать
# только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено
u = int(input())
fak = [1,0]
for i in range(0,u):
    fak[0] += fak[0] * i
    fak[1] += fak[0]
print(fak[1])