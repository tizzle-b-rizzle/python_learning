#a list is typed between two square brackets and seperated by commas
list1 = [1, 2, 3, 4, 5]

#to get one term of a list we can use "list[(n-1)]" where n = the term of the list. So in the below example, list1[2] will print "3"
print(list1[2])
#you can use negative numbers to go from the end of the list. -1 is the last term, minus 2 is the second-to-last and so on. The following example will print "3"
print(list1[-3])

#if you have lists inside of lists you can use multiple pairs of square brackets, with each pair going further into a list
list2 =[[1, 2, 3, 4, 5], ["cat", "rat", "bat"]]
#the below examples will print "5" and "rat" respectivley
print(list2[0][4])
print(list2[1][1])

#you can uses slices to return multiple values in a row from a list. The syntax is list[a:b] where a is where the splice will start from, and b is where the slice will go up to (but not include)
#the following will print "[3, 4, 5]"
print(list1[2:5])
#you can omit the numbber before the colon and it will set the start of the slic as the first term, and you can omit the second number and the slice will go up to the last term
#the following will print "[1, 2, 3]" and ["4,5"] repectively
print(list1[:3]) 
print(list1[3:])

#you can use len(list) to get the length of a list
print("The length of list 1 is " + str(len(list1)))
list3 = ["eenie", "meenie", "minie", "moo"]
#you can change the value of values in a list
list3[3] = "cow"
print(list3)
list3[0] = list3[3]
print(list3)

#you can add lists together with +
print(list1 + list2)
#you can multiply a list by an integer to replicate it
print(list1 * 5)

#you can delete items using del(list[n])
list4 = [1, 2, 3, 4, 5]
del list4[4]
print(list4)

#working with lists, you can use something like below to have a list where people add stuff to the list instead of naming 100 variables
list100 = []
list100 = list100 +[2]
print(list100)

#an example of using for loops with lists
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
 print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


#you can use '"" in list' to see if an item is in a list
2 in list1 #this will print"True"
"cat" in list1 #this will print False

#this can be used quite easily in function
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
 print('I do not have a pet named ' + name)
else:
 print(name + ' is my pet.')

 #you can use lists to assign multiple variables in 1 line of code
listcolour = ["red", "blue", "green"] #note! the no of variable and length of list but be exactly the same, or you'll get ValueEror
r, b, g = listcolour
print(r)

#if you want to do variable = variable (mathimatical operation) (number) you can use variable (opertaion)= number. example below
one_hundered = 100
one_hundered += 1
print(one_hundered)
#a method is sort of like a function. The syntax is variable.method(value). I can use index to see where a value is in a list, like you see below
print(listcolour.index("green"))

#you can use variable.append(new value) to add an item to the end of a list, as seen below
listcolour.append("yellow")
print(listcolour)

#insert does the same thing but for any place in the list. The syntax is variable.insert(index, value).  Here I'll add "purple" to be the third value. 
listcolour.insert(2, "purple")
print(listcolour)

#note how append/insert doesn't return the new list, only trasforms. Without either of the two prints above, the lists wouldn't be printed

#similar to how you can use del(list[value's index]) to remove a vlue with its index, you can use list.remove(value) to just remove a value, regardless of posiiton
listcolour.remove("purple")
print(listcolour)
#if there are multiple items with the same value, remove will just remove the first one

#list.sort() can be used to order a list numerically or alphabetically.
wrongordernumber = [2, 4, 6, 1 ,6 ,2 ,5 ,9]
wrongordernumber.sort()
print(wrongordernumber)
wrongorderletter = ["f", "k", "r", "j", "a"]
wrongorderletter.sort()
print(wrongorderletter)
#you can also use .sort(reverse=True) to have the list prnted backwards
wrongordernumber.sort(reverse=True)
print(wrongordernumber)

#you can do many of the del[] remove etc things for a string as well
name ="Tyler"
print(name[0])
for i in name:
    print(i)

#however you cannot change any of the values of a string
#>>>name[7] = "the" wouldn't print an error

#the proper way would be to slice like in the below example
namex ="Tyler fit"
namex2 = namex[0:6] + "is " + namex[6:]
print(namex2)

#as well as lists you have tuple's, which are similar but the syntax is tuple() and similar to strings, they are immutable
#if your uple has only 1 value, you need to put a comma in or it'll think you have a string
#("cat",) is a tuple, ("cat") is a string

#you can use list() and tuple() in order to turn a list, string, or tuple into a list or tuple