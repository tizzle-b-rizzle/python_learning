import re

password = input("""Please enter a password
Your password must must contain at least 8 characters,
at least one upper case and lower case character,
and contain at least one number.\n""")

regexUpperCharacters = re.compile(r'([A-Z])+')
regexLowerCharacters = re.compile (r'([a-z])+')
regexDigits = re.compile (r'([0-9])+')

moRUC = regexUpperCharacters.search(password)
moRLC = regexLowerCharacters.search(password)
moD = regexDigits.search(password)

if moRUC == False:
    print("Please make sure that your password contains at least one upper case character")
elif moRLC == False:
    print("Please make sure that your password contains at leasr one lower case character")
elif moD == False:
    print ("please ensure your password contains at least one number")

#doesn't work yet :(

    
