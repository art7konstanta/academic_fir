class Orange:                               # создаем класс
    def __init__(self, w, c):               # добавляем методы например вес и цвет
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created!')
    def rot(self, days, temp):
        self.mold = days * temp
orange = Orange(6, 'Апельсин')
print(orange.rot(10, 33))
print(orange.mold)
# Метод rot принимает два параметра число дней после срыва и среднюю температуру
