from card import Card
from suit import Suit
from random import shuffle
from player import Player
from init_ai import init_AI
from second_ai import second_AI
from team import Team
from comp import Comp
from termcolor import colored

import random

game_run = True
match_run = True
human = Player(1)
# human = second_AI(1,0, 1)
teammate = second_AI(1, 1, 0)
opponent_1 = second_AI(2, 2, 3)
opponent_2 = second_AI(2, 3, 2)
team1 = Team(human, teammate)
team2 = Team(opponent_1, opponent_2)

list_of_players_1 = [human, opponent_1, teammate, opponent_2]
list_of_players_2 = [opponent_1, teammate, opponent_2, human]
list_of_players_3 = [teammate, opponent_2, human, opponent_1]
list_of_players_4 = [opponent_2, human, opponent_1, teammate, ]
# the order if the player at each position wins, this is with the player and teammate being at
# posistion 0 and 1
iteration_of_players = {
    0: list_of_players_1,
    1: list_of_players_3,
    2: list_of_players_2,
    3: list_of_players_4

}

# cards on table is a dic that keeps the cards in a specific order,
# 0 is the player, 1 is the teammate, 2 and 3 or the opponents cards.
cards_on_table = {
    0: Card(Suit.NONE, -1),
    1: Card(Suit.NONE, -1),
    2: Card(Suit.NONE, -1),
    3: Card(Suit.NONE, -1)
}
inital_suit = Suit.HEART


def __init_deck():
    deck = list()
    for i in range(2, 15):
        deck.append(Card(Suit.HEART, i))
        deck.append(Card(Suit.DIAMOND, i))
        deck.append(Card(Suit.SPADE, i))
        deck.append(Card(Suit.CLUB, i))

    return deck


def shuffle_cards(current_deck):
    for i in range(random.randint(1, 10)):
        shuffle(current_deck)
        return current_deck


def deal_5(deck):
    five_cards = list()
    for i in range(5):
        five_cards.append(deck.pop())
    return five_cards


def deal_4(deck):
    four_cards = list()
    for i in range(4):
        four_cards.append(deck.pop())
    return four_cards


def shift_list(winning_pos):
    if winning_pos == 0:
        return 0
    elif winning_pos == 1:
        return -1
    elif winning_pos == 2:
        return -2
    return 1


deck = __init_deck()
current_cards = shuffle_cards(deck)

# pick the first hawkhem(the first king)
index_of_king = random.randint(0, 3)
index_of_starter = index_of_king
first = True
comp = Comp()
while match_run:

    for player in iteration_of_players[index_of_king]:
        player.add_cards(deal_5(current_cards))
        if first:
            comp.set_hokm(player.select_hokm())
            print('Hokm is {0}'.format(comp.hokm))
            first = False

    # break
    for player in iteration_of_players[index_of_king]:
        player.hokm = comp.hokm

    for i in range(2):
        for player in iteration_of_players[index_of_king]:
            player.add_cards(deal_4(current_cards))

    # print(teammate.play_card(None, None, -1))
    # for player in iteration_of_players[index_of_king]:
    #      print(player.player_number, '   ', player.hand)
    # break
    while game_run:
        for player in iteration_of_players[index_of_starter]:
            comp.set_and_comp(player.player_number,
                              player.play_card(comp.initial_suit, comp.switcher_2, comp.high_card_index))

        index_of_starter = comp.high_card_index

        comp.print_cards()
        # allow AI to know which cards have been played.
        for player in iteration_of_players[index_of_starter]:
            player.update_cards_played(comp.switcher_2, comp.initial_suit)

        if comp.high_card_index < 2:

            team1.hands_won = team1.hands_won + 1
            print(colored('Team1 won the hand', 'cyan'))
            string1 = '\nteam 1 has {0} points team2 has {1} points\n'.format(team1.hands_won, team2.hands_won)
            print(colored(string1, 'red'))
            if team1.hands_won == 7:
                team1.games_won = team1.games_won + 1

                string1 = 'End of Game team 1 won {0} games and team 2 won {1}'.format(team1.games_won,
                                                                                       team2.games_won)
                print(colored(string1, 'magenta', attrs=['bold', 'dark']))
                team1.hands_won = 0
                team2.hands_won = 0
                if index_of_king > 1:
                    index_of_king = (index_of_king - 1) % 2
                comp.new_game_reset()
                break
        else:

            team2.hands_won = team2.hands_won + 1
            print(colored('Team2 won the hand', 'yellow'))
            string1 = '\nTeam1 has {0} points Team2 has {1} points\n'.format(team1.hands_won, team2.hands_won)
            print(colored(string1, 'red'))
            if team2.hands_won == 7:
                team2.games_won = team2.games_won + 1

                string1 = 'End of Game team 1 won {0} games and team 2 won {1}'.format(team1.games_won,
                                                                                       team2.games_won)
                print(colored(string1, 'magenta', attrs=['bold', 'dark']))
                team1.hands_won = 0
                team2.hands_won = 0
                if index_of_king < 1:
                    index_of_king = index_of_king + 2
                comp.new_game_reset()
                break
        comp.after_hand_reset()

    index_of_starter = index_of_king
    first = True
    current_cards = shuffle_cards(__init_deck())
    for player in iteration_of_players[index_of_starter]:
        player.reset_hand()

    if team1.games_won == 7 or team2.games_won == 7:
        string1 = 'End of Match team 1 won {0} games and team 2 won {1}'.format(team1.games_won, team2.games_won)
        print(colored(string1, 'magenta', attrs=['bold', 'dark']))
        break
