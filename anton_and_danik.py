n = int(input())
s = input()

anton_counter = 0
danik_counter = 0

for char in s:
    if char == "A":
        anton_counter += 1
    else:
        danik_counter += 1

if anton_counter == danik_counter:
    print("Friendship")
elif anton_counter < danik_counter:
    print("Danik")
else:
    print("Anton")



