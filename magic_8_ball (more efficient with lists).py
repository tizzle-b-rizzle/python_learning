import random
magic_8_ball_options = [
    "You will guess coin tosses .38% more accurately",
    "Your wife is cheating on you. Even if you don't have a wife, she still is.",
    "You sill struggle to open every 3rd packet of bread that you open",
    "Help, I'm stuck in a magic 8 ball factory!",
    "Try again, idiot",
    "Yes",
    "Ut oh"
]

print(magic_8_ball_options[random.randint(0, (len(magic_8_ball_options) - 1))])