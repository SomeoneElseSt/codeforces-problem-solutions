# Input:  
# n = N of nums
# i = a1, a2, a3 ... an | The nums

# Processing
# Make i into a list, use max and min to get the highest and lowest values
# If the first i value is already the max, leave as is, otherwise swap with i + 1 value
# If the last i value is already the min, leave as is, otherwise swap with i - 1 value 

# Output:
# 

n = int(input())
i = list(map(int,input().split()))

# Get the max value that's leftmost, by default max will pick the first element it finds going from left to right so this can be simple
max_val = max(i)
max_i = i.index(max_val)

# Get the min value that's rightmost. 
# To find the rightmost element we'll reverse the list and pick the first minimum value. Then, we can map the index of that value to the original list
min_val = min(i)
min_i = len(i) - 1 - i[::-1].index(min_val)

if n % 2 == 0:
    time = (max_i - len(i)) + (min_i - len(i))
else: 
    time = ((max_i - len(i)) + (min_i - len(i)) - 1)

print(time)
