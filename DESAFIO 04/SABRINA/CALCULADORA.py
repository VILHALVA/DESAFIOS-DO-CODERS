import math

def calcular_media():
    numeros = input("Digite os números separados por espaço: ").split()
    numeros = [float(numero) for numero in numeros]
    media = sum(numeros) / len(numeros)
    return f"A média é: {media}"

def calcular_imc():
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    imc = peso / (altura ** 2)
    return f"O IMC é: {imc:.2f}"

def calcular_desconto():
    valor_original = float(input("Digite o valor original: "))
    taxa_desconto = float(input("Digite a taxa de desconto (em porcentagem): "))
    valor_desconto = (taxa_desconto / 100) * valor_original
    return f"O valor com desconto é: {valor_original - valor_desconto:.2f}"

def calcular_aumento():
    valor_original = float(input("Digite o valor original: "))
    taxa_aumento = float(input("Digite a taxa de aumento (em porcentagem): "))
    valor_aumento = (taxa_aumento / 100) * valor_original
    return f"O valor com aumento é: {valor_original + valor_aumento:.2f}"

def converter_temperatura():
    print("Opções de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    escolha = int(input("Escolha a opção (1/2): "))
    if escolha == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        return f"A temperatura em Fahrenheit é: {fahrenheit:.2f}"
    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        return f"A temperatura em Celsius é: {celsius:.2f}"
    else:
        return "Opção inválida."

def calcular_hipotenusa():
    cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
    cateto2 = float(input("Digite o comprimento do segundo cateto: "))
    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    return f"O comprimento da hipotenusa é: {hipotenusa:.2f}"

def calcular_sct():
    angulo = float(input("Digite o ângulo em graus: "))
    radiano = math.radians(angulo)
    seno = math.sin(radiano)
    cosseno = math.cos(radiano)
    tangente = math.tan(radiano)
    return f"Seno: {seno:.2f}, Cosseno: {cosseno:.2f}, Tangente: {tangente:.2f}"

def analisador_triangulo():
    lados = input("Digite os lados do triângulo separados por espaço: ").split()
    lados = [float(lado) for lado in lados]
    lados.sort()
    if lados[0] + lados[1] > lados[2]:
        if lados[0] == lados[1] == lados[2]:
            return "Este é um triângulo equilátero."
        elif lados[0] == lados[1] or lados[1] == lados[2]:
            return "Este é um triângulo isósceles."
        else:
            return "Este é um triângulo escaleno."
    else:
        return "Estes lados não formam um triângulo."

def detector_palindromo():
    palavra = input("Digite uma palavra ou frase: ").lower().replace(" ", "")
    if palavra == palavra[::-1]:
        return "É um palíndromo."
    else:
        return "Não é um palíndromo."

def progressao_aritmetica():
    primeiro_termo = float(input("Digite o primeiro termo da progressão: "))
    diferenca = float(input("Digite a diferença comum: "))
    numero_termos = int(input("Digite o número de termos desejado: "))
    termos = [primeiro_termo + (n * diferenca) for n in range(numero_termos)]
    return f"Os termos da progressão são: {', '.join(map(str, termos))}"

while True:
    print("\nOperações da Calculadora:")
    print("1. Calcular Média")
    print("2. Calcular IMC")
    print("3. Calcular Desconto")
    print("4. Calcular Aumento")
    print("5. Converter Temperatura")
    print("6. Calcular Hipotenusa")
    print("7. Calcular SCT (Sen, Cos, Tan)")
    print("8. Analisador de Triângulo")
    print("9. Detector de Palíndromo")
    print("10. Progressão Aritmética")
    print("0. Sair")
    
    escolha = int(input("Escolha a operação desejada: "))

    if escolha == 0:
        break
    elif escolha == 1:
        resultado = calcular_media()
    elif escolha == 2:
        resultado = calcular_imc()
    elif escolha == 3:
        resultado = calcular_desconto()
    elif escolha == 4:
        resultado = calcular_aumento()
    elif escolha == 5:
        resultado = converter_temperatura()
    elif escolha == 6:
        resultado = calcular_hipotenusa()
    elif escolha == 7:
        resultado = calcular_sct()
    elif escolha == 8:
        resultado = analisador_triangulo()
    elif escolha == 9:
        resultado = detector_palindromo()
    elif escolha == 10:
        resultado = progressao_aritmetica()
    else:
        resultado = "Opção inválida."
    
    print("\nResultado:")
    print(resultado)

print("Calculadora encerrada.")
