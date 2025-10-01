
n = int(input())

temp = []
for test in range(n):
    c_test = input().lower()

    # Normalize c_test to compare against yes
    if c_test == "yes":
        temp.append("YES")
    else:
        temp.append("NO")

print("\n".join(map(str, temp)))
