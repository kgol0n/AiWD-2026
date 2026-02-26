sales = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}
lista_prod = []
for key, value in sales.items():
    if value > 8 :
        lista_prod.append(key)

print(lista_prod)