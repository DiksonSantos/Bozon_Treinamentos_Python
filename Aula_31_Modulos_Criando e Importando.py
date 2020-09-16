# Modulo com funções variadas

#Função que exibe mensagem de boas vindas:
def mensagem ():
	print('Ralando pra sair dessa vida!\n')

# Função para calculo de fatorial de um numero:

def fatorial(numero):
	if numero < 0:
		return 'Digite um valor maior ou igual a Zero'
	else:
		if numero ==0 or numero ==1:
			return 
		else:
			return numero * fatorial(numero =1)

# Função para Retornar uma série Sequencia de Fibonacci até um valor X :
def fibo(n):
	resultado = [0]
	a, b= 0, 1
	while b < n:
		resultado.append(b)
		a, b = b, a+b
	return resultado

#Modulo Principal
#import modfunções    # Este Bózon não explicou como declarar QUEM é o MODFUNÇÕES !!

modfunções.mensagem()

numero = int(input('Digite Um Numero Inteiro:'))
print('Calculando o Fatorial do Número: ')
fat = modfunções.fatorial(numero)
print('O Fatorial é: ',fat)
print('Calculando a Sequencia de Fibonacci: ')
fib = modfunções.fibo(numero)
print('O Fibonacci é: ', fib)
