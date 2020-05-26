import random #imports the random library

def magic_8_ball_answer(functionName): #the function for the 8 ball. "functionName is randomly generated below, and based on the outcome, something will be printed"
    if functionName == 1:
       return "Yes"
    elif functionName == 2:
       return "No"
    elif functionName == 3:
       return "100%, absolutely!"
    elif functionName == 4:
       return "Literally never. Why would you even think that?"
    elif functionName == 5:
       return "Dunno lol"
    elif functionName == 6:
       return "Ask again, more politely"
    elif functionName == 7:
       return "Help! I'm stuck in a magic 8 ball factory!"
    elif functionName == 8:
        return "[sigh] Go on then, just for you"
    elif functionName == 9:
       return "Sure, why not"

n = random.randint(1, 9) #randomly generates a number between 1 and 9
answer = magic_8_ball_answer(n) #the variable "asnwer" is equal to the function of magic_8_ball_answer with the randomly generated answer above
print(answer) #prints the above variable
