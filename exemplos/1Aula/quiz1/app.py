from bd import dados

print("-"*65)
print("             DIGITE APENAS A ALTERNATIVA CORRETA")
print("-"*65)

c = 0
i = 0  

while c < 10:
    dado = dados[c]
    questao = dado['per']
    resposta = dado['res']
   
    res1 = input(questao + " ")

    res1.lower()

    if res1 == resposta:
        i += 1
    
    c += 1

print(f'Você acertou {i}/{c}')  
