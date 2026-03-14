import random

#autoexplicativo
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#tamanho de tudo
tamanho = int(input("Digite o comprimento da senha: "))

#autoexplicativo
senha = ""

#Loop
for i in range(tamanho):
    senha += random.choice(caracteres)


# A senha ta aq
print("Senha gerada:", senha)





















