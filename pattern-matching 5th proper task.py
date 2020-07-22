import re

def fakeStripFunction(string=""):
    regex = re.compile(r'( *)(.*)( *)')
    mo = regex.search(string)
    output1 = regex.sub(mo.group(2), string)
    print(output1)
fakeStripFunction("     cat       ")
