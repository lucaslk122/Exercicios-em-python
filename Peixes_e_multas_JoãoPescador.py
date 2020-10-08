print("Bem vindo senhor João Papo-de-Pescador")
print("De acordo com as regras do estado de SP, o senhor não deve trazer mais que 50kg de peixe,a taxa é de R$4.00 por quilo excedente")
Peso = float(input("Quantos kilos o senhor trouxe hoje? "))
if Peso > 50.0:
    Excendente = Peso - 50.0
    Multa = Excendente*4.00
    print(f"O senhor excendeu em {Excendente}Kg, portanto deve de pagar R${Multa} reais de multa")
else:
    print("O senhor não excendeu o psso limite portanto, não precisa pagar nada")


