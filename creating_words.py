n = int(input())

for w in range(n):
    c_w = list(input())
    c_w[0], c_w[4] = c_w[4], c_w[0]
    print("".join(c_w))
