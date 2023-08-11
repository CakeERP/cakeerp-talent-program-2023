def funcao_calcular_soma(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Chamando a função e exibindo o resultado
resultado = funcao_calcular_soma(valor1, valor2, valor3)
print(f"A soma dos três valores é: {resultado}")
