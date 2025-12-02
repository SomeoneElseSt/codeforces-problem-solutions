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
    
    # For > 100 rotations they have to be broken up in < 99 chunks
    strpd_line = int(re.sub("[^0-9]", "", line))

    # Re-append < 99 chunks with R/L rotation marker 
    if strpd_line > 99:
        lines = []
        marker = "L" if "L" in line else "R"

        # Append chunks of 99 or a remainder to lines
        while strpd_line > 0:
            print(f"line {line} is being trimmed down")
            chunk = 99 if strpd_line > 99 else strpd_line
            strpd_line -= chunk
            lines.append(marker + str(chunk))
            print(f"current lines ls is {lines}")
       
    # Else leave the original line alone 
    else:
        lines = [line]

    for l in lines: 

        # Determine the direction extracting L/R with a regex
        if "L" in l:
            line_n = int(re.sub("L", "", l))
            print(f"current line {line_n}")

            if DIAL - line_n < 0: 
                DIAL -= (line_n - 100)
                print(f"current line was LEFT and < 0. DIAL {DIAL}\n")

            elif DIAL - line_n > 0:
                DIAL -= line_n
                print(f"current line was LEFT and > 0. DIAL {DIAL}\n")

            elif DIAL - line_n == 0:
                DIAL = 0
                COUNTER += 1
                print(f"current line was LEFT and == 0. DIAL {DIAL}\n")
            
        elif "R" in l:
            line_n = int(re.sub("R", "", l))
            print(f"current line {line_n}")

            # The only way to go over is if the sum is > 99      
            if DIAL + line_n > 99:
                if (DIAL + line_n) - 100 == 0:
                    DIAL = 0
                    COUNTER += 1
                    print(f"current line was RIGHT and == 0. DIAL {DIAL}\n")
                else:
                    DIAL = (DIAL + line_n) - 100
                    print(f"current line was RIGHT and > 99. DIAL {DIAL}\n")

            elif DIAL + line_n <= 99:
                DIAL += line_n
                print(f"current line was RIGHT and < 99. DIAL {DIAL}\n")

print()
print(f"counter {COUNTER}")
