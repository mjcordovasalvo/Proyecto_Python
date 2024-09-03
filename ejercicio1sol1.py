#Solicitar ingresar valores al usuario
precio= int(input("Ingrese el precio: $"))
pago=int(input("ingrese con cuanto paga: $"))

#calculo del vuelto
vuelto= (pago-precio)

#Resultado
print(f"Su vuelto es: {vuelto}")