nota1 = float(input("Me fale a nota do primeiro bimestre:"))
nota2 = float(input("Me fale a nota do segundo bimestre:"))
nota3 = float(input("Me fale a nota do terçeiro bimestre:"))
nota4 = float(input("Me fale a nota do quarto bimestre:"))

total = nota1 + nota2 + nota3 + nota4

media = total/4

print(media)

if media >= 7.0 :
    print("aprovado")

elif media >= 5.0 and media <= 7.0 :
    print("recuperação")

else:
    print("reprovado")