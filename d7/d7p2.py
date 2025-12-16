import time

startTime = time.time()

input = open("input.txt", "r")
previousLine = list(input.readline().strip("\n").replace("S", "|"))
lineLength = len(previousLine)
for i in range(0, lineLength):
    if previousLine[i] == '|':
        previousLine[i] = 1

#count number of ways to get to each section
#total timelines = total number of ways to get to each section of the final line
for line in input:
    currentLine = list(line.strip("\n"))
    for i in range(0, lineLength):
        if type(previousLine[i]) == int:
            if currentLine[i] == '^':
                if i> 0:
                    if currentLine[i-1] == '.':
                        currentLine[i-1] = previousLine[i]
                    elif type(currentLine[i-1]) == int:
                        currentLine[i-1] += previousLine[i]
                if i+1 < lineLength:
                    if currentLine[i+1] == '.':
                        currentLine[i+1] = previousLine[i]
                    elif type(currentLine[i+1]) == int:
                        currentLine[i+1] += previousLine[i]
            elif currentLine[i] == '.':
                currentLine[i] = previousLine[i]
            elif type(currentLine[i]) == int:
                currentLine[i] += previousLine[i]

    for i in range(0, lineLength):
        previousLine[i] = currentLine[i]

timelines = 0
for value in currentLine:
    if type(value) == int:
        timelines += value

print(currentLine)
print(timelines)

print((time.time()-startTime)*1e3, "ms")