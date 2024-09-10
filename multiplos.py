a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))

if a>b:
    if a%b==0:
        print(f"{a}es multiplo de {b}")
elif a<b:
    if b%a==0:
        print(f"{a} no es multiplo de {b}")