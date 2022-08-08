# Objetivo: fazer uma cifra de césar

# passo 1 - entrada de dados (palavra para criptografar/decriptar | opção de criptografar/decriptar) | opção de escolha da chave
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
palavra = input('Digite uma palavra: ').lower()
chave = int(input('Informe o tamanho da chave: '))
print('Você quer criptografar ou decriptar?')
opcao = input('Digite [C] - criptografar [D] - decriptar: ').upper()
while opcao not in 'CD':
    print('Opção inválida!')
    opcao = input('Digite [C] - criptografar [D] - decriptar: ').upper()

num = len(alfabeto)
cifrada = ''
# passo 2 - criptografia/decriptografia em sí
for letra in palavra:
    indice = alfabeto.find(letra)
    if indice == -1:
        cifrada += letra
    else:
        if opcao == 'C':
            indice = indice + chave
        elif opcao == 'D':
            indice = indice - chave

        indice = indice % num
        cifrada += alfabeto[indice:indice+1]
# passo 3 - saída de dados (palavra ínicial | palavra criptografada/decriptada)
print(f'O texto ínicial é: {palavra}')

if opcao == 'C':
    print(f'O texto criptografado é: {cifrada}')
elif opcao == 'D':
    print(f'O texto decriptado é: {cifrada}')
