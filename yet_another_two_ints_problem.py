# Match left-wise the last integers of a to be the same as the current b, once done with the current index, move onto N indexes left 

from typing import Counter


n = int(input())

AVAIL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
COUNTER = 0

for i in range(n):
    BASE, TARGET = map(int, input().split())

    print(f"debug: {BASE}, {TARGET}")

    # Base case
    if BASE == TARGET:
        print("0")
        
    # Addition
    elif BASE < TARGET:
        print("debug: base < target true")
        for i in AVAIL:
            test = BASE + i
            print(f"debug: current test {BASE + i}")
            if int(repr(test)[-1]) == int(repr(TARGET)[-1]):
                print(f"debug: last elements true at {test}")
                BASE += i
                print(f"debug: new base {BASE}")
                COUNTER += 1
                break

        while BASE != TARGET:
            BASE += max(AVAIL)
            COUNTER += 1
    
    # Substraction
    elif BASE > TARGET:
        for i in AVAIL:
            test = BASE - i
            print(f"debug: current test {BASE - i}")
            if int(repr(test)[-1]) == int(repr(TARGET)[-1]):
                print(f"debug: last elements true at {test}")
                BASE -= i
                print(f"debug: new base {BASE}")
                COUNTER += 1
                break

        while BASE != TARGET:
            BASE -= max(AVAIL)
            COUNTER += 1

print(COUNTER)
