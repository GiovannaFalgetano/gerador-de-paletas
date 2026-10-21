import random #Chama a ferramenta de sorteio

caracteres = "0123456789ABCDEF"
cor = "#"

for i in range(6):
    cor = cor + random.choice(caracteres) 

print(cor)