lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[1]
except ZeroDivisionError:
    print('Nao e possivel realizar uma divisão por 0!')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmetica')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except Exception as ex:
    print('Erro Desconhecido. Erro: {}' . format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')