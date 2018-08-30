from card import Card
from suit import Suit

# This
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
        # player_card index = 0
        # teammate_ai index = 1
        # opponent_1 index = 2
        # opponent_2 index = 3


        self.switcher_2 = {

            0: self.player_card,
            1: self.teammate_ai,
            2: self.opponent_1,
            3: self.opponent_2
        }

    def set_player_card(self,card):
        self.player_card = card
        self.switcher_2[0] = card

    def set_teammate_ai(self,card):
        self.teammate_ai = card
        self.switcher_2[1] = card

    def set_opponent_1(self,card):
        self.opponent_1 = card
        self.switcher_2[2] = card

    def set_opponent_2(self,card):
        self.opponent_1 = card
        self.switcher_2[3] = card


    switcher = {
        0: set_player_card,
        1: set_teammate_ai,
        2: set_opponent_1,
        3: set_opponent_2
    }

    def set_card(self,index,card):
        self.switcher[index](self,card)


    def after_hand_reset(self):
        hokm = self.hokm
        self.__init__()
        self.hokm = hokm

    def new_game_reset(self):
        self.__init__()

    def set_hokm(self,suit):
        self.hokm = suit

    def set_initial_suit(self,suit):
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
    def compare(self,index):
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

    def set_and_comp(self,index,card):
        self.set_card(index,card)
        print(card)
        return self.compare(index)

    def print_cards(self):
        print('My card is {0[0]}, Card of my teammate {0[1]}\n Cards of my opponent {0[2]}, {0[3]}'.format(self.switcher_2))

# test = Comp()
# test.set_hokm(Suit.DIAMOND)
# test.set_card(1, Card(Suit.HEART, 10))
# print(test.teammate_ai)
# test.compare(1)
# test.set_card(2, Card(Suit.DIAMOND, 2))
# print(test.compare(2))
# test.set_card(3, Card(Suit.HEART, 11))
# print(test.compare(3))
#
# test.set_card(0, Card(Suit.SPADE, 14))
# print(test.compare(0))

# print(test.teammate_ai)





# OLD method from game_logic

# def high_card(inital_suit, cards_on_table, hokm):
#     high_value = -1
#     hokm_played = False
#     winning_position = -1
#     position = 0
#     for tuple in cards_on_table:
#         card = tuple[0]
#         if card.suit == inital_suit and card.value > high_value and hokm_played is False:
#            high_value = card.value
#            winning_position = position
#            position = position + 1
#
#         elif hokm_played is False and card.suit == hokm:
#             hokm_played = True
#             high_value = card.value
#             winning_position = position
#             position = position + 1
#
#         elif card.suit == hokm and card.value > high_value and hokm_played is True:
#            high_value = card.value
#            winning_position = position
#            position = position + 1
#         else:
#             position = position + 1
#
#     return winning_position