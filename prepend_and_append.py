# run the two pointers inwards 
# remove the 1st/last elems when they match 0,1 or 1,0 (additions)
# then keep the len of the remaining string 
# and if the last and first are 1, 1  or 0, 0 then return c_len 

n = int(input())

for test in range(n):
    c_len = int(input())
    c_test = list(map(int,input()))

    temp = False
    while temp is not True:
        if len(c_test) == 0:
            print(0)
            break

        if c_test[0] == 0 and c_test[-1] == 1:
            c_test.pop(0)
            c_test.pop(-1)
        elif c_test[0] == 1 and c_test[-1] == 0:
            c_test.pop(0)
            c_test.pop(-1)
        else:
            temp = True
            print(len(c_test))
