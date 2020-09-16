'''D = {'b':2, 'a':1,'d':4,'c':3} #Dicionário Inicial
ordenada = list(D.keys()) #Lista Não Ordenada de Chaves -> 'ordenada' Recebeu Lista de Chaves D. O Metodo KEYS Significa Obter as Chaves do Dicionario(B,A,D,C Apenas).
ordenada.sort() #Lista de Chaves Ordenada -> 'Ordenada' Foi Organizada pelo Atributo '.SORT'
for key in ordenada: # Para Cada Chave Dentro da Lista (for 'Key' in ordenada, poderia se como For 'I' in Range
    print(key,'=',D[key]) #Iteração através das chaves ordenadas, retornando o valor mapeado em cada chave.
#D[key] -> Estes colchetes indicam que o que deve ser mostrado é o valor ( Neste casonumerico) de cada Chave.
# Keys -> Significa -> Retorne as Chaves do Dicionario (Neste Caso D).'''


''''#FUNÇÃO SORTED:
D = {'b':2, 'a':1,'d':4,'c':3}
for key in sorted(D):  #: key -> É Uma Variavel (Criada Aqui)
    print(key, '=',D[key]) #Fez a Mesma Coisa -> Ordenou do menor para o maior.'''

#Outro Codigo que fez a mesma coisa:
D = {'b':2, 'a':1,'d':4,'c':3}
for key in sorted(D):
    print(key, '=', D[key])
