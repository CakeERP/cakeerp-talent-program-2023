respostas = []
respostas.append(input("Telefonou para a vítima? (sim ou não): ").lower())
respostas.append(input("Esteve no local do crime? (sim ou não): ").lower())
respostas.append(input("Mora perto da vítima? (sim ou não): ").lower())
respostas.append(input("Devia para a vítima? (sim ou não): ").lower())
respostas.append(input("Já trabalhou com a vítima? (sim ou não): ").lower())

respostas_positivas = respostas.count("sim")

if respostas_positivas == 2:
    print("Suspeita")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
