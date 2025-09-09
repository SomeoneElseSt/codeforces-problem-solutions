string_1 = input()
string_2 = input()

string_1_normalized = string_1.lower()
string_2_normalized = string_2.lower()

if string_1_normalized < string_2_normalized:
    print("-1")
elif string_1_normalized > string_2_normalized:
    print("1")
elif string_1_normalized == string_2_normalized:
    print("0")


