SCALE_FACTOR_LIMAK = 3 
SCALE_FACTOR_VIVEK = 2

def find_scale_factor_difference(a: int, b: int, scale_factor_a: int, scale_factor_b: int, ascending_order: bool):
    
    difference = 0

    if not isinstance(a, int) or not isinstance(b, int):
        print(f"Number input {a} {b} is not an integer and can not be processed")

    if not isinstance(scale_factor_a, int) or not isinstance(scale_factor_b, int):
        print(f"Scale factor input {scale_factor_a} {scale_factor_b} is not an integer and can not be processed")

    while a <= b if ascending_order else a >= b:
        difference += 1
        a = a * scale_factor_a
        b = b * scale_factor_b

    return difference

a, b = input().split()

a = int(a)
b = int(b)

if a == b:
    print("1")
else: 
    print(find_scale_factor_difference(a, b, SCALE_FACTOR_LIMAK, SCALE_FACTOR_VIVEK, True))