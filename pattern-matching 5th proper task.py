import re

def fakeStripFunction(string="", char=""):
    if char == "":
        regex = re.compile(r'( *)([a-zA-Z0-9]*)( *)')
        mo = regex.search(string)
        print(mo.group(2))
    else:
        regex = re.compile(r'[^'+char+'].*[^'+char+']')
        mo = regex.search(string)
        print(mo.group())
        
fakeStripFunction("sheepcatsheep", "sheep")
