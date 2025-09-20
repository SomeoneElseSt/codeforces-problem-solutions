# Input:
# n = the number of layers of feelings

n = int(input())

r = [0] * int(n)

for f in range(n + 1):
    if f % 2 != 0:
        r[f - 1] = "I hate that" if f is not n else "I hate it"
    else:
        r[f - 1] = "I love that" if f is not n else "I love it"

print(" ".join(map(str, r)))
        
