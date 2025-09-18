# Input:
# n = 1 <= n <= 10^25

# Sequence:
# - + - + 

# Processing 
# We need to take the i-th element, and with the right operator modify it with the i-th + 1 element, keeping track of the result  

n = int(input())

result = 0
switched = False

for i in range(1, n + 1):

    if switched == False:
        result -= i
        switched = True
    elif switched == True:
        result += i
        switched = False

print(result)