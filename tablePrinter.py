def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
    	    for j in range(len(tableData[i])):
                if len(tableData[i][j]) > colWidths[i]:
                    colWidths[i] = len(tableData[i][j])
                    print(colWidths)

printTable([['z', 'ab', 'abc', 'abbb'],
            ['Alice', 'Bob', 'Carol', 'Davidlalal'],
            ['dogs', 'cats', 'moose', 'goose']])
