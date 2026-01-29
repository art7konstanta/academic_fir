class Orange:                               # создаем класс
    def __init__(self, w, c):               # добавляем методы например вес и цвет
        self.weight = w
        self.color = c
        print('Created!')                   # создано
or1 = Orange(10, 'Темный апельсин')   # создаем объект и присваиваем ему параметры
print(or1.weight)                           # выводим все это дело на экран
print(or1.color)                            # для того что бы изменить значение переменной смотри код ниже
or1.weight = 100
or1.color = 'Светлый апельсин'
print(or1.weight, or1.color)                # используя класс апельсинов их можно создать целое множество
or2 = Orange(50, 'Светло-оранжевый')
or3 = Orange(60, 'Темно-оранжевый')
print(or2.weight, or2.color)
print(or3.weight, or3.color)

