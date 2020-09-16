def contar (valor=5, caractere='+'):
    for i in range(0,valor): #de 0 até valor que é =  5
        print(caractere) #caractere é igual a +
contar() # É a função que faz valor ser até 5 e caractere valer +
print('Passando um Caractere Diferente: ')
contar(caractere='Oba_Oba!') #Usando a função, porem troquei o valor de caractere
print('Passando um Valor Diferente')
contar(valor=5)

...
print('Passando valor e caractere diferente: ')
contar(6,'$')
