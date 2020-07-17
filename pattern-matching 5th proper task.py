import re

def fakeStripFunction():
    stringInput = input("Please enter the string that you want to remove characters from.\n")
    removeInput = input("Please enter what you would like removing form that string\nIf left blank, whitespace will be removed from your string.\n")
    regex = re.compile(removeInput)
    
