print ('Задание 1')  # Определите класс яблоко и добавьте к нему 4 переменных представляющих 4 свойства
class Apple:
    def __init__(self, c, w, s, v):
        self.color = c
        self.weight = w
        self.size = s
        self.variety = v
apple = Apple('Красное', '300 грамм', 'среднее', 'сезонное')
print(apple.color, apple.weight, apple.size, apple.variety)
print('Задание 1 выполнено')
print ('=' * 40)

print ('Задание 2') # создайте круг, найдите площадь, выведите результат и все это через модуль pi в math.
import math
class Circle:
    def __init__(self, r, l):
        self.radius = r
        self.long = l
    def area(self):
        return math.pi * self.radius ** 2
circle = Circle(10, 30)
print(circle.area())
print('Задание 2 выполнено')
print('=' * 40)

print ('Задание 3')
class Triangle:
    def __init__(self, a, h):
        self.long1 = a
        self.height = h
    def area(self):
        return (self.long1 * self.height) / 2
triangle = Triangle(10, 30)
print(triangle.area())
print('Задание 3 выполнено')
print('=' * 40)

print ('Задание 4')
class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6
hexagon = Hexagon(10, 20, 30, 40, 50, 60)
print(hexagon.calculate_perimeter())
print('Задание 4 выполнено')
print('=' * 40)