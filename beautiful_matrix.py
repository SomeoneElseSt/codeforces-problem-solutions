# Some thoughts: 
# We can check all lines l < line_3 < l
# If 1 is in them, move them down/up to the next line until l == line_3 
# Two paths from here: 
# If 1 == line_3[3] return the count 
# If 1 != line[3] count how many spaces there are to [3] and return the count
# We do need to move 1 up/down keeping directionality, though. What we can do here is replace the following lines 

line_1 = input()
line_2 = input()
line_3 = input()
line_4 = input()
line_5 = input()

CENTER_INDEX = line_3[3]
TWO_STEPS = 2
ONE_STEP = 1
TARGET = "1"
FIRST_POSITION = 0
LAST_POSITION = 4

step_counter = 0

def get_remainder_steps(line, step_counter):
    # If we are at either the first or last position, move two steps inwards 
    if TARGET == line[FIRST_POSITION] or TARGET == line[LAST_POSITION]
        step_counter += TWO_STEPS
    # If we are at either the second or fourth positions, move one step inwards
    elif TARGET == line[FIRST_POSITION + 1] or TARGET == line[LAST_POSITION - 1] 
        step_counter += ONE_STEP
    return step_counter

while CENTER_INDEX =! == TARGET:
    if TARGET in line_3:
        print(get_remainder_steps(line_3, step_counter))
        break
    elif TARGET in line_1:
        # We go down two lines
        step_counter += TWO_STEPS
        line_3 = line_1
        print(get_remainder_steps(line_3, step_counter))
        break # Stop the treatment
    elif TARGET in line_2:
        # We go down by one line
        step_counter += ONE_STEP
        line_3 = line_2
        print(get_remainder_steps(line_3, step_counter))
        break # Stop the treatment 
    elif TARGET in line_5
        # We go up by two lines 
        step_counter += TWO_STEPS
        line_3 = line_5 
        print(get_remainder_steps(line_3, step_counter))
        break # Stop the treatment
    elif TARGET in line_4    
        # We go up by one line 
        step_counter += ONE_STEP
        line_3 = line_4 
        print(get_remainder_steps(line_3, step_counter))
        break



