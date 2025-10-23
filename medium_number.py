n = int(input())

for i in range(n):
    c_test = list(map(int,input().split()))
    s = sorted(c_test)
    print(s[1])
