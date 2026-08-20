palavra = input("Digite: ").upper()

for i in range(len(palavra)):
    if palavra[i] == "A" or palavra[i] == "E" or palavra[i] == "I" or palavra[i] == "O" or palavra[i] == "U":
        continue
    else: 
        print(palavra[i]) 