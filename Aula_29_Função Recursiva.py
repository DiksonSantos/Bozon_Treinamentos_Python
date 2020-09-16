'''numero = int(input('Digite um numero Para Fatorar'))
soma = numero-1*numero
if numero == 0:
    print('Final',numero)'''

'''def fatorial(numero):
    if numero == 0 or numero ==1:
        return 1
    else:
        return numero * fatorial(numero -1)
x = int(input('Digite Numero: '))
res = fatorial(x)
print('O Fatorial de %d é %d' % (x,res)) #Formato parecido com o format substitui o %d pelos valores dentro dos ()

breakpoint()'''

def fibonacci (num):
    if num<=1:
        return  num
    else:
        return fibonacci(num -1) + fibonacci(num -2)
x = int(input('Digite Um Numero Para Seq Fibonacci: '))
res = fibonacci(x-1)
print('O Valor do º%d Fibonacci é %d '  % (x,res))
