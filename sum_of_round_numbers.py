# Inputs:
# n = the # of test cases
# k1, k2, k3, ... kn = each test case on a new line

# Processing
# First, make a set to know which are the K unique elements of the input and append this to the list 
# Second, make and append each new number into the results list considering we can take the N at the current position, and append it to it the # of chars 

n = int(input())

results = []

for test_case in range(n):
    current_t = list(set(map(int, str(input()))))

    for i in current_t:
        if len(current_t) > 2:
            results.append(len(current_t) - 1) # - 1 to exclude 0
            results.append(i + (len(current_t) - current_t.index(i)) *  0)
        else:
            results.append(1)
            results.append(i)

print("\n".join(map(str, results)))