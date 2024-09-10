n=(int(input("ingrese un numero entero")))

for i in range (2,n):
    if n%i == 0:
        print(f"{i} no es primo")

    else:
        print(f"{i} es primo")