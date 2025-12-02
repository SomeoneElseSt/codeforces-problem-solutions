# L = Left rotation 
# R = Right rotation 

# L -> 0 -> 99
# R -> 99 -> 0 

# Starting Pos: 50 

import re

# Read input.txt 
input = open("test.txt")

DIAL = 50
print(f"DIAL {DIAL}")
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

        # Went < 0
        if DIAL < 0:
            DIAl = 100 - DIAL
        
        if DIAL == 0:
            COUNTER += 1

    elif "R" in line:
        line_n = int(re.sub("R", "", line))
     
        if DIAL + line_n > 99:
            # ?
        elif DIAL + line_n < 99:
            DIAL += line_n

        # Went > 99 
        if DIAL > 99:
            DIAl = DIAL - 100 

        if DIAL == 0:
            COUNTER += 1

print(COUNTER)

        



