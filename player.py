from suit import Suit
from card import Card
from termcolor import colored


# Player is the class that controls user input from the terminal
class Player:
    team = -1
    suit_options = {"heart": Suit.HEART,
                    "spade": Suit.SPADE,
                    "club": Suit.CLUB,
                    "diamond": Suit.DIAMOND}

    player_number = 0

    def __init__(self, team):
        self.team = team
        self.hand = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }
        self.hokm = Suit.NONE

    def __repr__(self):
        return "Human"

    # resets the players hand after the game
    def reset_hand(self):
        self.hand = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }

    # prints the player hand nicely
    def print_hand(self):
        hearts = str(self.hand[Suit.HEART]).replace('11', 'J').replace('12', 'Q').replace('13', 'K').replace('14', 'A')
        diamonds = str(self.hand[Suit.DIAMOND]).replace('11', 'J').replace('12', 'Q').replace('13', 'K').replace('14',
                                                                                                                 'A')
        clubs = str(self.hand[Suit.CLUB]).replace('11', 'J').replace('12', 'Q').replace('13', 'K').replace('14', 'A')
        spades = str(self.hand[Suit.SPADE]).replace('11', 'J').replace('12', 'Q').replace('13', 'K').replace('14', 'A')

        print(colored(str(Suit.HEART) + hearts + ' ' + str(Suit.DIAMOND) + diamonds, 'red', 'on_grey', attrs=['bold']))
        print(colored(str(Suit.CLUB) + clubs + ' ' + str(Suit.SPADE) + spades, 'white', 'on_grey', attrs=['bold']))

    # translates a letter into the value of the card
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

    def select_hokm(self):

        print(self.hand)
        hokm = input("What is hokm?").lower().strip()
        print(hokm)
        return self.suit_options[hokm]

    # select card is called by play card this is where the program takes input from user.

    def select_card(self):
        self.print_hand()
        card_string = input("\nSelect Card to Play?").strip()
        split_set = card_string.split()
        card_val = self.card_value(split_set[1])

        if split_set[0].lower() in self.suit_options:
            suit = self.suit_options[split_set[0].lower()]
            if card_val in self.hand[suit]:
                return Card(suit, card_val)
            else:
                return self.select_card()
        else:
            return self.select_card()

    # play card is what is called from the game. This is where game passes information to the player and receives their
    # card back.
    # This also uses check suit to validate the correct selection of a card.

    def play_card(self, inital_suit, cards_on_table, winning_position):
        if inital_suit == Suit.NONE:
            stringer = '\n No Cards have been played \nHokm is {0}\n'.format(self.hokm)
            print(colored(stringer, 'green'))
            card = self.select_card()
            print('Played ', card)
            self.hand[card.suit].remove(card.value)
            return card

        else:
            string1 = 'The initial suit for this round is {0}\nThe hokm is {1}\n'.format(inital_suit, self.hokm)
            print(colored(string1, 'blue'))
            string2 = '\nCard of my teammate {0[1]}\nCards of my opponent {0[2]}, {0[3]}\n\n'.format(cards_on_table)
            print(colored(string2, 'cyan'))
            card = self.select_card()
            if card.suit == inital_suit or not self.hand[inital_suit]:
                print('Played ', card)
                self.hand[card.suit].remove(card.value)
                return card
            else:
                print('Cannot play this card')
                return self.play_card(inital_suit, cards_on_table, winning_position)

    def update_cards_played(self,cards, _):

        None