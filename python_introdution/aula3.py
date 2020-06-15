import os, sys
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = int(a / b)
resto = a % b
resultado = ('Soma: {soma} . \nSubtração: {sub} .'
'\nMultiplicação{multi}' 
 '\nDivisão: {div}'
 '\nRest: {rest}'
      .format(soma=soma,
              sub=subtracao,
              multi=multiplicacao,
              div=divisao,
              rest=resto))
print(resultado)


