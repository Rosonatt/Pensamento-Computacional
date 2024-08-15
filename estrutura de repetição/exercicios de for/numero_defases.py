# Solicita ao usuário o número de fases
num_fases = int(input("Digite o número de fases: "))

soma_ponderada = 0
soma_pesos = 0


for i in range(num_fases):
    peso = i + 1
    
    nota = float(input(f"Digite a nota da fase {i + 1}: "))
    
    soma_ponderada += nota * peso
    soma_pesos += peso


media_ponderada = soma_ponderada / soma_pesos

print(f"A média ponderada das notas é: {media_ponderada:.2f}")
