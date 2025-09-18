# Input:
# n = 1 <= n <= 10^25

n = int(input())

# Sequence:
# - + - + - 

result = 0
switched = False

for i in range(n):

    if switched == False:
        result -= i
        switched = True
    elif switched == True:
        result += i
        switched = False

print(result)