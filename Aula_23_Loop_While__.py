'''contador = 0
while contador < 1024:
    print('O Valor do Contador é %d' %contador)
    contador+=1
print('Loop Encerrado')'''

''''#Menu de Banco:
controle=''
while (controle!='s'):
    print('Digite A - Pagar')
    print('Digite B Para Receber')
    print('C Para Consultar')
    print('Digite S - Para Sair')
    controle= input('Digite A Opção Desejada: ')
print('Processo Encerrado! ')'''

# Decrementando e Usando o BREAK :
var = 20
while(var>0):
    print('O Valor de VAR é %d' %var)
    var-=1
    if(var==11):
        break
print('Loop Interrompido em valor 11')
