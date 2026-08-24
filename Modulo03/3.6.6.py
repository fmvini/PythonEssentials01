my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

temp = sorted(my_list)

unique = [temp[0]]

for i in range(1, len(temp)):
    if temp[i] != temp[i - 1]:
        unique.append(temp[i])

print("A lista com os elementos exclusivos aqui")
print(unique)   