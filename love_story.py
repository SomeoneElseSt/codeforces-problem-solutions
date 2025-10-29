n = int(input())

c = ['c', 'o', 'd', 'e', 'f', 'o', 'r', 'c', 'e', 's']

for i in range(n):
    c_test = list(input())
    temp = 0

    for j in range(len(c)):
        if c[j] != c_test[j]:
            temp += 1
    print(temp)
