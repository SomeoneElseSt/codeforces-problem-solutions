# Input: 
# n = The number of rooms
# p, q = The number of people who live in room, the room's capacity 

# Processing: 
# Whenever the difference in p - q is >= 2, add to a counter

n = int(input())

room_counter = 0

for room in range(n):

    room1, room2 = map(int, input().split())

    if room2 - room1 >= 2:
        room_counter += 1

print(room_counter)

