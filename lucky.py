
n = int(input())

for i in range(n):
    c_test = list(map(int, input()))

    if sum(c_test[:3]) == sum(c_test[3:]):
        print("YES")
    else:
        print("NO")