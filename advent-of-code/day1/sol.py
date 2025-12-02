# L = Left rotation 
# R = Right rotation 

# L -> 0 -> 99
# R -> 99 -> 0 

# Starting Pos: 50 

import re

# Read input.txt 
input = open("test.txt")

DIAL = 50
COUNTER = 0
 
# Iterate over each line 
for line in input:
    # Determine the direction extracting L/R with a regex
    if "L" in line:
        line_n = int(re.sub("L", "", line))

        if DIAL - line_n < 0: 
            DIAL -= (line_n - 100)

        elif DIAL - line_n > 0:
            DIAL -= line_n

        elif DIAL - line_n == 0:
            DIAL = 0
            COUNTER += 1


    elif "R" in line:
        line_n = int(re.sub("R", "", line))

        # The only way to go over is if the sum is > 99      
        if DIAL + line_n > 99:
            if (DIAL + line_n) - 100 == 0:
                DIAL = 0
                COUNTER += 1
            else:
                DIAL = (DIAL + line_n) - 100

    elif DIAL + line_n < 99:
        DIAL += line_n

print(COUNTER)

        



