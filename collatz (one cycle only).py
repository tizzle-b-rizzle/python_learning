#collatz
#if number is even, half it
#if number is odd, multiply it by 3 and then +1

def collatz(number):
    if int(number) % 2 == 0:
        print(number/2)
    elif int(number) % 2 == 1:
        print(number * 3) + 1
collatz(11)
