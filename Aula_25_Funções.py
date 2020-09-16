# def <nome da função>(Argumentos):
#     <instruções>


#Ex:
'''def msn ():
    print('Tente de novo')

print(msn())'''

#Função com argumentos:
'''A = int(input('Digite Num: '))
B = int(input('Digite Num_2: '))
def soma (z,y):
   # return z+y #Define o que a função faz
    return z**y
R = soma(A,B)  # O produto da função tem que ir para uma Variavel antes de ser Printado
print(R)'''



valores=[1,2,3,4,5]
#valores_ = [3, 6, 9]
def quad(valores):
    quad = [] # Esta vazia pois vai receber os resultados.
    for x in valores:
        quad.append(x**2)
    return quad

results = quad(valores)

for y in results:
    print(y)
