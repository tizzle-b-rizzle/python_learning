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
# 'mobile's
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

#.search() will return the first matched-item if there are multiple, to match multiple you use .findall()
#if the regex has no groups, findall will return a list, if there are groups then findall will return a list of tuples, each tuple containing all of the matched groups
# eg if the regex is  re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') then .findall('Cell: 415-555-9999 Work: 212-555-0000') would return ['415-555-9999', '212-555-0000']
# if the regex is  (r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') then .findall('Cell: 415-555-9999 Work: 212-555-0000') would return [('415', '555', '1122'), ('212', '555', '0000')]

#earlier we know that \d meant "match a digit 0 to 9", here are some others
#\D means match a charcter that ISN'T a digit 0 to 9
#\w means match any underscore charcter, letter, or numeric digit, \W matches NOT all of them
#\s matches any space, tab, or newline character, \S matches any of NOT them

#you can make your own character class using []
#eg re.compile(r'[aeiouAEIOU]') will match all vowels, upper and lower case
#you can use a - to get a range 
#eg re.comple(r'[0-9a-zA-Z]') will match all digits and uper and lower case letters
#everything in the [] will be matched, including punctuation such as \
#you can use a ^ right before the [] to match everything except what's inside the []
#eg re.compile(^[0-9]) will match everything aside from 0-9