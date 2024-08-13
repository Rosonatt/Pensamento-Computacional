provas = int(input("qual o numero de provas"))
notas = 0
for i in range (provas):
    notas += float(input(f"insira sua nota, {i+1}°:"))

    media = notas/provas
print(f'media:{media:.1f}')
if media >= 7:
        print(media,":aprovado")
else:
        print(media,":rerprovado")