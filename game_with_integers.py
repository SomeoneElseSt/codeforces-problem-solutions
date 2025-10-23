# If n % 3 == 0 Vova will always keep it ± 1 off
# If ~ Vanya can ± 1 and win 

n = int(input())

for i in range(n):
    c_test = int(input())

    if c_test % 3 != 0:
        print("First")
    else:
        print("Second")
