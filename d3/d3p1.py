input = open("input.txt", "r")

def maxVoltage(numString):
    max = "0"
    secondHighest = "0"

    for i in range(0, len(numString)-2):
        if numString[i] > max:
            secondHighest = numString[i+1]
            max = numString[i]
        elif numString[i] > secondHighest:
            secondHighest = numString[i]

    if numString[len(numString)-2] > secondHighest:
        secondHighest = numString[len(numString)-2]
    return(max + secondHighest)

totalVoltage = 0
line = 1
    
for numString in input:
    voltage = maxVoltage(numString)
    totalVoltage += int(voltage)
    line += 1

print(totalVoltage)