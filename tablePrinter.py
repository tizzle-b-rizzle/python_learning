def printTable(tableData):
    all_values = []
    # creates a list of 0s for how many items (sublists) there are
    #colWidths = [0, 0, 0]
    for i in range(0, len(tableData)):
        for str in tableData[i]:
             str = len(str) #turns each str into the length of itself (e.g. apple would = 5)
             all_values.append(str) #adds the above values to the all_values list
             final_list = " ".join(tableData[i])
    final_width = max(all_values)
    #print(final_width)
    print(final_list.rjust(final_width, "-"))   #CLOSE

printTable([['z', 'ab', 'abc', 'abbb'],
            ['Alice', 'Bob', 'Carol', 'Davidlalal'],
            ['dogs', 'cats', 'moose', 'goose']])