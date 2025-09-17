n = int(input())

def check_unique(s):
    if isinstance(s, int):
        s = str(s)
    return len(set(s)) == len(s)

for year in range(n + 1, 10000, 1):
    if check_unique(year) == True:
        print(year)
        break


