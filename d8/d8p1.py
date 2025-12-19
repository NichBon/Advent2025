import time
import math
startTime = time.time()

#ingestion & processsing

input = open("input.txt", "r")

coordinatesList = []

for line in input:
    coordinates = line.strip("\n").split(",")
    for i in range(0, len(coordinates)):
        coordinates[i] = int(coordinates[i])
    coordinatesList.append(coordinates)

# pair distance calculation & sorting

pairDistances = []

for i in range(0, len(coordinatesList)):
    for j in range(i+1, len(coordinatesList)):
        pairDistances.append([i, j, math.sqrt((coordinatesList[i][0] - coordinatesList[j][0])**2 + (coordinatesList[i][1] - coordinatesList[j][1])**2 + (coordinatesList[i][2] - coordinatesList[j][2])**2)])

pairDistances.sort(key= lambda x: x[2])

# circuit forming

circuits = [[pairDistances[0][0], pairDistances[0][1]]]
pairIndex = 1
circuitsToConnect = 1000

#print(len(pairDistances), " pairs to check", pairDistances[0][0], pairDistances[0][1], " added at start")

while pairIndex < circuitsToConnect:
    containsFirst = -1
    containsSecond = -1
    pair = pairDistances[pairIndex]

    #check which circuit (if any) contains either or both breakers

    for i in range(0, len(circuits)):
        for junction in circuits[i]:
            if junction == pair[0]:
                containsFirst = i
            if junction == pair[1]:
                containsSecond = i
            if containsFirst >= 0 and containsSecond >= 0:
                break

    #print("checking: ", pair[0], pair[1], " current connections: ", connections)
    ## if both pairs already connected break       
    
    #if one inside a circuit append the junction to that circuit
    #if both are inside separate circuits join the two circuits
    #feels like there should be many ways to shortcut

    if not (containsFirst == containsSecond and containsFirst >= 0):

        if containsFirst == -1 and containsSecond == -1:
            circuits.append([pair[0], pair[1]])
            #print("added circuit ", circuits[-1])
        elif containsFirst != -1 and containsSecond != -1:
            #print("joined circuits ", circuits[containsFirst], circuits[containsSecond], "connections: ", connections+1)
            circuits[containsFirst] = circuits[containsFirst] + circuits[containsSecond]
            circuits = circuits[:containsSecond] + circuits[containsSecond+1:]
        elif containsFirst != -1:
            #print("added junction ", pair[1], " to circuit ", circuits[containsFirst], "connections: ", connections+1)
            circuits[containsFirst].append(pair[1])
        elif containsSecond != -1:
            #print("added junction ", pair[0], " to circuit ", circuits[containsSecond], "connections: ", connections+1)
            circuits[containsSecond].append(pair[0])

        #print("junctions ", pair[0], pair[1], "already connected")   
            
        
    pairIndex += 1

circuits.sort(key= lambda x: 1/len(x))

# for circuit in circuits:
#     print(circuit)

if len(circuits) >= 2:
    total = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    print(total)

print((time.time()-startTime)*1e3, "ms")