n = int(input())
stones = list(input().strip())

left_index = 0
right_index = 1

rocks_counter = 0

while right_index < len(stones):
    if stones[left_index] == stones[right_index]:
        rocks_counter += 1
        stones.pop(right_index)
    else:
        right_index += 1
        left_index += 1

print(rocks_counter)
