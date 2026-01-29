'''В этом примере объекты Rectangle имеют
две переменные экземпляра: long и width.
Метод аrеа возвращает площадь объекта Rectangle,
перемножая между собой переменные экземпляра,
а метод change_size изменяет переменные,
присваивая им числа, которые передаются в качестве параметров.'''
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.long = l
    def area(self):
        return self.width * self.long
    def change_size(self, w, l):
        self.width = w
        self.long = l
rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
