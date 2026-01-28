import time
startTime = time.time()

input = open("input.txt", "r")

coordinates = []
for line in input:
    coordinatePair = line.strip("\n").split(",")
    for i in range(0, len(coordinatePair)):
        coordinatePair[i] = int(coordinatePair[i])
    coordinates.append(coordinatePair)


## Do I draw out the outline and then fill? How do I fill correctly?
# can I do it with inequalities for lines? Are lines diagonal or only vertical and horizontal? Appears true
# if rectangle includes coordinate in vertical or horizontal range of the line must meet conditions of the inequality, inequality will be based on constant coordinate, range based on changing coordinate
# e.g. 7,1 + 11,1 if x coordinates include values between 7 and 11, y must be less than 1
# how do I know which way the inequality is with logic?
# use maximum and minimum values for each coordinate? There are edge cases that break that right? (wrap around cases, like walls/door around a single room)
# use max and min to determine initial direction of inequalities, then use values to determine if reversed or not.

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