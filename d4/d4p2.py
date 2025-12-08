import copy
input = open("input.txt", "r")

def accessiblePaperCheck(row, column, rowCount, columnCount, paperArray):
    if paperArray[row][column] != "@": return False
    adjacent = -1
    #print("column boundaries: ", column - 1 if column -1 > 0 else 0 , column + 1 if column + 1 < columnCount else column)
    for columnToCheck in range(column - 1 if column -1 > 0 else 0 , column + 2 if column + 1 < columnCount else columnCount):
        for rowToCheck in range(row - 1 if row -1 > 0 else 0, row + 2 if row + 1 < rowCount else rowCount):
            #print(row)
            try:
                #print(columnToCheck, rowToCheck, paperArray[rowToCheck][columnToCheck])
                if paperArray[rowToCheck][columnToCheck] != ".":
                    adjacent += 1
            except: print("FROM: ", row, column, "Out of bounds: ", rowToCheck, columnToCheck)
    #print(adjacent)
    if adjacent < 4:
        return True
    return False
    

paperArray = []
for line in input:
    paperArray.append(line.strip('\n'))
columnCount = len(paperArray[0])
rowCount = len(paperArray)

accessibleRolls = 0
newlyAccessiblePaper = 1

while newlyAccessiblePaper > 0:
    newlyAccessiblePaper = 0
    nextPaperArray = copy.deepcopy(paperArray)

    for rowIndex, row in enumerate(paperArray):
        currentRow = list(nextPaperArray[rowIndex])
        for columnIndex, cell in enumerate(row):
            if (accessiblePaperCheck(rowIndex, columnIndex, rowCount, columnCount, paperArray)):
                    newlyAccessiblePaper += 1
                    currentRow[columnIndex] = "."
                    nextPaperArray[rowIndex] = "".join(currentRow)
    
    accessibleRolls += newlyAccessiblePaper
    paperArray = nextPaperArray


for row in paperArray:
    print(row)
print(accessibleRolls)

#accessiblePaperCheck(1, 0, 10, 10, paperArray)