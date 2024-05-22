salario = float(input("Informe seu Salário:"))

if salario <= 3000:
    print("promador junior")
elif salario > 3000 and salario <= 6000:
    print("promador pleno")
elif salario <= 3000 and salario <= 15000:
    print("promador senior")
else:
    print("gerente de projeto")