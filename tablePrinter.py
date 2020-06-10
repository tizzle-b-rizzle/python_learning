def printTable(tableData):
    colWidths = [0] * len(tableData)
    # creates a list of how many items in each sublist
    colWidths
    for i in range(1, len(tableData) + 1):
        for j in range(1, len(colWidths) - 1):
            colWidths[j] = max(tableData[i-1])
            finalWidth = max(colWidths[j])
            print(finalWidth)


printTable([['z', 'ab', 'abc', 'abbb'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']])
