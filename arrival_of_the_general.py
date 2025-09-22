# Some notes: 
# Len gives the actual count, starting at 1. Same for any N that describes the amount of test cases or elements 
# Array indices start from 0, so valid indices are: 0, 1, 2, ..., (n-1)
# Distance to first position (index 0) = current_index (because the current index is the distance to the first position)
# Distance to last position (index n-1) = (n-1) - current_index (because the current index is the distance to the last position - 1 to account for the zero index)

n = int(input())
nums_list = list(map(int,input().split()))

max_val = max(nums_list)
max_i = nums_list.index(max_val)

min_val = min(nums_list)
min_i = len(nums_list) - 1 - nums_list[::-1].index(min_val)

min_distance = (n - 1) - min_i 

if n == 2:
    result = 1 if nums_list[0] < nums_list[1] else 0
elif max_i == 0 and min_i == n - 1:
    result = 0
elif max_i > min_i:
    result = (min_distance + max_i) - 1
else: 
    result = min_distance + max_i

print(result)