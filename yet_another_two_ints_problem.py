# Match left-wise the last integers of a to be the same as the current b, once done with the current index, move onto N indexes left 

n = int(input())

AVAIL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(n):
    COUNTER = 0
    BASE, TARGET = map(int, input().split())

    if BASE == TARGET:
        print("0")
        continue

    for i in AVAIL:
        test = BASE + i if BASE < TARGET else BASE - i 

        if int(repr(test)[-1]) == int(repr(TARGET)[-1]):
            BASE = test
            COUNTER += 1
            break
    
    while BASE != TARGET:
        BASE = BASE + max(AVAIL) if BASE < TARGET else BASE - max(AVAIL)
        COUNTER += 1        
     
    print(COUNTER)
