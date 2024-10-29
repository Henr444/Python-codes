import math
while True:
  ang=float(input('Entre com o angulo em graus: '))
  print('Selecione a função trigonometrica a ser calculada: ')
  print(f'(1) cos({ang})')
  print(f'(2) sin({ang})')
  print(f'(3) tan({ang})')
  print('(4) Sair')
  op=int(input('Opção escolhida: '))
  match op:
    case 1:
      rad=math.radians(ang)
      cos=math.cos(rad)
      print(f'Cos({ang} = {cos})')
    case 2:
      rad=math.radians(ang)
      sin=math.sin(rad)
      print(f'Sin({ang} = {sin})')
    case 3:
      rad=math.radians(ang)
      tan=math.tan(rad)
      print(f'Tan({ang} = {tan})')
    case 4:
      print('Programa encerrado!')
      break
    case _:
      print('Opcao invalida')
