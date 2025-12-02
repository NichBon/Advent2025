#read
input = open("input.txt", "r")

invalidSum = 0
#split to array
inputRangesArr = input.read().rstrip().split(',')

#reminder python loops don't include the last value
for IDRange in inputRangesArr:
    limits = IDRange.split('-')
    lower = int(limits[0])
    upper = int(limits[1])

    for i in range(lower, upper+1):
        numString = str(i)
        length = len(numString)
        midpoint = length/2
        if length % 2 == 0 and numString[:int(midpoint)] == numString[int(midpoint):]:
            invalidSum += i

print(invalidSum)