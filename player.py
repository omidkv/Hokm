from suit import Suit
from card import Card

class Player:

    team = -1
    suit_options = {"heart": Suit.HEART,
               "spade": Suit.SPADE,
               "club": Suit.CLUB,
               "diamond": Suit.DIAMOND}


    player_number = 0

    def __init__(self,team):
        self.team = team
        # self.hand = list()
        self.hand = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }
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
        # self.hand.extend(cards)

        for card in cards:
            self.hand[card.suit].append(card.value)
        for key, items in self.hand.items():
            items.sort()

    def select_hokm(self):

        print(self.hand)
        hokm = input("What is hokm?").lower().strip()
        print(hokm)
        return self.suit_options[hokm]
    # select card is called by play card this is where the program takes input from user.

    def select_card(self):
        print(str(self.hand).replace('11','J').replace('12','Q').replace('13','K').replace('14','A'))
        card_string = input("Select Card to Play?").strip()
        split_set = card_string.split()
        if (self.card_value(split_set[1])) in self.hand[self.suit_options[split_set[0].lower()]]:
            self.hand[self.suit_options[split_set[0].lower()]].remove(self.card_value(split_set[1]))
            return Card(self.suit_options[split_set[0].lower()], self.card_value(split_set[1]))
        else:
            return self.select_card()


    #     check suit checks to make sure that the user doesn't have the init suit in their hand.

    # def check_suit(self,suit):
    #     for card in self.hand:
    #         if card.suit == suit:
    #             return True
    #     return False

    # play card is what is called from the game. This is where game passes information to the player and receives their
    # card back.
    # This also uses check suit to validate the correct selection of a card.

    def play_card(self,inital_suit,cards_on_table,winning_position):
        print('\nCard of my teammate {0[1]}\nCards of my opponent {0[2]}, {0[3]}\n\n'.format(cards_on_table))
        # (self.hand.sort())
        if inital_suit == Suit.NONE:
            card = self.select_card()
            print('Played ', card)
            return card

        else:
            print('The initial suit for this round is ', inital_suit)
            card = self.select_card()
            if card.suit == inital_suit or self.hand[inital_suit]is None:
                print('Played ', card)
                return card
            else:
                print('Cannot play this card')
                return self.play_card(inital_suit,cards_on_table,winning_position)
