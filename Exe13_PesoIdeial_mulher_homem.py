print("Programa que calcula o peso ideia baseado na altura da pessoa")
Altura = float(input("Digite sua altura em metros: "))
Sexo = input("Digite seu sexo, h para homem ou m para mulher: ")
Sexo2 = Sexo.lower()
if Sexo2 == "h":
    PesoIdealHomem = (72.7 *Altura) - 58.0
    print(f"Para uma altura de {Altura}m , o peso ideal é de {round(PesoIdealHomem,2)}Kg")
elif Sexo2 == "m":
    PesoIdealMulher = (62.1*Altura) - 44.7
    print(f"Para uma altura de {Altura}m , o peso ideal é de {round(PesoIdealMulher,2)}Kg")
else:
    print("Entrada invalida")

