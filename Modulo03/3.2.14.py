blocos = int(input())

altura = 0
necessarios_camada = 1

while blocos >= necessarios_camada:
    blocos -= necessarios_camada
    altura += 1
    necessarios_camada += 1

print("A altura da pirâmide:", altura)