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
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo.group(1) would = 415
# mo.group() returns all groups, mo.groups() returns a tuple of all groups

# you can use | (a pipe) to match multiple expressions
#heroRegex = re.compile (r'Batman|Tina Fey')
#mo1 = heroRegex.search('Batman and Tina Fey.')
# mo1.group()
# Batman
# when both are matched, only the first will be returned, as shown above

# if you want to find at items that all have the same prefix, you can also use a pipe
# eg
#batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#mo = batRegex.search('Batmobile lost a wheel')
# mo.group()
# 'Batmobile'
# mo.group(1)
# 'mobile'
# The search will look for any of those words: Batman, Batmobile, Batcopter, Batbat
# group(1) returns 'mobile' because that's the second item in the regex brackets

# you can use a ? after () to show that there should be a match if the group in the () is there or not
# eg re.compile(r'Bat(wo)?man') would find a match with "Batman" and "Batwoman"
# essentially the ? means "match 1 or 0 of this" which can be useful if phones have area codes or not

# you can use a * after () to say "match 0 or more"
# so re.compile(r'(bat)*man') would find 'batman' and 'man' and 'batbatbatbatbatbatbatbatman'
# you can use a + after the () to mean "match 1 or more"

# if you want to match a certain amount, you can use ("thing you're looking for"){amount you wnat to find}
# eg regex = re.compile(r'(ha){3}') would match "hahaha"
# you can use a , to give a range
# eg {3,5} means match between 3 and 5, {,5} means match 0 to 5, {5,} means match 5 or more
# {3,5} is much quicker than writing {hahaha|hahahaha|hahahahaha}

# regexs are greedy by default, this means they'll match the longets string possible
# eg regex = re.compile(r'(ha){3,5}')
#mo = regex.search("hahahahaha")
# mo.group() would return "hahahahaha" because that's the longest match
# to make something nongreedy (i.e. return the smallest possible string) we put a ? after the {}
# the above code but with re.compile(r'(ha){3,5}?)') would return "hahaha"

# you can match anything with .*, the . means any non-newine character, and the * means zero or more of the preceeding caracter
# so re.complie(r'First Name: (.*)') will match anything after "First Name:"
# .* is greedy by default, you cna use a ? at the end
# so re.compile(r'<.*?>') on <yes>yes> will match <yes> but without the ? it would match <yes>yes>
# you can use re.DOTALL to as the second argument in re.compile in order to match all characters including newline

# if you want to match a string regardless of whether it has capital letters, you can put re.I or re.IGNORECASE as the recond argument of re.compile
# eg re.compile(r"hello", re.I) would match "hello", "HELLO", and "hElLo"

#you can use .sub() to sub in new words to replace the strings you're matching
#so if you had regex=re.compile(r'Hello') , regex.sub(r'goodbye', string) would sub any "Hello" with "goodbye" in that string
#you can use .sub(\1), .sub(\2) etc to say "insert the text form group 1/2" and so on
#eg let's say you want to only sow the first letter of something and censor the rest:
#you'd do regex=re.compile(r'(\w)w+') (this is just a word but the first letter is in its own group)
#then you can do regex.sub(r'\1****', Tyler) this would return T**** because the T is in its own group

#just did this to get the github ting
