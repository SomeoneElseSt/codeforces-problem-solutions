line_1 = input()
line_2 = input()
line_3 = input()
line_4 = input()
line_5 = input()

TWO_STEPS = 2
ONE_STEP = 1
TARGET = "1"
FIRST_POSITION = 0
LAST_POSITION = 4

step_counter = 0

def get_remainder_steps_at_third_line(line, step_counter):
    line = line.split()
    if TARGET == line[FIRST_POSITION] or TARGET == line[LAST_POSITION]:
        step_counter += TWO_STEPS
    elif TARGET == line[FIRST_POSITION + 1] or TARGET == line[LAST_POSITION - 1]:
        step_counter += ONE_STEP
    return step_counter

if TARGET in line_3:
    print(get_remainder_steps_at_third_line(line_3, step_counter))
elif TARGET in line_1:
    step_counter += TWO_STEPS
    line_3 = line_1
    print(get_remainder_steps_at_third_line(line_3, step_counter))
elif TARGET in line_2:
    step_counter += ONE_STEP
    line_3 = line_2
    print(get_remainder_steps_at_third_line(line_3, step_counter))
elif TARGET in line_4:
    step_counter += ONE_STEP
    line_3 = line_4 
    print(get_remainder_steps_at_third_line(line_3, step_counter))
elif TARGET in line_5:
    step_counter += TWO_STEPS
    line_3 = line_5 
    print(get_remainder_steps_at_third_line(line_3, step_counter))
