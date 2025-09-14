# Input: 
# n = Number to substract from
# k = Times to substract from the number

# Processing
# If the last digit of the number is != 0, then n - 1
# If the last digit of the number == 0, then n[:-1] <- Trim the last digit 

# Implementation:
# Use a for loop over k that checks with an if last_digit is 0 cut by one, else - 1 until the loop is done

# Output: 
# n

n, k = map(int, input().split())

for i in range(k):
    if n % 10 == 0:
        n = n // 10
    else:
        n = n -1 

print(n)