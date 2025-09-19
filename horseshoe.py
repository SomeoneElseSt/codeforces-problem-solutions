ints = list(map(int, input().split()))

# Set de-dubs
unique_ints = set(ints) 

# The difference between the dedubbed list and the original is the amount of items that are duplicated
print(len(ints) - len(unique_ints))