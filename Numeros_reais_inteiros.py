import math

NumeroInteiro = int(input("Digite um numero inteiro: ")) #primeiro numero
NumeroInteiro2 = int(input("Digite um segundo numero inteiro: "))  #Segundo numero
NumeroReal = float(input("Digite um numero real: ")) #terceiro numero
PrimeiroCalculo = (2*NumeroInteiro) * (NumeroInteiro2/2)
print(f"O produto do dobro do primeiro com metade do segundo é {int(PrimeiroCalculo)}" )
SegundoCalculo = (3*NumeroInteiro) + NumeroReal
print(f"A soma do triplo do primeiro com o terceiro é {float(round(SegundoCalculo,2))}")
TerceiroCalculo = math.pow(NumeroReal,3.0)
print(f"O terceiro elevado ao cubo é {round(TerceiroCalculo,2)}")