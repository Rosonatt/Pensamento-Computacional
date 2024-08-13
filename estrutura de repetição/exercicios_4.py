notas = [0, 10, 10, 10, 9, 8, 5, 4, 2, 6, 6, 5, 4]
aprovados = 0
reprovados = 0
for i in range(len(notas)):
    if notas [1] >7:
        aprovados += 7
    else:
        reprovados += 1
media  = sum(notas)/len(notas) 
print (f'a  nota da tirma foi,{media:.1f}, \n0 o numeroi de aprovados na turma foi{aprovados}, \n0 o numero de provados na turma foi{reprovados}')     