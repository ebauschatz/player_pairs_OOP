import random
from data_models.card import Card

class Deck:
    def __init__(self, card_types, type_repetitions):
        self.cards = self.__generate_deck(card_types, type_repetitions)

    def __generate_deck(self, card_types, type_repetitions):
        new_deck = []
        for card_type in card_types:
            for _ in range(type_repetitions):
                new_deck.append(Card(card_type))
        return new_deck

    def shuffle_deck(self):
        random.shuffle(self.cards)