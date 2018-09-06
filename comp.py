from card import Card
from suit import Suit


# Comp is a class that is used by the game logic to see the current winner of the hand is.
# Comp also stores the cards that are on the table.
#
#
class Comp:
    def __init__(self):
        self.player_card = Card(Suit.NONE, -1)
        self.teammate_ai = Card(Suit.NONE, -1)
        self.opponent_1 = Card(Suit.NONE, -1)
        self.opponent_2 = Card(Suit.NONE, -1)
        self.hokm = Suit.NONE
        self.initial_suit = Suit.NONE
        self.high_card = Card(Suit.NONE, -1)
        self.high_card_index = -1

        self.switcher_2 = {

            0: self.player_card,
            1: self.teammate_ai,
            2: self.opponent_1,
            3: self.opponent_2
        }

    def set_player_card(self, card):
        self.player_card = card
        self.switcher_2[0] = card

    def set_teammate_ai(self, card):
        self.teammate_ai = card
        self.switcher_2[1] = card

    def set_opponent_1(self, card):
        self.opponent_1 = card
        self.switcher_2[2] = card

    def set_opponent_2(self, card):
        self.opponent_1 = card
        self.switcher_2[3] = card

    switcher = {
        0: set_player_card,
        1: set_teammate_ai,
        2: set_opponent_1,
        3: set_opponent_2
    }

    def set_card(self, index, card):
        self.switcher[index](self, card)

    def after_hand_reset(self):
        hokm = self.hokm
        self.__init__()
        self.hokm = hokm

    def new_game_reset(self):
        self.__init__()

    def set_hokm(self, suit):
        self.hokm = suit

    def set_initial_suit(self, suit):
        self.initial_suit = suit

    #   compare will see if the last card played is the winning card currently
    #    rules for winning either the same suit as the initial card and higher or
    #     hokm and the highest value.
    #
    #     if high card is none than other card is the high card
    #     if high card suit is hokm and the other cards suit isn't high card stays the same
    #     if high card suit is hokm and the other cards suit is high card is the higher of the values
    #     if high card suit isn't hokm and the other cards suit is the other card is now the high card
    #     if high card suit isn't hokm and the other card is the same as the init suit higher value wins
    #     if other card is any suit other than hokm or init it is a trash card and high card stays the same
    def compare(self, index):
        if self.high_card_index == -1:
            self.high_card = self.switcher_2[index]
            self.high_card_index = index
            self.initial_suit = self.switcher_2[index].suit
            # print('here 0')
        else:
            high_card_suit = self.high_card.suit
            other_card = self.switcher_2[index]
            if high_card_suit == self.hokm:
                if other_card.suit == self.hokm and other_card.value > self.high_card.value:
                    self.high_card = other_card
                    self.high_card_index = index
                    # print('here 1')

            else:
                if other_card.suit == self.hokm:
                    self.high_card = other_card
                    self.high_card_index = index
                    # print('here 2')
                elif other_card.suit == self.initial_suit and other_card.value > self.high_card.value:
                    self.high_card = other_card
                    self.high_card_index = index
                    # print('here 3')

        return self.high_card_index

    # set_and_comp is the function called by the game logic to set a card and run a compare after that moment.
    def set_and_comp(self, index, card):
        self.set_card(index, card)
        # print(card)
        return self.compare(index)

    # print_cards is used to print the cards that are on the table after all of the cards are played.
    # User needs to see the cards that have been played in order to make a good decision.
    def print_cards(self):
        print('\nMy card is {0[0]}, Card of my teammate {0[1]}\n Cards of my opponent {0[2]}, {0[3]}'.format(
            self.switcher_2))
