input = open("input.txt", "r")

dial = 50
output = 0

for line in input:
    rotation = int(line[1:])
    if line[0] == 'R':
        dialWorking = dial + rotation
    else: 
        dialWorking = dial - rotation

    # add 1 if crossing from positive to negative
    if dialWorking <= 0 and dial != 0:
        output += 1

    dial = dialWorking % 100  
    
    # make positive before adding floor division
    if dialWorking < 0:
        dialWorking = dialWorking*-1

    output += dialWorking // 100


print(output)