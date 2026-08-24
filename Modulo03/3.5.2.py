my_list = [] 
qnt = int(input("Digite o tamanho da lista: "))

for i in range(qnt):
    my_list.append(int(input(f"Digite o numero de posição {i}: ")))

swapped = True
 
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
 
