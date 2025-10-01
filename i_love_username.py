# Input:
# n = number of contests
# perf = list, the numeric result of each contest

# Processing: 
# Take the first element of perf as both the minimum and maximum 
# Iterate over the list, and if we find something less than the first element, it's the new min, if it's higher, its the new max. Add to the counter if this happens  

n = int(input())
perf = list(map(int,input().split()))
counter = 0

min_c = perf[0]
max_c = perf[0]
perf.pop(0)

for c in perf:
    if c < min_c:
        min_c = c
        counter += 1
    elif c > max_c:
        max_c = c
        counter += 1

print(counter)
