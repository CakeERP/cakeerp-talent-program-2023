numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

meio = numero1 + numero2 + numero3 - maior - menor

print(f"Números em ordem decrescente: {maior}, {meio}, {menor}")