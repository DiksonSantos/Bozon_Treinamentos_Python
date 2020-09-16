'''def lista_itens(w, x, y , z):
    print(w,x,y,z)

lista = [21,22,67,69]

lista_itens(*lista)   #Caso não coloque o * antes , ele irá atribuir a lista somente ao primeiro Item ou o W, e vai dar Pau.
#... e cada um dos elementos da lista vai substituir uma das letras da Função DEF'''

#Empacotando Itens
def somar(*args):  #args\pode ser outro nome qualquer -> serve para lidar com um numero indefinido de argumentos\parametros
    soma = 0
    for i in range(0, len(args)):
        soma+= args[i] #Eles vão sendo acumulados na variavél soma.
        return soma

print(somar(1,2,3,4,5,6,7,8,9,10))
print(somar(77,23))
