def somaImposto(taxaImposto, custo):
    custo_com_imposto = custo * (1 + taxaImposto / 100)
    return custo_com_imposto


taxa = float(input("Digite a taxa de imposto sobre vendas em porcentagem: "))
custo_item = float(input("Digite o custo do item antes do imposto: "))

custo_com_imposto = somaImposto(taxa, custo_item)
print(f"O custo do item com imposto é: R${custo_com_imposto:.2f}")
