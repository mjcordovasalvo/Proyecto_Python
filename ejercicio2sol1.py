#Solicitar ingresar valores al usuario
precio= int(input("Ingrese el precio del producto: $"))
pago=int(input("ingrese con cuanto paga: $"))

#calculos del vuelto
vuelto= (pago-precio)

#billetes de 1000
billetesmil= int(vuelto/1000)

#calculando el sobrante de los billetes de 1000
sobrante= vuelto%1000

#monedas 
monedas=int(sobrante/500)

print(f"su vuelto es {vuelto} con {billetesmil} billetes de $1000 y {monedas} monedas de $500")




