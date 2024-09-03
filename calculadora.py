operacion = input("Qué operación deseas hacer (+, *, /, -): ")
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un segundo número: "))

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/': 
    resultado = float(num1) / num2
else:
    print("No colocaste una operación válida, asegúrate de elegir una operación.")

print(f"El resultado de {num1} {operacion} {num2} es: {resultado}");

