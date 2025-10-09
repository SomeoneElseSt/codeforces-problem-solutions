n = int(input())

for test in range(n):
    c_test = list(map(int,input().split()))
    a = c_test[0]
    c_test.sort()

    print(len(c_test) - c_test.index(a) - 1) 
