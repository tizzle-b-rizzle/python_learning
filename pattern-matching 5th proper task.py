import re

def fakeStripFunction(string):
    regex = re.compile(r'()*(string)()*')
    regex.sub(string)
