import time

startTime = time.time()

input = open("input.txt", "r")
stringInput = []
cleanInput = []
total = 0

# strip newlines, add as strings to array before transposing

for line in input:
    stringInput.append(line.strip("\n"))

inputNumberRows = len(stringInput)-1
transposedInput = []

# print(stringInput)

for i in range(0, len(stringInput[0])):
    transposedString = ""
    for j in range(0, inputNumberRows):
        transposedString += stringInput[j][i]
    transposedString = transposedString.strip()
    if len(transposedString) > 0:
        transposedInput.append(int(transposedString))
    else:
        transposedInput.append(0)
transposedInput.append(0)

numberOperators = stringInput[-1].split()

#print(numberOperators)
print("Length of number operators line: ", len(numberOperators))
#print(transposedInput)
print("Length of transposed input:" ,len(transposedInput))
 
# 2783 numbers, so 227 are missing once transposed, should be 3*operators which is 1000 in this case
# 999 lines not transposed which should be all dividing lines
# why am I still missing numbers? Does the input vary the number of values per operator?
# number of values before an operator varies, need to combine the values? OR also add the empty string


# calculate
numberIndex = 0
for i in range(0, len(numberOperators)): 
    try:
        if numberOperators[i] == "+":
            subTotal = 0
            while transposedInput[numberIndex] != 0:
                subTotal += transposedInput[numberIndex]
                numberIndex +=1
        else:
            subTotal = 1
            while transposedInput[numberIndex] != 0:
                subTotal = subTotal * transposedInput[numberIndex]
                numberIndex +=1
        total += subTotal
    except: print("Failed to complete at operator: ", i, " operator: ", numberOperators[i] , " numberIndex: ", numberIndex)
    numberIndex += 1
    
print(total)
print((time.time()-startTime)*1e3, "ms")

# 41285959599856972 too high
# 6019576288487
