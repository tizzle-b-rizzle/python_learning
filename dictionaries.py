#dictionaries are similar to lists, like how lists have indexes for their data, dictionaries have keyvalues.
dictionary_1 = {"name": "Tyler", "height": "small", "eye_colour": "blues"} 
#in this example, the keys are name, height, and eye_colour, and the values are tyler, small, and blue
#this means the key-value pairs are name and tyler, height and small, and eye_colour and blue
print(dictionary_1["name"])

#unlike lists, dictionaries aren't ordered, this means there is no "first" item in a dictionary which also means that two dictionaries with the same
#content in different orders would be equals

#the following example shows how you can easily store new things in dictionaries
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#while True:
# print('Enter a name: (blank to quit)')
# name = input()
# if name == '':
# break
# if name in birthdays:
# print(birthdays[name] + ' is the birthday of ' + name)
# else:
# print('I do not have birthday information for ' + name)
# print('What is their birthday?')
# bday = input()
# birthdays[name] = bday
 #print('Birthday database updated.')

#use dictionary.keys() to get the key
#use dictionary.values() to get the value
#use dictionary.items() to get a key value

for i in dictionary_1.items():
    print(i)

#you can use "in" or "not in" to see if something is in a dictionary
#Tyler in dictionary_1.values() would be true (you can just put tyler in dictionary_1 and this would also works)

#you can use the get() function to see if something is in a dictionary. The first argument is the key, and the second is the value assigned to that key if they key doesn't exist in the dictionary
#in the below example, because eggs doesn't have a value, it returnd 0 eggs as stated in the get() function
#picnicItems = {'apples': 5, 'cups': 2}
#'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
#'I am bringing 2 cups.'
#'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
#'I am bringing 0 eggs.'

#You can do the same as above butuse setdefault() to add something to the dictionary if it doesn't already exist
noOfAlbums = {"muse": 8, "radiohead": 9}
noOfAlbums.setdefault("ghost", 4)
print(noOfAlbums)

