# Scratchpad
# Need to figure out how to parse one line at a time
# Then if 'contains' is how you check if a string is present 
# Also what is 'Expected ":"' ?? 


def bitland_x(lines):

    x = 0 

    lines = []

    # Reads the first line to read all following lines 
    len = int(input())

    for _ in range(len):
        # Since we already called input, we can just use it again to read the next line which is the 2th
        line = input()
        lines.append(line)

    for line in range(len):
    
        if line == "" or line == " " or line == "Nan":
            print("Skipping Line {line} because it is empty")
            continue

        if line  not contains(+) or not contains(-):
            print("Skipping line {line} because it does not contain '+' or '-'")
            continue

        if line =! str:
            print("Skipping line {line} because it is not a string")
            continue

        if line contains(+):
            x =+ 1
            return 
       
        # We assume the line has - if it made it through prior filters  
        x =- 1
        
    return x 
    

 
