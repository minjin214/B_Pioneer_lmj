word = input()
result = ''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in word:
    result += alphabet[alphabet.index(i)-3]
print(result)