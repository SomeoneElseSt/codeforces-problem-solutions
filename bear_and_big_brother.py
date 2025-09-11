a, b = input().split()

a = int(a)
b = int(b)

years_counter = 0

if a == b:
    print("1")
else: 
    while a <= b:
        years_counter += 1 
        a = a * 3
        b = b * 2
        print(years_counter)



