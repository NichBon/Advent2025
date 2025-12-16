import time
import copy

startTime = time.time()

input = open("input.txt", "r")
previousLine = list(input.readline().strip("\n").replace("S", "|"))
lineLength = len(previousLine)
splitCount = 0

for line in input:
    currentLine = list(line.strip("\n"))
    for i in range(0, lineLength):
        if previousLine[i] == '|' and currentLine[i] == '^':
            splitCount += 1
            if currentLine[i-1] == '.' and i > 0:
                currentLine[i-1] = '|'
            if currentLine[i+1] == '.' and i+1 < lineLength:
                currentLine[i+1] = '|'
        elif previousLine[i] == '|' and currentLine[i] == '.':
            currentLine[i] = '|'
    previousLine = copy.deepcopy(currentLine)

print(currentLine)
print(splitCount)

print((time.time()-startTime)*1e3, "ms")