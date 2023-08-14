from bd import dados

print("-"*65)
print(" AS RSPOSTAS DEVEM INICIAR EM LETRA MAIUSCULA E CONTER ACENTOS")
print("-"*65)

c = 0
i = 0  

while c < 10:
    dado = dados[c]
    questao = dado['per']
    resposta = dado['res']
    ide = dado['id']

    res1 = input(questao + " ")

    if res1 == resposta:
        i += 1
    
    c += 1

print("Número de respostas corretas:", i)  
