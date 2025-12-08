import time

startTime = time.time()

def withinRange(number, lower, upper):
    if number >= lower and number <= upper:
        return True 

input = open("input.txt", "r")

#Initialise
idRanges = []

#Massage input into arrays
line = input.readline()
while line != "\n":
    tempRange = line.strip('\n').split('-')
    for i in range(0, 2):
        tempRange[i] = int(tempRange[i])
    idRanges.append(tempRange)
    line = input.readline()

idRanges.sort(key= lambda x: x[0])

#iterate through fresh ids to find fresh ingredients
freshIdRanges = [idRanges[0]]
print("ID ranges: ",len(idRanges))

for lower, upper in idRanges:
    newIdRange = True

    lowerInRange = lower <= freshIdRanges[-1][1]
    upperInRange = upper <= freshIdRanges[-1][1]

    if lowerInRange and not upperInRange:
        freshIdRanges[-1][1] = upper
    elif not lowerInRange:
        freshIdRanges.append([lower, upper])
            
freshIds = 0
for start, end in freshIdRanges:
    freshIds += end - start + 1

print(freshIdRanges)
print(freshIds)
print((time.time()-startTime)*1e3, "ms")