
from suit import Suit
from card import Card

class inital_AI:


    team = -1
    player_number = -1

    def __init__(self,team,number):
        self.team = team
        self.player_number = number
        self.hand = {
            Suit.HEART:list(),
            Suit.DIAMOND:list(),
            Suit.SPADE:list(),
            Suit.CLUB:list()
        }
        self.hokm = Suit.NONE

    def __repr__(self):
        return "AI " + str(self.player_number)

    suit_options = {"heart": Suit.HEART,
                   "spade": Suit.SPADE,
                   "club": Suit.CLUB,
                   "diamond": Suit.DIAMOND}

    # This method is used by the game to give the ai information about the hokm.
    def set_hokm(self, hokm):

        self.hokm = hokm

    def card_value(self, str):
        if str.isdigit():
            return int(str)
        elif str == "A":
            return 14
        elif str == "J":
            return 11
        elif str == "Q":
            return 12
        elif str == "K":
            return 13

    def add_cards(self, cards):
        for card in cards:
            self.hand[card.suit].append(card.value)
        for key, items in self.hand.items():
            items.sort()
        print(self.hand)

    def select_hokm(self):
        hokm = Suit.NONE
        max_length = 0
        max_value = 0
        for key, lists in self.hand.items():
            new_length = len(lists)
            if new_length >= max_length:
                new_value = self.find_value(lists)
                if new_length > max_length or new_value > max_value:
                    hokm = key
                    max_length = new_length
                    max_value = new_value
        print(hokm)
        return hokm


    def select_card(self,inital_suit,cards_on_table):
        print(self.hand)
        if inital_suit is None:
            return self.hand[0]
        else:
            print(Card(split_set[0].lower(), self.card_value(split_set[1])))
            return self.select_card()

    def check_suit(self,suit):
        for card in self.hand:
            if card.suit == suit:
                return True
        return False
    # play_card requires the A_I to look at cards on table and play, if first card they should pick their highest card.
    # def play_card(self,inital_suit, cards_on_table):
    #     print(cards_on_table)
    #     (self.hand.sort())
    #     if inital_suit is None:
    #         card = self.select_card(inital_suit,cards_on_table)
    #         print('Played ', card)
    #         return card
    #
    #     else:
    #         card = self.select_card()
    #         if card.suit == inital_suit or not self.check_suit(inital_suit):
    #             print('Played ', card)
    #             return card
    #         else:
    #             print('Cannot play this card')
    #             return self.play_card(inital_suit,cards_on_table)

    def play_card(self, init_suit, cards_on_table, winning_position):
        print(cards_on_table)
        # A_I makes the first move
        if init_suit is None:
            return self.highest_card()
        elif winning_position > -1 and winning_position > 1:
            return self.hand[init_suit].pop(0)



    def find_value(self, lists):
        total = 0
        for card_value in lists:
            total = total + card_value
        return total

    def highest_card(self):
        highest_value = -1
        suit = Suit.NONE
        for key, card_value in self.hand.items():

            high_in_suit = card_value[-1]
            if high_in_suit > highest_value:
                suit = key
                highest_value = high_in_suit

        return Card(suit,self.hand[suit].pop())








