import math

print("Este programa retorna o tepo estimado de download para um dado tamanho de arquivo e velocidade internet")
arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade da sua internet em mbps: "))
tempo = (arquivo/velocidade)/60
print(f"Seu arquivo de {arquivo}Mb vai demorar {round(tempo,2)} minutos")