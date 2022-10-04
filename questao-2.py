salarioCarlos: float
salarioJoao: float
mes: int
mes = 0

salarioCarlos = float(input("Digite o salário do funcionário Carlos: "))

salarioJoao = salarioCarlos / 3
while salarioJoao <= salarioCarlos:
    mes += 1
    salarioCarlos *= 1.02
    salarioJoao *= 1.05

print(f"A quantidade de meses é: {mes}, o salário de Carlos virou: {round(salarioCarlos,2)} e o salário de João virou: {round(salarioJoao,2)}")