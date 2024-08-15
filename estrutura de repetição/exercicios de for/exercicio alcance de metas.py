meta = 50
semestre_1 = [20, 50, 100,300, 2, 1]
semestre_2 = [12, 100, 3, 40, 49, 70]

alcance_de_meta = []
semestre_1.extend(semestre_2)
ano = semestre_1
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out','Nov', 'Dec']

       
for i, meses in enumerate(meses):
    if ano[i] >= meta:
        print(f'{meses} = {ano[i]}')
