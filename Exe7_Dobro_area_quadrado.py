import math

print("Este programa lê o valor do lado de um quadrado, calcula a area e retorna seu dobro")
lado = float(input("Digite o lado de um quadrado: "))
AreaEmDobro = (math.pow(lado,2)) * 2.0
print(f"O dobro da area de um quadrado é {round(AreaEmDobro,2)}")
