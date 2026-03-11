print('Primeiro Projeto em Python', 'Primeira aula', sep='-') ##separador

print('-------------------------------------')

print('Primeiro Projeto em Python', 'Primeira aula', sep='-', end='***') ##finalizador

print('-------------------------------------')


print('Olá', 'Primeira aula', sep='-') 

print('-------------------------------------')



#Formatação
print('772', '558', '333', sep='.', end='-')
print(20)

print('-------------------------------------')


#Outras formas de impressão
print("texto'texto entre aspas simples'")
print('-------------------------------------')
print('texto"texto entre aspas duplas"')
print('-------------------------------------')


#Laço de repetição
nomes = ['Julia', 'Lara', 'Luiza']
for nome in nomes:
    print(nome)
print('-------------------------------------')

#for/else
nomes = ['Julia', 'Lara', 'Luiza']
for nome in nomes:
    print(nome)
else:
    print("Todos os nomes foram listados")
print('-------------------------------------')

#For de string
palavra = "Vamos estudar"
for letra in palavra:
    print(letra)
print('-------------------------------------')

#For listando Vetor
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Ceilandia'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])
print('-------------------------------------')

#for com continue
pessoas = [({'nome': 'João', 'cidade': 'Ceilandia'}),
           ({'nome': 'Maria', 'cidade': 'Taguatinga'}),
           ({'nome': 'Pebinha', 'cidade': 'Ceilandia'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])
print('-------------------------------------')

#For com range que retorna o valor do contador o conteudo
for numero in range(10):
    if numero % 2 == 0:
        print("O número", numero, "é par") 
print('-------------------------------------')

#For com enumerete
for i, j in enumerate(range(10, 1, - 1)):
    print(i, j)
print('-------------------------------------')

#For alinhad
for numero_coluna1 in range(2, 5):
    print("Tabuada do ", numero_coluna1)
    for numero_coluna2 in range(11):
        print(numero_coluna1, "x", numero_coluna2, " = ", numero_coluna1 * numero_coluna2)
print('-------------------------------------')
