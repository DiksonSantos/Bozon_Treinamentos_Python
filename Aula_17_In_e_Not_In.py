#Esta é a aula 18 !!!
'''# Exemplo que eu fiz, funcionou como eu queria:
fruta = str(input("Digite o Nome Da Fruta: "))
L=["Laranja","maçã","abacate","uva"]
for i in range(len(L)):
    if fruta == L[i]:
     print("Fruta",fruta,"Encontrada")
if fruta != L[i]:
     print("Fruta Em Falta")'''
#______________________________________
#Incrementei o INPUT e o mecanismo de busca FUNCIONOU ^^ :
lang = str(input("Digite Linguagem: "))
lista = ["Python", "Ruby", "Java", "C"]
for x in range(len(lista)):
 if lang not in lista:
    print("Não Encontrada")
if lang in lista:
    print("Cadastrada")
