# At each turn, check if either C[0] or C[-1] is greater and at add it to the player at that turn

n = int(input())
cards = list(map(int,input().split()))

C_1 = 0
C_2 = 0
SWAP = True

for turn in range(n):
    if cards[0] >= cards[-1]:
        c = cards.pop(0)
    else:
        c = cards.pop(-1)

    if SWAP:
        C_1 += c
        SWAP = False
    elif not SWAP:
        C_2 += c
        SWAP = True

print(C_1, C_2)
