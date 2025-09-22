# Input:  
# n = N of nums
# i = a1, a2, a3 ... an | The nums

# Processing
# Make i into a list, use max and min to get the highest and lowest values
# If the first i value is already the max, leave as is, otherwise swap with i + 1 value
# If the last i value is already the min, leave as is, otherwise swap with i - 1 value 

n = int(input())
i = list(map(int,input().split()))

max_val = max(i)
max_i = i.index(max_val)

min_val = min(i)
min_i = len(i) - 1 - i[::-1].index(min_val)

min_distance = n - min_i

if n == 2:
    result = 1 if i[0] < i[1] else 0
elif max_i == 0 and (min_i - 1) == n - 1:
    result = 0
elif max_i > min_i:
    result = (min_distance + max_i if n % 2 == 0 else min_distance + max_i - 1) - 1
else: 
    result = min_distance + max_i if n % 2 == 0 else min_distance + max_i - 1

print(result)