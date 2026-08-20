palavra = input("Digite: ").upper()

word_without_vowels = []

for i in range(len(palavra)):
    if palavra[i] in "AEIOU":
        continue
    else:
        word_without_vowels.append(palavra[i])

for i in range(len(word_without_vowels)):
    print(word_without_vowels[i], end="")