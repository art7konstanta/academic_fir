print ('Задание 1, 2, 3')
# Создайте классы треугольник и квадрат с методом вычисляющим их периметр
# Вызови эти методы - Задание 1
# В методе квадрат создай метод который уменьшает или увеличивает каждую сторону - Задание 2
class Shape:
    def __init__(self, what_am_i):
        self.what_am_i = what_am_i
        print('Я фигура.')
class Rectangle(Shape):
    def __init__(self, a, b, c, what_am_i='Треугольник'):
        super().__init__(what_am_i)
        self.side1 = a
        self.side2 = b
        self.side3 = c
    def calculate_perimetr(self):
        return self.side1 + self.side2 + self.side2 + self.side3
class Square(Shape):
    def __init__(self, a1, b2, c3, d4, what_am_i='Квадрат'):
        super().__init__(what_am_i)
        self.side1 = a1
        self.side2 = b2
        self.side3 = c3
        self.side4 = d4
    def calculate_perimetr(self):
        return self.side1 + self.side2 + self.side3 + self.side4
    def change_size(self, n):
        self.side1 += n
        self.side2 += n
        self.side3 += n
        self.side4 += n
        return self.side1, self.side2, self.side3, self.side4
rectangle = Rectangle(10, 12, 15)
print(rectangle.calculate_perimetr())
square = Square(10, 10, 10, 10)
print(square.calculate_perimetr())
print(square.change_size(5))
print ('Задание 1, 2, 3 выполнены')
print ('=' * 40)

print ('Задание 4')
print ('=' * 40)
# Создайте классы наездник и лошадь. Используйте композицию, что бы смоделировать лошадь с всадником на ней.
class Horse:
    def __init__(self, b, ms, c):
        self.breed = b
        self.max_speed = ms
        self.color = c

class Rider:
    def __init__(self, n):
        self.name = n
        self.horse = None

John = Rider('Джон скоростной')
Lara = Rider('Лара ветер')

horse1 = Horse('Австрийская', 40, 'Белая')
horse2 = Horse('Английская', 50, 'Черная')

storm = horse1
thunderbolt = horse2

John.horse = horse1
Lara.horse = horse2

print(f"{storm.breed}, макс. скорость: {storm.max_speed}, цвет: {storm.color}")
print(f"{thunderbolt.breed}, макс. скорость: {thunderbolt.max_speed}, цвет: {thunderbolt.color}")
print(f"{John.name} ездит на {John.horse.breed}")
print(f"{Lara.name} ездит на {Lara.horse.breed}")
print ('=' * 40)
print ('Задание 4 выполнено')
