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
        # print(f"current line {line_n}")


        if DIAL - line_n < 0: 
            DIAL -= (line_n - 100)
            # print(f"current line was LEFT and < 0. DIAL {DIAL}\n")

        elif DIAL - line_n > 0:
            DIAL -= line_n
            # print(f"current line was LEFT and > 0. DIAL {DIAL}\n")

        elif DIAL - line_n == 0:
            DIAL = 0
            COUNTER += 1
            # print(f"current line was LEFT and == 0. DIAL {DIAL}\n")
        
    elif "R" in line:
        line_n = int(re.sub("R", "", line))
        # print(f"current line {line_n}")

        # The only way to go over is if the sum is > 99      
        if DIAL + line_n > 99:
            if (DIAL + line_n) - 100 == 0:
                DIAL = 0
                COUNTER += 1
                # print(f"current line was RIGHT and == 0. DIAL {DIAL}\n")
            else:
                DIAL = (DIAL + line_n) - 100
                # print(f"current line was RIGHT and > 99. DIAL {DIAL}\n")

        elif DIAL + line_n < 99:
            DIAL += line_n
            # print(f"current line was RIGHT and < 99. DIAL {DIAL}\n")

print(f"counter {COUNTER}")
