input = open("input.txt", "r")

dial = 50
output = 0

for line in input:
    rotation = int(line[1:])
    if line[0] == 'R':
        dial = (dial + rotation) % 100
    else: 
        dial = (dial - rotation) % 100
    if dial == 0:
        output += 1

print(output)



