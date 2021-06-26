# import calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(1982, 12)
# print(str)


def calcular(lista, sinal): # def calcular(lista, sinal = '*'): se ele for utilizado dessa forma, o progroma entenderá que o operador padrao é a multiplicação. Se não for colocado o operador no input, ele usará
    resultado = 1
    for i in lista:
        if sinal == '+':
            resultado += i
        elif sinal == '-':
            resultado -= i
        elif sinal == '*':
            resultado *= i
        elif sinal == '/':
            resultado /= i
        else:
            return 'Operador inválido'
    return resultado