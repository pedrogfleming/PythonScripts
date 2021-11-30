def realizar_operacion(num1,num2,operador):
    if operador == "+":
        return num1+num2
    elif operador == "-":
        return num1-num2
    elif operador == "/" and num2 != 0:
        return num1/num2
    elif operador == "*":
        return num1*num2
    else:
        return "Operacion invalida"


num1 = float(input("Ingrese primer numero: "))
op = input("Ingrese operador")
num2 = float(input("Ingrese segundo numero: "))
print(realizar_operacion(num1,num2,op))
