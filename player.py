from suit import Suit
from card import Card

class Player:

    team = -1
    suit_options = {"heart": Suit.HEART,
               "spade": Suit.SPADE,
               "club": Suit.CLUB,
               "diamond": Suit.DIAMOND}

    def __init__(self,team):
        self.team = team
        self.hand = list()

    def __repr__(self):
        return "Human"

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
    def add_cards(self,cards):
        self.hand.extend(cards)


    def select_hokm(self):

        (self.hand.sort())
        print(self.hand)
        hokm = input("What is hokm?").lower().strip()
        print(hokm)
        return self.suit_options[hokm]
    # select card is called by play card this is where the program takes input from user.

    def select_card(self):
        print(self.hand)
        card_string = input("Select Card to Play?").strip()
        split_set = card_string.split()
        if Card(self.suit_options[split_set[0].lower()], self.card_value(split_set[1])) in self.hand:
            return Card(self.suit_options[split_set[0].lower()], self.card_value(split_set[1]))
        else:
            return self.select_card()

    #     check suit checks to make sure that the user doesn't have the init suit in their hand.

    def check_suit(self,suit):
        for card in self.hand:
            if card.suit == suit:
                return True
        return False

    # play card is what is called from the game. This is where game passes information to the player and receives their
    # card back.
    # This also uses check suit to validate the correct selection of a card.

    def play_card(self,inital_suit,cards_on_table,winning_position):
        print(cards_on_table)
        (self.hand.sort())
        if inital_suit is None:
            card = self.select_card()
            print('Played ', card)
            return card

        else:
            card = self.select_card()
            if card.suit == inital_suit or not self.check_suit(inital_suit):
                print('Played ', card)
                return card
            else:
                print('Cannot play this card')
                return self.play_card(inital_suit,cards_on_table)
