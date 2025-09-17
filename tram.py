# Input:
# n = 1 to N number of train stops 
# a = some passangers
# b = some passangers 
# train = starts empty at 1 station

# Input Example:

# 4 <- Number of train stops
# 0 3 <- The N of people that exit, and the N of people that enter
# Min Capacity Counter = 3
# 2 5 <- The N of people that exit, and the N of people that enter 
# So, 3 - 2 = 1 + 5 = 6, since we substract the min capacity counter from the the passangers exiting and then add the entering passangers, if the result is < min_counter, we must update min_counter to the latest minmax
# 4 2
# So, 6 - 4 = 2 + 2 = 4 
# 4 0 
# So, 4 - 4 = 0 + 0 = 0 

# The relationship is, in iter 1, min_capacity_counter = current_line[1]
# Afterwards min_capacity_counter = (min_capacity_counter - current_line[0]) + current_line[1]

n = int(input())

first_station = list(map(int,input().split()))

min_counter = first_station[1]

# Iter to n - 1 because we already inputted the first line 
for station in range(n - 1):

    # This will iterate over N remaining input lines
    current_line = list(map(int,input().split()))

    min_calc = (min_counter - current_line[0]) + current_line[1]

    if min_calc > min_counter:
        min_counter = min_calc

print(min_counter)

