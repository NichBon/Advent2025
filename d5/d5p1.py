input = open("test.txt", "r")

#Initialise
idRanges = []
ingredientIds = []
freshIngredients = 0

#Massage input into arrays
line = input.readline()
while line != "\n":
    tempRange = line.strip('\n').split('-')
    for i in range(0, 2):
        tempRange[i] = int(tempRange[i])
    idRanges.append(tempRange)
    line = input.readline()

for line in input:
    ingredientIds.append(int(line.strip('\n')))

#iterate through fresh ids to find fresh ingredients
for id in ingredientIds:
    id = id
    for range in idRanges:
        if id >= range[0] and id <= range[1]:
            freshIngredients += 1
            break
    
print(freshIngredients)