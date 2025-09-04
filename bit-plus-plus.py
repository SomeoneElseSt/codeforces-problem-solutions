# Scratchpad
# Need to figure out how to parse one line at a time
# Then if 'contains' is how you check if a string is present 
# Also what is 'Expected ":"' ?? 


def bitland_x():

    x = 0

    lines = []

    # Reads the first line to read all following lines
    lines_lenght = int(input())

    for _ in range(lines_lenght):
        # Since we already called input, we can just use it again to read the next line which is the 2th
        line = input()
        lines.append(line)

    for line in lines:

        if line is None or line == " " or line == "Nan":
            print("Skipping Line {line} because it is empty")
            continue

        if "+" not in line and "-" not in line:
            print("Skipping line {line} because it does not contain '+' or '-' Bit++ operators")
            continue

        if "+" in line:
            x += 1
        elif "-" in line:
            x -= 1

    return x 
 
