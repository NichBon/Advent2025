#read
input = open("input.txt", "r")

invalidSum = 0
#split to array
inputRangesArr = input.read().rstrip().split(',')
#reminder python loops don't include the last value

def checkInvalid(value):
    numString = str(value)
    length = len(numString)

    for i in range(1, length+1):
        if length % i == 0 and i < length:
            for j in range (0, int(length/i)):
                if j >= int(length / i) - 1: 
                    print(value, " is valid with sequence length ",  i)
                    return True
                if numString[i*j: i*(j+1)] != numString[i*(j+1): i*(j+2)]: 
                    break

    return False

for IDRange in inputRangesArr:
    limits = IDRange.split('-')
    lower = int(limits[0])
    upper = int(limits[1])

    for id in range(lower, upper+1):
        if checkInvalid(id) == True: invalidSum += id

print("Sum of invalids: " , invalidSum)