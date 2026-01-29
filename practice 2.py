print ('Задание 1') # Программа, которая записывает информацию в списки в зависимости от ввода
print ('')
rock = []
country = []
def collect_songs():
    print("=== ПРОГРАММА ЗАПУЩЕНА ===")
    song = 'Укажите песню: '
    ask = 'Введите p (рок) или k (кантри). Введите X для выхода: >>>  '

    while True:
        genre = input(ask)
        if genre == 'X' or 'x':
            break
        if genre == 'p':
            rk = input(song)
            rock.append(rk)
        elif genre == 'k':
            cy = input(song)
            country.append(cy)
        else:
            print('НЕВЕРНО')
    print(rock)
    print(country)
collect_songs()
# Весь код является процедурным программированием (одно действие за другим (последовательно))
