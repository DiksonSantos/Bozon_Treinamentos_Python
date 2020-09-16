var = str(input('Digite algo: '))
for x in var:
    print(x) # Ele imprime uma letra por linha (da palavra que for digitada).

frutas = ('laranja', 'morango', 'guarana', 'açai')
for y in frutas:
    print('Fruta: %s' %y.title()) # Significa: %s trocar por %y (Com S significando STRING).
#Este print de cima exibe um item Por Linha. O de baixo mostra a tupla ou lista comforme ela foi digitada.
print(frutas)

'''for x in range(11):  #Imprime de 0 a 10
    print(x)
for w in range(0,51,5): # Imprime de 0 a 50 pulando de 5 em 5.
    print(w)'''
