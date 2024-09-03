def es_primo(n):
    for i in range(2,n):
        if n%i==0:
            print("no es primo")
            return False
        return True
    

es_primo=es_primo(7)
if es_primo:
    print("es primo")
else:
    print("no es primo")
