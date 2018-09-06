from suit import Suit
from card import Card


# init_AI is the first iteration of my game AI.


class init_AI:
    team = -1
    player_number = -1

    def __init__(self, team, number):
        self.team = team
        self.player_number = number
        self.hand = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
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

    # Resets the hand at the end of a game.
    def reset_hand(self):
        self.hand = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }

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
            # print(self.hand)

    # selects hokm based on which suit has the most cards. Or which has the highest total value if there is a tie
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
        return hokm

    # play_card requires the A_I to look at cards on table and play, if first card they should pick their highest card.
    def play_card(self, init_suit, cards_on_table, winning_position):
        # A_I makes the first move
        if init_suit == Suit.NONE:
            return self.highest_card()
        elif self.my_team_winning(winning_position):
            # play a trash card your team is winning
            return self.find_low_card(init_suit)
        else:
            return self.find_high_card_or_pass(init_suit)

    # find value is used when selecting the hokm
    def find_value(self, lists):
        total = 0
        for card_value in lists:
            total = total + card_value
        return total

    # highest card is used to select the highest card that they can play
    def highest_card(self):
        highest_value = -1
        suit = Suit.NONE
        for key, card_value in self.hand.items():
            if card_value:

                high_in_suit = card_value[-1]
                if high_in_suit > highest_value:
                    suit = key
                    highest_value = high_in_suit

        return Card(suit, self.hand[suit].pop())

    # determine if their team is winning
    def my_team_winning(self, winning_position):
        if self.team == 1:
            return -1 < winning_position < 2
        else:
            return winning_position > 1

    # find the lowest card that they can play
    def find_low_card(self, init_suit):
        if not self.hand[init_suit]:
            for key, cards in self.hand.items():
                if key != self.hokm and key != init_suit:
                    try:
                        return Card(key, self.hand[key].pop(0))
                    except IndexError:
                        return self.find_high_card_or_pass(init_suit)

        else:
            return Card(init_suit, self.hand[init_suit].pop(0))

    # finds a high card or passes if they don't have a card that can win.
    def find_high_card_or_pass(self, init_suit):
        # print(init_suit)
        if self.hand[init_suit] is None or not self.hand[init_suit]:
            # print(self.hokm)
            if not self.hand[self.hokm]:
                # Cannot win hand have to throw a trash card.
                for key, cards in self.hand.items():
                    if key != self.hokm and key != init_suit and cards:
                        return Card(key, self.hand[key].pop(0))
            # Else needs to be changed currently just playing highest hokm or highest init more needs to go into this
            # later.
            else:
                return Card(self.hokm, self.hand[self.hokm].pop())
        else:
            return Card(init_suit, self.hand[init_suit].pop())
