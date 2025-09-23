key = int(input())
n = int(input())
decrypt = []

for i in range(n):
    cuurent_letter = input()
    letter_decryption = ord(cuurent_letter) + key
    letter = chr(letter_decryption)
    decrypt.append(letter)

for i in decrypt:
    print(i, end="")
