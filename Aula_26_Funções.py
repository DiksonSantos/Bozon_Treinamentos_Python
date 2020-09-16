var_global = 'Dikson_Treinando Tecnologias'
def escreve_texto():
    global var_global
    var_global = 'Dikson' # se colocar um sinal de recebe (=) e adicionar um texto diferente do original aqui, este substitui o original.
    #https://blog.liveedu.tv/python-como-usar-variavel-global-numa-funcao/
    var_local= 'Texto de Testes Função'
    print('Variavel Global', var_global)
    print('Variavel Local', var_local)
print('Executando a Função Escreve texto')
print('Escreve Func Texto:')
escreve_texto()

'''print('\nTentando acessar as variaveis diretamente')
print('Variavel Global', var_global)'''

# A variavél Var_Global dentro da função DEF foi alterada\substituida
