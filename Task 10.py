print ('Задание 1 и 2')
# добавьте переменную square list в класс square так, что бы когда создаем объект он добавлялся в список
# Измените класс Square так, что бы выводилось сколько на сколько квадрат
print("=" * 40)
class Square:
    square_list = []
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.square_list.append((self.w, self.l))
    def perimeter(self):
        return 2 * self.l + self.w
    def print_size(self):
        print('''{} на {} на {} на {}'''.format(self.l, self.w, self.l, self.w))
sq1 = Square(4, 3)
sq2 = Square(5, 4)
sq3 = Square(6, 5)
print(Square.square_list)
print(sq2.print_size())
print("=" * 40)
print ('Задание 1 и 2 выполнены')

print ('Задание 3')
print("=" * 40)
class Fuzzy:
    def __init__(self):
        self.cat = 'Моня'

mone = Fuzzy()
pest_mone = mone
print (mone is pest_mone)

ne_mone = Fuzzy()
print (mone is ne_mone)
print("=" * 40)
print ('Задание 3 выполнено')
