n = input()

LUCKY_NUMS = [4, 7]
present_nums = []

for num in n:
    if num == "4" or num == "7":
        present_nums.append(num)

if len(present_nums) in LUCKY_NUMS:
    print("YES")
else:
    print("NO")