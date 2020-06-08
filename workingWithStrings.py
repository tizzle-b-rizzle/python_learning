#the join() method is useful for joining a list of strings together
list = ["Tyler", "Chris", "Louie", "Luke"]
print(", ".join(list))
#whatever is put before the .join is what will seperate each item

#.split() does the opposite, but how it splits a string is determined by what's in the ()
#for example .split() would split the string anytime it sees a space, whereas .split("\n") would split the string everytime there's a newline
poem = """There once was a man from Peru
          Who dreamt of eating his shoes
          He woke with a fright
          In the middle of the night
          To find that his dream had come true"""
print(poem.split("\n"))

#.rjust() and .ljust() allow you to add spaces/other characters to the left and right of the string respectively
#The first argument is the number of characters, the second is what type of character"
print("Hello".ljust(10, "-"))
#.center does the same but for left and right together, effectively centering the string

#.strip, .lstrip, .rstrip will remove all white space, all the the left white space, and all the right white space respectively
print("         Hello".lstrip())
#you can put a character in the () to remove that character from the strip
