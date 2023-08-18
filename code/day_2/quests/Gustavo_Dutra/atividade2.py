idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa: "))
    altura = float(input(f"Digite a altura da pessoa: "))
    idades.append(idade)
    alturas.append(altura)

print("Idades e alturas na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Idade: {idades[i]} anos, Altura: {alturas[i]} ")
