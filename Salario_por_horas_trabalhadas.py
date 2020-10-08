SalarioHora = float(input("Quanto voce ganha por hora? "))
HorasTrabalhadas = float(input("Quantas horas voce trabalhou durante o mês? "))
SalarioTotal = SalarioHora * HorasTrabalhadas
print(f"Voce tem para receber R${round(SalarioTotal,2)} reais esse mes")
