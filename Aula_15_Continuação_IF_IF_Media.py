nota1 = float(input("Digite Sua Nota"))
Nota2 = float(input("Digite_Segunda_Nota"))
media = (nota1 + Nota2) / 2

if media >= 7.00:
    print("Você Foi AProvado Parabéns!!")
else:
    if media >= 5.00 and media== 6.00:
        print("Aluno Em Recuperação")
    else:
        print("O Aluno Esta Reprovado...")
        print("Estude Mais!")
print("A Média é{:.2f}".format(media)) #Esta linha Eu incrementei, no comentário logo a baixo esta a original.
#print"A Média é %f " % media) -> Mas desta forma estava mostrando a média com um monte de casas decimais.
