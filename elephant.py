target_position = int(input())

starting_position = 0
steps_count = 0 

available_steps = [1, 2, 3, 4, 5]

if target_position in available_steps:
    print("1")
else: 
    while starting_position != target_position:
        steps_count += 1 
        starting_position += max(step for step in available_steps if step < starting_position - starting_position)

    print(steps_count)