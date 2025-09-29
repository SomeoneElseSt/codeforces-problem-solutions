n = int(input())
results = []

for number in range(n):
    a, b, c = map(int, input().split())

    if a + b == c or b + c == a or a + c == b:
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(map(str, results)))




