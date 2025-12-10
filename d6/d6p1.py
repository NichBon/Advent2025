import time
# import json

startTime = time.time()

input = open("input.txt", "r")
cleanInput = []
total = 0

#clean data, strip needless symbols

for line in input:
    cleanInput.append(line.strip("\n").split())

nPerCalc = len(cleanInput)-1

# log = open("log.txt", "w")
# for line in cleanInput:
#     log.writelines(json.dumps(cleanInput))

for i in range(0, nPerCalc):
    for j, number in enumerate(cleanInput[i]):
        cleanInput[i][j] = int(number)

#calculate

for i in range(0, len(cleanInput[0])): 
    subTotal = cleanInput[0][i]
    if cleanInput[-1][i] == "+":
        for j in range(1, nPerCalc):
            subTotal += cleanInput[j][i]
    else:
        for j in range(1, nPerCalc):
            subTotal = subTotal * cleanInput[j][i]
    total += subTotal
print(total)
print((time.time()-startTime)*1e3, "ms")

# 8621639912066 too high
# 3968933219902