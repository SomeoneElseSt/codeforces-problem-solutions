# Input: 
# letter_set = {a, b, c} set of letters

# Processing
# Run a parser to clean out the brackets and commas, make a, b, c into a list -> set 

import re 

# sub([matches to replace], "what to replace them with", "for what string/var")
input_set = set(re.sub("[{}, ]" , "", input()))

print(len(input_set))
