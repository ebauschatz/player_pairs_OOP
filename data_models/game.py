from data_models.deck import Deck
from data_models.helpers import Helpers

class Game:
    def __init__(self):
        self.card_types = ['ace', 'two', 'three']
        self.card_type_repetitions = 3
        self.cards_per_hand = 5
        self.deck = Deck(self.card_types, self.card_type_repetitions)
        self.number_of_players = self.__get_number_of_players()
        self.number_of_rounds = self.__get_number_of_rounds()

    def __get_number_of_players(self):
        return Helpers.get_valid_numeric_input('players')

    def __get_number_of_rounds(self):
        return Helpers.get_valid_numeric_input('rounds')
    
    def run_game(self):
        self.deck.shuffle_deck()
        print()