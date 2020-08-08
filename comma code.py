list1 = ["cat", "dog", "sheep"]
def comma_code(some_list):
    sentence = ""
    for i in range(len(some_list)-1): #it goes through the length of the list aside from the last item
        sentence += some_list[i] + ", " #"sentence" becaomes each item on teh list then a comma, aside form the last item
    print(sentence + "and " + some_list[len(some_list)-1]) #prints "sentence" and the word "and" and the last item
