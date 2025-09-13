word = input()

lowers_counter = 0
uppers_counter = 0

for char in word:
    if char == char.upper():
        uppers_counter += 1
    else:
        lowers_counter += 1

if uppers_counter == lowers_counter:    
    print(word.lower())
elif uppers_counter > lowers_counter:
    print(word.upper())
else:
    print(word.lower())


