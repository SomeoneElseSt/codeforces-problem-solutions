# Sequence:
# a + 1 | a
# a + 2 | a
# a + 3 | a 
# a + 4 | a 
# a + 5 | a 
# a + n | a

# Processing
# We need to find the n that n is - 1 after being divided by 2 for even numbers and the n by 2 for odds 

# This works for 20000000 (even) (current_t // 2) - 1
# But not for anything else 
# This works for 381621773, 7, 1  (odd) current_t // 2
# This makes sense because when it's even it's -1 because we always need b to be at least 1 at some point, whilst with an odd number that's guaranteed 


n = int(input())

results = []

for test_case in range(n):

    current_t = int(input())
    
    if current_t % 2 == 0:
        result = (current_t // 2) - 1
    else:
        result = current_t // 2

    results.append(result)

print("\n".join(map(str, results)))