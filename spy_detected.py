# Make a set of the elements
# The spy is whichever's count 1 
# Get the index of the spy

n = int(input())

for i in range(n):
    c_test_l = int(input())
    c_test = list(input().split())
    a, b = set(c_test)

    if c_test.count(a) == 1:
        print(c_test.index(a) + 1)
    else:
        print(c_test.index(b) + 1)