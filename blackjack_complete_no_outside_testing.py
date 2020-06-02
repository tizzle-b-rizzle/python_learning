# usualy 6 decks (no jokers)
# face cards are all 10, ace can be 1 or 11 (give option to decide at beginning?)
# dealer will hit if their cards are >17, 17 and above, they'll stand

import random
import sys

deck = [  # one full deck (no jokers)
    "ace",
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    "jack",
    "queen",
    "king",
]


full_deck = deck
player_cards = [0]
dealer_cards = [0]
dealer_stand = ""
player_stand = ""

def endgame_call():
    endgame()

def endgame():
    global player_cards
    global dealer_cards
    global player_stand
    global dealer_stand
    endgame = input(
        "Would you like to play again?\nHit 'y' to play again, 'n' to exit\n")
    if endgame == "y":
        player_cards = [0]
        dealer_cards = [0]
        dealer_stand = ""
        player_stand = ""
        ace_question()
        player_hit()
    elif endgame == "n":
        exit()
    else:
        endgame_call()



def endgame_comparison():
    global player_cards
    global dealer_cards
    if player_cards[0] > dealer_cards[0]:
        print("The value of your cards is higher than the house's, you win!")
        endgame()
    elif dealer_cards[0] > player_cards[0]:
        print(
            "The house's cards are greater than yours, the house wins.\nBetter luck next time!")
        endgame()


def hit_or_stand_question_comparison():
    if player_stand == "true" and dealer_stand == "true":
        endgame_comparison()
    else:
        hit_or_stand_question()


def hit_or_stand_question():
    global player_stand
    global dealer_stand
    hit_or_stand = input(
        "Would you like to hit, or stand?\nPress 'h' to hit, 's' to stand\n")
    if hit_or_stand == "h":
        player_hit()
    elif hit_or_stand == "s":
        player_stand = "true"
        if dealer_cards[0] > player_cards[0]:
            print("You lose, better luck next time!")
            endgame()
        dealer_hit()
    else:
        hit_or_stand_question()


def ace_question():
    global full_deck
    ace_answer = input(
        "Would you like aces to be high or low?\nHit 'h' or 'l' and then hit 'enter'\n")
    if ace_answer == "h":
        deck[0] = 11  # turns the ace into an 11
        full_deck = deck * 24
    elif ace_answer == "l":
        deck[0] = 1  # turns the ace into a 1
        full_deck = deck * 24
    else:
        ace_question()


def player_hit():
    global full_deck
    global player_cards
    i = random.randint(0, len(full_deck)-1)
    new_player_card = full_deck[i]
    if new_player_card == "king":
        new_player_card = int(10)
        print("The dealer deals you a king")
    elif new_player_card == "queen":
        new_player_card = int(10)
        print("The dealer deals you a queen")
    elif new_player_card == "jack":
        new_player_card = int(10)
        print("The dealer deals you a jack")
    else:
        new_player_card = int(new_player_card)
        print("The dealer deals you a " + str(new_player_card))
    player_cards[0] += new_player_card
    print("The total value of your cards is " + str(player_cards[0]))
    if player_cards[0] > 21:
        print("You go bust; the house wins.\nBetter luck next time!")
        endgame()
    elif player_cards[0] == 21:
        print("You got Blackjack! You Win!")
        endgame()
    else:
        dealer_hit()


def dealer_hit():
    global full_deck
    global dealer_cards
    global dealer_stand
    j = random.randint(0, len(full_deck)-1)
    while dealer_cards[0] < 17:
        new_dealer_card = full_deck[j]
        if new_dealer_card == "king":
            new_dealer_card = int(10)
            print("The dealer reveals a king")
        elif new_dealer_card == "queen":
            new_dealer_card = int(10)
            print("The dealer reveals a queen")
        elif new_dealer_card == "jack":
            new_dealer_card = int(10)
            print("The dealer reveals a jack")
        else:
            new_dealer_card = int(new_dealer_card)
            print("The dealer reveals a " + str(new_dealer_card))
        dealer_cards[0] += new_dealer_card
        print("The total value of the dealer's cards is " +
              str(dealer_cards[0]))
        if dealer_cards[0] > 21:
            print("The house goes bust, you win!")
            endgame()
        if dealer_cards[0] == 21:
            print("The house got Blackjack.\nBetter luck next time!")
            endgame()
        elif dealer_cards[0] == 17 or dealer_cards[0] > 17:
            print("The dealer stands")
            dealer_stand = "true"
            hit_or_stand_question_comparison()
        else:
            hit_or_stand_question_comparison()


''

ace_question()  # first thing user sees, asks them if they want aces to be high or low
player_hit()
