def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro'


while True:
    print('=== Calculadora ===')
    try:
        n1 = float(input(' Digite um Numero:'))
        n2 = float(input('Digite outro Numero:'))
    except:
        print('Isso Não é um número!')
        continue
    

    print('Escolha um simbolo dentre as opçoes +, -, /, *')

    simbolo = input('Digite um Simbolo: ')

    if simbolo == '+':
        resultado = somar(n1, n2)

    elif simbolo == '-':
        resultado = subtrair(n1, n2)

    elif simbolo == '*':
        resultado = multiplicar(n1, n2)

    elif simbolo == '/':
        resultado = dividir(n1, n2)
    else:
        resultado = 'Símbolo Inválido'

    print(f'Resultado = {resultado}')

    continuar = input('Gostaria de continuar? (s/n):  ')
    if continuar.lower() != 's':
        print('Terminando a calculadora!')
        break





