# Input: 
# n = amount of money to withdraw
# consts = 1, 5, 10, 20, 100, the possible values in which money can be withdrawn

# Processing: 
# Use a while loop that adds the highest fitting bill into a bill counter until the current const won't fit anymore into the original N 

n = int(input())

consts = [100, 20, 10, 5, 1]

counter = 0

while n > 0:
    for bill in consts:
        if bill <= n:
            counter += 1 
            n -= bill
            break

print(counter)
