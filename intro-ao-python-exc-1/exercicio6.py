# Exercício: Provedor de Internet
consumo = float(input('insira a quantidade consumida em GB: '))
tipo_plano = input('insira o tipo de plano: (R para residencial e E para empresarial): '.upper())

if consumo >= 10.00 and tipo_plano == "R":
    valorf = consumo * 8.00
    print(f"o valor a ser pago é: R$ {valorf:.2f}")
elif consumo > 10.00 and tipo_plano == "R":
    valorf = consumo * 12.00
    print(f"o valor a ser pago é: R$ {valorf:.2f}")
elif consumo >= 100.00 and tipo_plano == "E":
    valorf = consumo * 10.00
    print(f"o valor a ser pago é: R$ {valorf:.2f}")
else:
    valorf = consumo * 15.00
    print(f"o valor a ser pago é: R$ {valorf:.2f}")