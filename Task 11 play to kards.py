class Card:
    # список мастей
    suits = ["пикей","червей", "бубей", "треф"]
    # список старшинства карт
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    # создание карты
    def __init__(self, v, s):
        """suit и value целые числа"""
        self.value = v
        self.suit = s
   # определение какая карта больше
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else: return False
        return False
    # или меньше
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    # создание конкретной карты
    def __repr__(self):
        v = self.values[self.value] + ' of ' \
        + self.suits[self.suit]
        return v
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1<card2)
print(card1>card2)
card = Card(3, 2)
print(card)
# создание колоды карт
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range (2, 15):
            for j in range (4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
deck = Deck()
for card in deck.cards:
    print(card)

# создание игроков
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
# класс представляющий игру

class Game:
    def __init__(self):
        name1 = input('Name player 1: ')
        name2 = input('Name player 2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = '{} he takes the cards'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} puts {}, a {} puts {}'
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Forward!')
        while len(cards) >= 2:
            m = 'Press X to exit. Press any other key to start the game.'
            response = input(m)
            if response.upper() == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1c, p2c, p1n, p2n)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print('Game over! {} wins!'.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'Draw!'
game = Game()
game.play_game()