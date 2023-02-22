# create the Hand with an initial set of cards

import unittest
import hw5_cards as hw_cards


class Hand:
    ''' a hand for playing card
        Class Attributes:
            None
        Instance Attributes :
            init_card: list (a list of card)

    '''

    def __init__(self, init_cards):
        self.init_cards = hw_cards.Card()
        print(self.init_cards)

    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass

    def draw(self, deck):
        pass


if __name__ == "__main__":
    unittest.main()
