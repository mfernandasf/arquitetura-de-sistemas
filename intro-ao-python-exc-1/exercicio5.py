# Exercício: Cálculo do valor de multa
multa = 0
velocidade = float(input('insira a velocidade em Km/h: '))
if velocidade > 80:
  excesso = velocidade - 80
  multa = excesso * 5.00
  print('você foi multado')
  print(f'o valor da multa: R$ {multa:.2f}')
else:
  print('você está dentro do limite de velocidade')