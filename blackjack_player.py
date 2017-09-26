import random
from functools import reduce
from blackjack_deck import Card

class Player(object):
    # value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    #               '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
    #               'K': 10, 'A': 11}

    def __init__(self,starting_cash=10000):
        self.hand = []
        self.money = starting_cash
        self.hand_total = 0

    def receive_card(self, card):
        self.hand.append(card)
        tot = 0
        a_count = 0
        for c in self.hand:
            if c.number == 'A':
                a_count += 1
            tot += c.value_dict[c.number]

        while tot > 21 and a_count > 0:
            tot -= 10
            a_count -= 1
        self.hand_total = tot

    def hand_text(self):
        return "Player: " + " ".join(str(card) for card in self.hand)

    def clear (self):
        self.hand = []
        self.hand_total = 0

class Dealer(object):
    def __init__(self):
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)
        tot = 0
        a_count = 0
        for c in self.hand:
            if c.number == 'A':
                a_count += 1
            tot += c.value_dict[c.number]

        while tot > 21 and a_count > 0:
            tot -= 10
            a_count -= 1
        self.hand_total = tot

    def hand_text(self):
        return "Dealer: " + " ".join(str(card) for card in self.hand)

    def clear (self):
        self.hand = []
        self.hand_total = 0
