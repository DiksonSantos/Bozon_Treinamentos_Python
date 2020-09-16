'''import random
print('Gerando Numeros entre 1 e 50')
for i in range(1,6): #posições 1 até 5
    n = random.randint(1, 50) #Randomizando 50 numeros
    print('Numero Gerado: ', n) #Exibindo os numeros randomizados'''

'''import random
print('Cinco Numeros de Ponto Flutuante: ')
for i in range(1,6):
    n = random.uniform(1,100) #Aleatorios de ponto flutuante
    print('Numero Gerado: ', n) #Caso não usasse o .uniform na função random, poderia usar aqui o 'n*11'''''


import random
L = [2,4,6,8,10,12,14,16,18,20]
print('Numeros da Lista:\n ')
print('Sequencia Original:\n')
print(L)

#n= random.sample(L,4) # .choice -> pega só um numero.   O (L, 4 Itens da Lista)
n= random.shuffle(L) #Embaralha a Lista
print('Sequencia Embaralhada: \n')
print(L)
print('Numero Gerado: ', n)
