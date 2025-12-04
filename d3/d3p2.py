input = open("input.txt", "r")

def maxVoltage(numString, outputLength):
    maxSequence = ""
    index = -1
    numString = numString.strip()

    for voltageDigit in range(0, outputLength):
        max = "0"
        for i in range(index + 1, len(numString)-(outputLength - voltageDigit)+1):
            if numString[i] > max:
                max = numString[i]
                index = i

        maxSequence += max
 
    return(maxSequence)

totalVoltage = 0
    
for numString in input:
    voltage = maxVoltage(numString, 12)
    totalVoltage += int(voltage)

print(totalVoltage)