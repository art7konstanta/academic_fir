class Square:
    pass
print (Square)

# переменные экземпляра класса принадлежат объектам
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print (' {} на {} '.format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

class Rectangle1:
    recs = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print('''{}  на  {}'''.format(self.width, self.len))

r1 = Rectangle1(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)