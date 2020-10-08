SalarioHora = float(input("Quanto voce ganha por hora? "))
HorasTrabalhadas = float(input("Quantas horas voce trabalhou durante o mês? "))
SalarioBruto = SalarioHora * HorasTrabalhadas
InssPagar = SalarioBruto*(11.0/100.0)
PagarSindicato = SalarioBruto*(5.0/100.0)
SalarioLiquido = SalarioBruto - InssPagar - PagarSindicato
print(f"Salario Bruto: R${round(SalarioBruto,2)}")
print(f"IR (11%) : R${float(InssPagar)}")
print(f"Sindicato ( 5%) : R${float(PagarSindicato)}")
print(f"Salário Liquido : R${float(SalarioLiquido)}")