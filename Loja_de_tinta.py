import math

print("1L de tinta pinta 3 metros quadrados, cada galão possui 18L e custam R$80.00 cada")
Area = float(input("Digite o tamanho da area em metros quadrados a ser pintada: "))
Litros = float(Area/3)
Latas = float(Litros/18)
Preço = float(round(Latas,0)*80)
print(f"Voce vai precisar de {math.ceil(Latas)} lata de tinta para pintar {Area}m^2, portanto, pagará R${round(Preço,2)}")


