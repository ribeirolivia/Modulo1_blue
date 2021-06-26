# def calcular(lista, sinal): # def calcular(lista, sinal = '*'): se ele for utilizado dessa forma, o progroma entenderá que o operador padrao é a multiplicação. Se não for colocado o operador no input, ele usará
#     resultado = 1
#     for i in lista:
#         if sinal == '+':
#             resultado += i
#         elif sinal == '-':
#             resultado -= i
#         elif sinal == '*':
#             resultado *= i
#         elif sinal == '/':
#             resultado /= i
#         else:
#             return 'Operador inválido'
#     return resultado


# from testefuncao import calcular #### 1° importar a função quando ela está em outro arquivo
import testefuncao #2° é outra forma de usar, quando vc precisa só de 1 funçao do arquivo
a = testefuncao.calcular(entradas, operador) ###2°

entradas = []
for i in range(5):
    numero = int(input('Entre um número: '))
    entradas.append(numero)

operador = input('Digite a operação que deseja: ')
print(calcular(entradas, operador))


##### Como comitar no Git




