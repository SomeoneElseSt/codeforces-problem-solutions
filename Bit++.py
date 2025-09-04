# Scratchpad
# Need to figure out how to parse one line at a time
# Then if 'contains' is how you check if a string is present 
# Also what is 'Expected ":"' ?? 


def bitland_x(lines):

    x = 0 

    # Get the lenght
    len = lines[1]

    # Start after N lines statement
    line = lines[-1]

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
    

 
