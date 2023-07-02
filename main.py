#Desafio 3: Crie um programa que receba uma frase do usuário e conte a quantidade de ocorrências de cada letra. Armazene os resultados em um dicionário e exiba-os.

frase = input('Digite um frase: ')

ocorrencias = {}

for letra in frase:
    if letra.isalpha():
        if letra in ocorrencias:
            ocorrencias[letra] += 1
        else:
            ocorrencias[letra] = 1

print('Ocorrências de cada letra: ')
for letra, quantidade in ocorrencias.items():
    print(letra, '-', quantidade)
