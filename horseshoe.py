ints = list(map(int, input().split()))

unique_ints = set(ints) 

print(len(ints) - len(unique_ints))