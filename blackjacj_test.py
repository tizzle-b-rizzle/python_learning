# usualy 6 decks (no jokers)
# face cards are all 10, ace can be 1 or 11 (give option to decide at beginning?)
# dealer will hit if their cards are >17, 17 and above, they'll stand

import random

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
    new_player_card = int(full_deck[i])
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
        new_player_card = new_player_card
        print("The dealer deals you a " + str(new_player_card))
    player_cards[0] += new_player_card
# once a card has been dealt to the player, it will be removed fom the deck
    full_deck.remove(int(new_player_card))
    print("The total value of your cards is " + str(player_cards[0]))
    if player_cards[0] > 21:
        print("You go bust; the house wins.\nBetter luck next time!")


def dealer_hit():
    global full_deck
    global dealer_cards
    j = random.randint(0, len(full_deck)-1)
    new_dealer_card = int(full_deck[j])
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
        new_dealer_card = new_dealer_card
        print("The dealer reveals a " + str(new_dealer_card))
    dealer_cards[0] += new_dealer_card
# once the dealer has dealt their own card, it will be removed fom the deck
    full_deck.remove(int(new_dealer_card))
    print("The total value of the dealer's cards is " + str(dealer_cards[0]))
    if dealer_cards[0] > 21:
        print("The house goes bust, you win!")


''

ace_question()  # first thing user sees, asks them if they want aces to be high or low


player_hit()

dealer_hit()


def hit_or_stand_question():
    hit_or_stand = input(
        "Would you like to hit, or stand?\nPress 'h' to hit, 's' to stand\n")
    if hit_or_stand == "h":
        player_hit()
    elif hit_or_stand == "s":
        dealer_hit()
    else:
        hit_or_stand_question()


while player_cards[0] < 21 and dealer_cards[0] < 21:
    hit_or_stand_question()

#move player_hit() and dealer_hit() into the while loop, then hit_or_stand in the other functions
