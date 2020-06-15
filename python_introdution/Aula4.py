# This Python file uses the following encoding: utf-8
import os, sys
a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado! Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado! Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado! terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado! Quarto bimestre: '))
media = (a + b + c + d) / 4
if media >= 7.0:
    print('Você foi aprovado. Sua média é: {}' . format(media))
else:
    print('Você foi reprovado. Sua média é: {}' . format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:


    # print('Foi informado algum valor errado')

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número é par!')
# else:
#     print('nenhum Número par foi digitado! !')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
# if a > b and a > c:
#     print('O maior número é:{}' .format(a))
# elif b > a and b > c:
#     print('O maior número é: {}' .format(b))
# else:
#     print('O maior número é: {}'. format(c))
# print('Final do  Programa')
