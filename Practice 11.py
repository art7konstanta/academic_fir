text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
# нашел совпадение в тексте и вернул
# что бы не учитывать регистр - добавляем re.IGNORECASE
import re
matches = re.findall('beautiful', text, re.IGNORECASE)
print(matches)
# использовать re.MULTILINE что бы искать совпадения во всех строках многострочного экрана
m = re.findall('^If', text, re.MULTILINE)
print(m)
string = 'Два даа.'
# регулярное выражение сначала находит совпадение с "д" затем либо с "а" либо "в" потом с "а"
o = re.findall('д[ав]а', string, re.IGNORECASE)
print(o)
# Вывод только цифр из текста
line = '123?34 привет?'
l = re.findall('\\d', line, re.IGNORECASE)
print(l)
# для того что бы использовать не "Жадный" поиск в python необходимо добавить знак "?"
t = '__one__ __two__ __three__'
found = re.findall('__.*?__', t, re.IGNORECASE)
for match in found:
    print(match)
# с помощью нежадного поиска можно создать игру чепуха (practice 12)
# в регулярных выражениях можно экранировать символы например:
line1 = 'Я люблю $'
m1 = re.findall('\\$', line1, re.IGNORECASE)
print(m1)
print ('Задание 1')
# найдите любое слова в мудрости Пайтона используя регулярное выражение
print('=' * 40)
m2 = re.findall('ambiguity', text, re.IGNORECASE)
print(m2)
print('=' * 40)
print ('Задание 1 выполнено')
print ('Задание 2')
# создайте регулярное выражение которое находит все цифры в заданном выражении и отсортируйте это значение
print('=' * 40)
line3 = 'Москва: 777, 999, 797. Тула: 071, 950, 112.'
m3 = re.findall('\\d', line3, re.IGNORECASE)
import math
print(sorted(m3))
print('=' * 40)
print ('Задание 2 выполнено')

print('Задание 3')
# создайте регулярное выражение для поиска любого слова с произвольного символа, предшествующего буквам ло.
# затем используйте модуль re, что бы найти сочетание ало и зло в предложении
print('=' * 40)
offer = ('Приведение прошуршало и исчезло в углу.')
m4 = re.findall('.ло', offer, re.IGNORECASE)
print(m4)
m5 = re.findall('зло|ало', offer, re.IGNORECASE)
print(m5)