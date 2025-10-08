# Two pairs of numbers, a, b
# How many times can you -= a, b before
# A == 0 and A != 0 or B == 0 and A != 0
# Then, if the resulting A, B > 1
# return times from above + resulting A, B - 1

a, b = map(int, input().split())
T_COUNTER = 0
I_COUNTER = 0

while a > 0 or b > 0:
    if a == 0:
        if b == 1:
            break
        b -= 2
        I_COUNTER += 1
    elif b == 0:
        if a == 1:
            break
        a -= 2
        I_COUNTER += 1
    else:
        a -= 1
        b -= 1
        T_COUNTER += 1

print(T_COUNTER, I_COUNTER)
