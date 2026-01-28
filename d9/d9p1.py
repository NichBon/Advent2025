import time
startTime = time.time()

input = open("input.txt", "r")

coordinates = []
for line in input:
    coordinatePair = line.strip("\n").split(",")
    for i in range(0, len(coordinatePair)):
        coordinatePair[i] = int(coordinatePair[i])
    coordinates.append(coordinatePair)

# for coordinate in coordinates:
#     print(coordinate)

largestArea = 0
largestCoordinate1 = 0
largestCoordinate2 = 0

for i in range(0, len(coordinates) - 1):
    for j in range (i, len(coordinates)):
        area = abs((coordinates[i][0]-coordinates[j][0] + 1)*(coordinates[i][1]-coordinates[j][1]+1))
        if area > largestArea:
            largestArea = area
            largestCoordinate1 = i
            largestCoordinate2 = j

print(largestArea, largestCoordinate1, largestCoordinate2)

print((time.time()-startTime)*1e3, "ms")