# L = Left rotation 
# R = Right rotation 

# L -> 0 -> 99
# R -> 99 -> 0 

# Starting Pos: 50 

import re

# Read input.txt 
input = open("input.txt")

DIAL = 50
COUNTER = 0
 
# Iterate over each line 
for line in input:
    # Determine the direction extracting L/R with a regex
    if "L" in line:
        line_n = int(re.sub("L", "", line))

        # Go left line_n
        DIAL -= line_n

        # Went < 0
        if DIAL < 0:
            DIAl = 100 - DIAL
        
        if DIAL == 0:
            COUNTER += 1

    elif "R" in line:
        line_n = int(re.sub("R", "", line))

        # Go right line_n
        DIAL += line_n

        # Went > 99 
        if DIAL > 99:
            DIAl = DIAL - 100 

        if DIAL == 0:
            COUNTER += 1

print(COUNTER)

        



