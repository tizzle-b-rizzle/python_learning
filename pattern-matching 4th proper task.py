import re #imports the regex function

def passwordFunction(): #creates a function
    password = input("Please enter a password.\nPlease make sure your password contains at least one upper case character, one lower case character, and at least one digit.\n") #what the user is asked
    passwordRegex = re.compile(r'([a-zA-Z0-9])+') #looks for at least one upper case character, lower case character, and digit 
    passwordMatchObject = passwordRegex.search(password) #searches for the above pattern in the password that the user inputted
    if passwordMatchObject == None: #if all of these conditions are not fufilled, passwordMatchedObject would == None. Should this be the case, the below will be printed
        print("Your password is not strong!")
    else: #the password is either strong, or not, so if the password is strong than the below shall be printed
        print("Wow! " + password + " is such a strong password!")

passwordFunction()
