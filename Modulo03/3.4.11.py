beatles = []
print("Etapa 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

for i in range(2):
    beatles.append(input("Digite o nome dos outros integrantes: "))
print("Etapa 3:", beatles)

for i in range(2):
    del beatles[-1]
print("Etapa 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)

print("o fabuloso", len(beatles))