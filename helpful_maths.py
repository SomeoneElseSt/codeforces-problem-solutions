nums = input()

count_1 = []
count_2 = []
count_3 = []

for str in nums:

    if str == "1": 
        count_1.append("1")
    elif str == "2": 
        count_2.append("2")
    elif str == "3": 
        count_3.append("3")

delimiter = "+"

ordered_nums = delimiter.join(count_1 + count_2 + count_3)

print(ordered_nums)