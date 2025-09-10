n, k = map(int, input().split())

scores = list(map(int, input().split()))

new_participans = 0

for score in scores:
    if score >= k:
        new_participants += 1

print(new_participants)
