#usualy 6 decks (no jokers)
#face cards are all 10, ace can be 1 or 11 (give option to decide at beginning?)
#dealer will hit if their cards are >17, 17 and above, they'll stand
 
import random

deck = [ #one full deck (no jokers)
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
player_cards = ""
dealer_cards = ""

def ace_question():
    global full_deck
    ace_answer = input("Would you like aces to be high or low?\nHit 'h' or 'l' and then hit 'enter'\n")
    if ace_answer == "h":
        deck[0] = 11 #turns the ace into an 11
        full_deck = deck * 24
    elif ace_answer == "l":
        deck[0] = 1 #turns the ace into a 1
        full_deck = deck * 24
    else:
        ace_question()

def player_hit():
    global full_deck
    global player_cards
    i = random.randint(0, len(full_deck)-1)
    new_player_card = str(full_deck[i])
    if new_player_card == "king":
        new_player_card = str(10)
        print("The dealer hands you a king")
    elif new_player_card == "queen":
         new_player_card = str(10)
         print("The dealer hands you a queen")
    elif new_player_card == "jack":
         new_player_card = str(10)
         print("The dealer hands you a jack")
    else:
        new_player_card = new_player_card
        print("The dealer hands you " + new_player_card)
    player_cards += new_player_card
    full_deck.remove(int(new_player_card))
    print("The total value of your cards is " + player_cards)

#def dealer_hit():           #basically copy above, then work in a function for when the user types "hit" (maybe add to the very first thing maybe)
 #   global full_deck
  #  global dealer_cards
   # j =

ace_question() #first thing user sees, asks them if they want aces to be high or low

print("The dealer deals a card to you")
player_hit()




