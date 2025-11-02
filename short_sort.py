n = int(input())

for t in range(n):
    c_t = list(input())

    if "".join(c_t) == 'abc':
        print("YES")    
        continue
    else:
        c_t_a = c_t.copy()
        c_t_b = c_t.copy()
        c_t_c = c_t.copy()
        t = False

        c_t_a[0], c_t_a[1] = c_t_a[1], c_t_a[0]
        c_t_b[1], c_t_b[2] = c_t_b[2], c_t_b[1]
        c_t_c[0], c_t_c[2] = c_t_c[2], c_t_c[0]

        if "".join(c_t_a) == 'abc' or "".join(c_t_b) == 'abc' or "".join(c_t_c) == 'abc':
            print("YES")
            t = True
            continue

    if not t:
        print("NO")
