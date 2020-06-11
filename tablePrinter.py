def printTable(tableData):
    all_values = []
    colWidths = [0] * len(tableData)
    # creates a list of 0s for how many items (sublists) there are
    #colWidths = [0, 0, 0]
    for i in range(1, len(tableData) - 1):
        


printTable([['z', 'ab', 'abc', 'abbb'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']])