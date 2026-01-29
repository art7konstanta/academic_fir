class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Дилберт")
print(lion)
# когда вы выводите объект Lion Python вызывает в нем магический метод __repr__, унаследованный
# этим объектом от Object, и выводит то, что возвращает __repr__. Можно переопределить унаследованный метод,
# __repr__ что бы изменить его вывод
class Lion:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion("Дилберт")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs (self.n + other.n)
x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x + y)


# Ключевое слово is возвращает значение True если два объекта являются одним и тем же объектом и False -#
#- в противном случае
class Person:
    def __init__(self):
        self.name = 'Боб'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

x = 10
if x is None:
    print ('x равно None :(')
else:
    print('x не равно None')
x = None
if x is None:
    print('x равно None :(')
else:
    print('x не равно None')