def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= 1 and num2 >= num3:
        return num2
    else:
        return num3

is_male = False
is_tall = False
if is_male and is_tall:
    print("eres hombre o alto")
elif is_male and not(is_tall):
    print("Eres un hombre petiso")
else:
    print("No eres hombre ni eres alto")

print(max_num(1,3,8))