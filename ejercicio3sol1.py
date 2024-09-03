#solicitar ingreso de la medida del lado del cuadrado al usuario
lado=float(input("ingrese el lado de las figura: "))

#calcular el area del cuadrado 
area_cuadrado=lado**2

#calcular el area de un triangulo equilatero
area_triangulo=((3**(0.5))/4) * (lado**2)

#calcular el area de un pentagono regular
area_pent=(lado**2*(25+10*5**(0.5))**(0.5))/4

#mostrar resultado
print(f"el area del cuadrado es: {area_cuadrado:.2f}")
print(f"el area del triangulo es: {area_triangulo:.2f}")
print(f"el area del pentagono es: {area_pent:.2f}")