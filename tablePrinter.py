def printTable(tableData):
    all_values = []
    colWidths = [0] * len(tableData)
    # creates a list of 0s for how many items (sublists) there are
    #colWidths = [0, 0, 0]
    for i in range(0, len(tableData)):
        for str in tableData[i]:
             str = len(str)
             widths = []
             widths.append(str) #CLOSE, only need to get all of them into one list, not separate lists
             print(widths)
             

printTable([['z', 'ab', 'abc', 'abbb'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']])