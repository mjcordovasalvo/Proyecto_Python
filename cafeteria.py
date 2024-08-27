precios={
    "cafe":1500,
    "te":1000,
    "jugo de naranja": 2000
    "pastel de chocolate": 2500
    "tarta de frutas":3000,
}

pedidos={
    "cafe":int(input("ingrese la cantidad del cafe:")),
    "te":int(input("ingrese la cantidad del te:")),
    "jugo de naranja":int(input("ingrese la cantidad del jugo natural:"))
    "pastel de chocolate": int(input("ingrese la cantidad del pastel de chocolate:"))
    "tarta de frutas"int(input("ingrese la cantidad de tarta:"))
}
total=0

for producto, cantidad in pedidos.items()
    total += cantidad * precios[producto]

print(total)

