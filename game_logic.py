from card import Card
from suit import Suit
from random import shuffle
from player import Player
from init_ai import init_AI
from team import Team

import random

game_run = True
match_run = True
human = Player(1)
teammate = inital_AI(1, 1)
opponent_1 = inital_AI(2, 2)
opponent_2 = inital_AI(2, 3)
team1 = Team(human, teammate)
team2 = Team(opponent_1, opponent_2)

list_of_players = [human, teammate, opponent_1, opponent_2]
cards_on_table = list()
inital_suit = Suit.HEART

def __init_deck():
    deck = list()
    for i in range(2,15):
        deck.append(Card(Suit.HEART,i))
        deck.append(Card(Suit.DIAMOND,i))
        deck.append(Card(Suit.SPADE,i))
        deck.append(Card(Suit.CLUB,i))

    return deck


def shuffle_cards(current_deck):
    for i in range(random.randint(1,10)):

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

while match_run:
    human.add_cards(deal_5(current_cards))
    hokm = human.select_hokm()
    teammate.add_cards(deal_5(current_cards))
    teammate.select_hokm()
    opponent_1.add_cards(deal_5(current_cards))
    opponent_1.select_hokm()

    opponent_2.add_cards(deal_5(current_cards))
    opponent_2.select_hokm()

    # break

    for i in range(2):
        human.add_cards(deal_4(current_cards))
        teammate.add_cards(deal_4(current_cards))
        opponent_1.add_cards(deal_4(current_cards))
        opponent_2.add_cards(deal_4(current_cards))

    print(teammate.play_card(None, None, -1))
    break
    # while game_run:
    #     card1 = list_of_players[0].play_card(None, cards_on_table)
    #     cards_on_table.append((card1,list_of_players[0]))
    #
    #     card2 = list_of_players[1].play_card(card1.suit, cards_on_table)
    #     cards_on_table.append((card2,list_of_players[1]))
    #
    #     card3 = list_of_players[2].play_card(card1.suit, cards_on_table)
    #     cards_on_table.append((card3,list_of_players[2]))
    #
    #     card4 = list_of_players[3].play_card(card1.suit, cards_on_table)
    #     cards_on_table.append((card4,list_of_players[3]))
    #
    #     winning_pos = high_card(card1.suit, cards_on_table, hokm)
    #     winner = list_of_players[winning_pos]
    #     if winner == human or ai_2:
    #         team1.hands_won = team1.hands_won + 1
    #         list_of_players.rotate(shift_list(winning_pos))
    #         if team1.hands_won == 7:
    #             team1.games_won = team1.games_won + 1
    #             team1.hands_won = 0
    #             team2.hands_won = 0
    #             break
    #     else:
    #         team2.hands_won = team2.hands_won + 1
    #         list_of_players.rotate(shift_list(winning_pos))
    #         if team2.hands_won == 7:
    #             team2.games_won = team2.games_won + 1
    #             team1.hands_won = 0
    #             team2.hands_won = 0
    #             break
    #
    #
    # # print('human ' , human.hand)
    # # print('ai_1 ', ai_1.hand)
    # # print('ai_2 ', ai_2.hand)
    # #
    # # print('ai_3 ', ai_3.hand)
    #
    #
    # break