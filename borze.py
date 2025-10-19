# . = 0
# -. = 1
# -- = 2

message = input()

# Replace longer strings first and pass the result 
decoded_message = message.replace('--', '2').replace('-.', '1').replace('.', '0')

print(decoded_message)
