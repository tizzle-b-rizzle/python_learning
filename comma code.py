list1 = ["cat", "dog", "sheep"]
def comma_code(some_list):
    sentence = ""
    for i in range(len(some_list)-1):
        sentence += some_list[i] + ", "
    print(sentence + "and " + some_list[len(some_list)-1])
