lista = [1, 2, 3, 4, 5]
lista[2] = int(input("Digite um numero: "))

del lista[-1]

print("tamanho da lista: ", len(lista))
print(lista)