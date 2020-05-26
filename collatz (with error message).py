#collatz
#if number is even, half it
#if number is odd, multiply it by 3 and then +1

def collatz(number):
    try:
        number = int(number)
        while (number) != 1:
            if (number) % 2 == 0:
                number = int((number/2))
                print(number)
            elif int(number) % 2 == 1:
                number = int((number * 3) + 1)
                print(number)
        print("We'll end it here so the cycle doesn't continue forever!")
    except ValueError:
        print("please enter a correct value")
        
choice = input("Enter a number\n")
collatz(choice)