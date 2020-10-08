import math

print("Um galão com 18L custa R$80.00 e uma lata com 3,6L por R$25.00")
Area = float(input("Digite o tamanho da area em metros quadrados a ser pintada: "))
Litros = Area/6.0
folga = Litros + (Litros*0.10)
Latas_80L = math.ceil(folga/18.0)
Preço_80L = round(Latas_80L,2)*80
Latas_3_6L = math.ceil(folga/3.6)
Preço_3_6L = round(Latas_3_6L,2)*25
mistura = (folga//18)*80 + math.ceil((folga%18)//3.6)*25
print(f"Voce vai precisar de {Latas_80L} lata de tinta de 18L para pintar {Area}m^2, portanto, pagará R${Preço_80L}")
print(f"Voce vai precisar de {Latas_3_6L} lata de tinta de 3.6L para pintar {Area}m^2, portanto, pagará R${Preço_3_6L}")
print(f"A mistura resulta numv valor de R${mistura}")



