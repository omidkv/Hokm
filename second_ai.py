from suit import Suit
from card import Card


# second_AI is the second iteration of my game AI.


class second_AI:
    team = -1
    player_number = -1

    def __init__(self, team, number, teammate):
        self.team = team
        self.teammate_index = teammate
        self.player_number = number
        self.hand = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }
        self.hokm = Suit.NONE
        self.cards_played = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }
        self.suit_partner_doesnt_have = list()

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
        self.cards_played = {
            Suit.HEART: list(),
            Suit.DIAMOND: list(),
            Suit.SPADE: list(),
            Suit.CLUB: list()
        }
        self.suit_partner_doesnt_have = list()

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
            return self.first_to_play()
        # elif self.my_team_winning(winning_position):
        #     # play a trash card your team is winning
        #     return self.find_low_card(init_suit)
        else:
            card = self.not_first(init_suit, cards_on_table, winning_position)
            if(card is None):
                raise Exception("Failed")
            return card

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

        self.check_for_sure_win(suit, highest_value)
        return Card(suit, self.hand[suit][-1])

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

    def update_cards_played(self, cards, init_suit):

        # Need to check the out of cards later
        for key, card in cards.items():
            self.cards_played[card.suit].append(card.value)
            if key == self.teammate_index:
                if card.suit != init_suit:
                    # print('Marker')
                    # print(card.suit)
                    # print('init suit', init_suit)
                    self.suit_partner_doesnt_have.append(init_suit)

        # print('Cards ', self.cards_played)

    def check_for_sure_win(self, suit, value):
        cards_played = self.cards_played[suit]
        cards_larger = 14 - value

        new_list = [i for i in cards_played if i > value]
        # print("Marker")
        # print(value)
        # print(new_list)
        # print(len(new_list) == cards_larger)
        return len(new_list) == cards_larger

    # def play_card(self, init_suit, cards_on_table, winning_position):
    #     # This is when you are the first to play
    #     if init_suit == Suit.NONE:


    def first_to_play(self):
        # card that will definitely win
        for suit, values in self.hand.items():
            if len(values) >= 1:
                if self.check_for_sure_win(suit, values[-1]):
                    return Card(suit, self.hand[suit].pop())

        # pass to partner if out of a suit

        for suit in self.suit_partner_doesnt_have:
            if len(self.hand[suit]) > 0:
                return Card(suit, self.hand[suit].pop(0))

        highest_card = self.highest_card()
        # print('Marker')
        # print(highest_card)
        return Card(highest_card.suit, self.hand[highest_card.suit].pop(0))

    def not_first(self, init_suit, cards_on_table, winning_position):

        if len(self.hand[init_suit]) > 0:
            return self.play_from_init_suit(init_suit, cards_on_table, winning_position)
        return self.play_another_suit(init_suit,cards_on_table,winning_position)

    def teammate_guarenteed_win(self, cards_on_table, winning_position):
        if winning_position != self.teammate_index:
            return False
        else:
            card = cards_on_table[winning_position]
            return self.check_for_sure_win(card.suit, card.value)

    def check_if_can_take_lead(self, init_suit, cards_on_table, winning_position):
        winning_card = cards_on_table[winning_position]
        if winning_card.suit != init_suit:
            return False
        else:
            cards_ahead = [i for i in self.hand[init_suit] if i > winning_card.value]
            if len(cards_ahead) == 0:
                return False
            else:
                return True

    def play_guarenteed_win_or_just_ahead(self, init_suit, cards_on_table, winning_position):
        winning_card = cards_on_table[winning_position]
        cards_ahead = [i for i in self.hand[init_suit] if i > winning_card.value]
        if self.check_for_sure_win(init_suit, cards_ahead[-1]):
            return Card(init_suit, self.hand[init_suit].pop())
        else:
            value = cards_ahead[0]
            self.hand[init_suit].remove(value)
            return Card(init_suit, value)

    def play_from_init_suit(self, init_suit, cards_on_table, winning_position):
        if self.teammate_guarenteed_win(cards_on_table, winning_position) or not self.check_if_can_take_lead(init_suit,
                                                                                                             cards_on_table,
                                                                                                             winning_position):
            return self.find_low_card(init_suit)
        else:
            return self.play_guarenteed_win_or_just_ahead(init_suit, cards_on_table, winning_position)

    def play_lowest_hokm_or_pass(self, init_suit, cards_on_table, winning_position):
        winning_card = cards_on_table[winning_position]
        if winning_card.suit == self.hokm:
            cards_ahead = [i for i in self.hand[self.hokm] if i > winning_card.value]
            if len(cards_ahead) > 0:
                self.hand[self.hokm].remove(cards_ahead[0])
                return Card(self.hokm, cards_ahead[0])
            else:
                return self.find_low_card(init_suit)
        else:
            return Card(self.hokm, self.hand[self.hokm].pop(0))

    def play_another_suit(self, init_suit, cards_on_table, winning_position):
        if self.teammate_index == winning_position:
            teammate_card = cards_on_table[winning_position]
            if self.check_for_sure_win(teammate_card.suit, teammate_card.value):
                # print("1")

                return self.find_low_card(init_suit)

        if len(self.hand[self.hokm]) == 0:
            # print("2")
            return self.find_low_card(init_suit)


        else:
            # print("3")
            return self.play_lowest_hokm_or_pass(init_suit, cards_on_table, winning_position)
