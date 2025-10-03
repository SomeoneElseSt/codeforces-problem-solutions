n = int(input())

for rating in range(n):
    c_rating = int(input())

    if c_rating >= 1900:
        print("Division 1")

    elif c_rating >= 1600:
        print("Division 2")

    elif c_rating >= 1400:
        print("Division 3")

    elif c_rating <= 1399:
        print("Division 4")

