n, k = map(int, input().split())

scores = list(map(int, input().split()))

new_participants = 0

k_th_score = scores[k - 1] 

if k_th_score == 0:
    for score in scores:
        if score > 0:
            new_participants += 1
else:
    for score in scores:
        if score >= k_th_score:
            new_participants += 1

print(new_participants)
