# Make a set of the elements
# Get the index of the spy
# The spy is whichever's count 1 

n = int(input())

for i in range(n):
    c_test_l = int(input())
    c_test = list(input().split())

    # If the first element isn't equal to the 1st, 2nd, it's the spy
    if c_test[0] != c_test[1] and c_test[0] != c_test[2]:
        print(1)
        continue
    # If the second element isn't equal to the 1st, 2nd, it's the spy
    elif c_test[1] != c_test[0] and c_test[1] != c_test[2]:
        print(2)
        continue
    # Otherwise it's true the first element is not a spy and can be used for comparison
    else:
        n_spy = c_test[0]
        for i in range(2, len(c_test)):
            if c_test[i] != n_spy:
                print(i + 1)
                break