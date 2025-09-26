# Inputs:
# n = the # of test cases
# k1, k2, k3, ... kn = each test case on a new line

# Processing
# First, make a set to know which are the K unique elements of the input and append this to the list 
# Second, make and append each new number into the results list considering we can take the N at the current position, and append it to it the # of chars 

n = int(input())

results = []

for test_case in range(n):
    current_t = int(input())
    list_t = list(map(int, str(current_t)))
    builder = []

    counter = 0
    for i in range(0, len(list_t)):
        if list_t[i] != 0:
            builder.append(str(list_t[i]) + "0" * (len(list_t) - i - 1))
            counter += 1
    delimiter = " "
    results.append(counter)
    results.append(delimiter.join(builder))

print("\n".join(map(str, results)))