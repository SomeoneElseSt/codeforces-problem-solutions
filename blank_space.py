n = int(input())

for i in range(n):
    c_l_len = int(input())
    c_l = input().split()

    m_z = 0
    c_z = 0
    for j in range(c_l_len):
        if c_l[j] == "0":
            c_z += 1
            if c_z > m_z:
                m_z = c_z
        else:
            c_z = 0
    print(m_z)

