# In chunks of 4, delete the third element 

n = int(input())

for i in range(n):
    c_t = list(input())

    result = [c_t[0], c_t[1]]
    for j in range(3, len(c_t), 2):
        result.append(c_t[j])
    
    print("".join(result))
