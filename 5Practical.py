'''Вариант 13.
Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. 
Вывести на экран все символы, расположенные внутри этих скобок'''

str = "Скоро (а время всё мчится быстрее) Стают снега"
print(str[str.find('(')+1: str.find(')')])