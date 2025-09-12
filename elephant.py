target_position = int(input())

starting_position = 0
steps_count = 0 

AVAILABLE_STEPS = [1, 2, 3, 4, 5]

if target_position in AVAILABLE_STEPS:
    print("1")
else: 
    while starting_position != target_position:
        steps_count += 1 
        starting_position += max(step for step in AVAILABLE_STEPS if step <= target_position - starting_position)

    print(steps_count)