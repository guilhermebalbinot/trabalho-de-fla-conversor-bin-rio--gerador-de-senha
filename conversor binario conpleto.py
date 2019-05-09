


import math

resultado = ''
n = float(input('digite o valor a ser trans formado em numero binario:'))
x = n
while n > 0:
    #o codigo vai ser repeti do enqunto n for maior que 0 
    n = n / 2
  if n % 2 == 0:
    # n vaiser dividido pro dois, só o resto da divisão vai ser conputado
    n = n / 2
    resultado = '0' + str(resultado)
  else:
    n = n / 2
    n = math.floor(n)
    resultado = '1' + str(resultado)

resultado = str(str('o valor de: ') + str(x)) + ('O numero em  binario:') + str(resultado)
print(resultado)
print(" O valor digitado foi:",x )



