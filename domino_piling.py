m, n = map(int, input().split())

domino_area = m * n
domino_size = 2

if domino_area % 2 == 0:
    print(domino_area // domino_size) 
else:
    print((domino_area - 1) // domino_size)
    