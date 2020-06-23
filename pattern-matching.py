# regular expressions (or regexes for short) a descriptions for a pattern of text
# we use them by using 'import re'
# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object)

#phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# the "r" turns it into a raw string so the \ don't ruin the code \d
# "\d" in regex means a digit between 0 and 9, the example on line 5 is like a phone number

# you can use the regex object's search() function to see if a string macthes the regex
# if there is one, it will be returned as a match-object (mo)
# you can use "[mo-name]".group() to return the actual string in the matched object

# eg
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())
# Phone number found: 415-555-4242

# you can add () to a regex to create groups
# eg re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
# the first set of () is goup 1 and so on
#import re
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo.group(1) would = 415
# mo.group() returns all groups, mo.groups() returns a tuple of all groups
