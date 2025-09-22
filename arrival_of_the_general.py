
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