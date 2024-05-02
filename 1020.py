import math

idade_em_dias = int(input())

idade_em_anos = math.floor(idade_em_dias / 365)
idade_em_meses = math.floor((idade_em_dias % 365) / 30)
idade_em_dias_restantes = math.floor((idade_em_dias % 365) % 30)

print(f"{idade_em_anos} ano(s)")
print(f"{idade_em_meses} mes(es)")
print(f"{idade_em_dias_restantes} dia(s)")
