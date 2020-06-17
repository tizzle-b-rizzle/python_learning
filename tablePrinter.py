def printTable(tableData):
    # creates a list of 0's that is as long as the no of sublists in tableData
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            # loops through each sublist and replaces each colWidths value with the highest value
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    for x in range(len(tableData)):
        for y in range(len(tableData[0])):
            print(tableData[x][y].rjust(colWidths[x], " "))


printTable([['z', 'ab', 'abc', 'abbb'],
            ['Alice', 'Bob', 'Carol', 'Davidlalal'],
            ['dogs', 'cats', 'moose', 'goose']])
