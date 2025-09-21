# Input:
# n = N of letters in word
# word = the word to check

# Processing:
# Check if all the elements in a list with all the English dictionary letters are in the list of the input word 

import string

n = int(input())
word = list(input().lower())

abc = list(string.ascii_lowercase)

pangram = "YES" if all(char in word for char in abc) else "NO"

print(pangram)
