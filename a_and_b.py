# https://codeforces.com/problemset/problem/2149/D

n = int(input())

RESULTS = []
for test in range(n):
    c_test_l = int(input())
    c_test = input()

    if c_test_l == 1 or c_test_l == 2:
        RESULTS.append(0)
        continue
    else:
        for j in c_test:
