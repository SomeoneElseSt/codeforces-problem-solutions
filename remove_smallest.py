n = int(input())

for i in range(n):
    c_len = int(input())
    c_test = list(map(int,input().split()))

    if len(c_test) == 1:
        print("YES")
        continue
    else:
        # Heuristic: if diff between 2 nums is > 1, it's a no
        # Set -> diff for i-th, i-th+1 > 1? No! else Yes!
        temp = sorted(set(c_test))

        if len(temp) == 1:
            print("YES")
            continue

        for j in range(0, len(temp) - 1):
            diff = abs(temp[j] - temp[j+1])
            if diff > 1:
                print("NO")
                break
        else: # if break != true
            print("YES")
    