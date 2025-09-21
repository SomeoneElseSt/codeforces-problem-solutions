# Input:
# N = amount of test cases
# n1,n2, n3,n... = all the test cases

# Processing
# We will need to find the difference between the divisor and the current remainder of a % b to know how many more times would we have to increase b to fully fit into a 

n = int(input())

results = []

for pair in range(n):
    a, b = map(int, input().split())
    
    if a % b == 0:
        results.append(0)
    else:
        results.append(b  - (a % b))

print("\n".join(map(str, results)))
        




     