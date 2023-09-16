#============[ A ]IMPORTANDO MÓDULOS:=========================================================================
from time import sleep
import math
import os
import datetime
from random import randint
c = 0
print("\033[1;7;34;41m", end= "") #>(Letra negrita/Texto Vermelho/Fundo Azul)

#============[ B ]FUNÇÕES UNIVERSAIS:=========================================================
def linha(txt):
    print("_" *35)
    print(txt)
    print("_" *35)
      
def PROCESSO(txt, I, F, P, S):
    for c in range(I, F, P):   
        print(f"{txt}({c}%)...",end="\r")
        sleep(S)
        
def PROCESSANDO():
    PROCESSO("⌛Processando", 00, 101, 1, 0.1)
     
def FIM():
    sleep(3)
    print("-" *20)
    print("⛔THE END")
    print("-" *20)
    PROCESSO("⌛Inderisando", 00, 125, 25, 0.4)
    
def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("😬ERRO! Digite um valor Inteiro!!!")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
            return n
        else:
            return n 
            
def VALOR_FLOAT(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"😬ERRO!: \'{entrada}\' é valor inválido!!!")  
        else:
            válido = True
            return float(entrada)
            
#============[ B ]SENHA/APRESENTAÇÃO:========================================================================
cont = 1
def tempo(txt1, I, txt2):
     print(f"😠Foram {cont} tentativas!!!", end="\r")
     sleep(2)
     for c in range(I, 0, -1):
         print(f"{txt1}: {c} {txt2}", end="\r")
         sleep(1)
     senha = str(input("🔐Digite a senha para começar:\n>>>"))   
senha = str(input("🔐Digite a senha para começar:\n>>>"))
while senha not in "SAMUEL":
    cont += 1
    senha = str(input("🔒Senha inválida!!!Tente novamente:\n>>>"))
    if cont == 3:
        tempo("⌛Aguarde", 60, "segundos...")        
    elif cont == 6:
        tempo("⌛Aguarde", 300, "segundos...")
    elif cont > 10:
        tempo("⌛Aguarde", 9999999, "segundos...")                
print("=" *35, f"\n👏PARABÉNS!!!\n🔓VOCÊ ACERTOU!!!\n⭐Foram {cont} tentativas!!!\n", "=" *35)
sleep(2)
PROCESSO("⌛Iniciando", 00, 110, 10, 0.7)
name = str(input("👽Para começarmos, por favor, digite o seu nome:\n>>>")).strip()
print(f"🌞Seja bem vindo ao Gnoses, {name}. Esse programa foi criado para resolver pequenos problemas!")
sleep(3)
print("⏬Você irá receber o menu de opções logo abaixo. Basta digitar o número da função que você deseja usar:")

#==========[ C ]MENU PRINCIPAL:================================================================================
opcao = 0
while opcao != 21:
    PROCESSO("⌛Carregando", 00, 120, 20, 0.5)     
    linha('''   
       🏆MENU PRINCIPAL: \n  
   🙌 [ 0 ] SAIR DO PROGRAMA
   👅 [ 1 ] ENTREVISTA COPT
   ♏ [ 2 ] CALCULAR MÉDIA
   ♈ [ 3 ] CALCULAR IMC
   ♎ [ 4 ] CALCULAR DESCONTO
   ♐ [ 5 ] CALCULAR AUMENTO
   💣 [ 6 ] CONVERTER TEMPERATURA
   📐 [ 7 ] CALCULAR HIPOTENUSA  
   📏 [ 8 ] CALCULAR SCT
   🎨 [ 9 ] PINTAR PAREDE
   🚗 [ 10 ] ALUGUEL CARRO
   🚦 [ 11 ] RADAR ELETRÔNICO
   🌞 [ 12 ] CUSTO DA VIAJEM 
   📆 [ 13 ] ANO BISSEXTO
   💰 [ 14 ] APROVANDO EMPRÉSTIMO
   💱 [ 15 ] CONVERSOR NUMÉRICO
   💂 [ 16 ] ALISTAMENTO MILITAR
   🔷 [ 17 ] ANALISADOR TRIÂNGULO
   🛂 [ 18 ] DETECTOR PALINDROMO
   🎮 [ 19 ] JOGO ADIVINHAÇÃO
   🏧 [ 20 ] PROGRESSÃO ARITMÉTICA
             ''')    
    opcao = VALOR_INT("\n😎Digite o número da sua opção:\n>>>") 
    PROCESSO("⌛Carregando", 00, 110, 10, 0.2)
     
#===========[ 1 ]ENTREVISTA DE EMPREGO:============================================
    if opcao == 1:
         print("🔺AVISO: Essa entrevista se trata apenas de uma SIMULAÇÃO!!!")
         sleep(3)
         print("😎Seja bem vindo a mais uma entrevista de emprego genérica.")
         sleep(3)   
         nome = input("😎Qual é o seu nome?\n>>>").strip().upper()
         if "SAMUEL" in nome or "DANIEL" in nome or "LUCAS" in nome or "MARIA" in nome or "ANA" in nome:
             print("😍Que nome lindo você tem!")
         else: 
             print("😒Seu nome é tão comum!")
         sleep(3)       
         sexo = input("😎Informe o seu sexo[M/F]:\n>>>").strip().upper()[0]
         while sexo not in "MmFf":
             sexo = input("😠Dados inválidos!!!\n😬Por favor, informe seu sexo[M/F]:\n>>>").strip().upper()[0]
         if sexo == "M":
            sexo = "HOMEM"
         if sexo == "F":
            sexo = "MULHER"
         print(f"🌝Isso significa que você é {sexo}!!!")
         sleep(3)    
         idade = VALOR_INT("😎Qual é a sua idade?\n>>>")
         if idade <= 30:
             print("😱Nossa,como você é jovem!!!")
         else: 
             print("💪É...Ainda dá pro gasto!")
         sleep(3)    
         mora = input("😎Onde você mora?\n>>>").strip().upper()
         if "ACRE" in mora or "SERGIPE" in mora:
             print("🌚Sei,na terra dos dinossauros!")
         elif "BRASIL" in mora or "ARGENTINA" in mora:
             print("😏Sei,no país menos corrupto!")
         else:
             print("🌎Excelente!!!")
         sleep(3)    
         trabalha = input("😎Você trabalha em quê?\n>>>").strip().upper()
         if "NÃO" in trabalha or "NAO" in trabalha or "DESEMPREGADO" in trabalha or "DESEMPREGADA" in trabalha or "AUTÔNOMO" in trabalha or "AUTÔNOMA" in trabalha or "AUTONOMO" in trabalha or "AUTONOMA" in trabalha:
             print("😔Com essa crise fica difícil mesmo!")
         else:
             print("🙌Que bom!!!")
         sleep(3)        
         escola = input("😎Você tem o ensino médio completo?\n>>>").strip().upper()
         if "SIM" in escola or "TENHO" in escola or "FIZ" in escola or "FACULDADE" in escola or "UNIVERSIDADE" in escola:
             print("👏PARABÉNS!!!")
         elif "NÃO" in escola or "FUNDAMENTAL" in escola:
             print("😔Assim fica complicado️!") 
         else:
             print("👏️Continue,que você consegue!!!️")
         sleep(3)      
         meta = input("😎Quais são suas metas para o futuro?\n>>>").strip().upper()
         print("☺️Com estudo e dedicação você consegue!")
         sleep(3)    
         experiência = input("😎Agora me conta: Qual é sua experiência profissional?\n>>>").strip().upper()
         if "NÃO" in experiência or "POUCO" in experiência or "POUCA" in experiência or "NENHUM" in experiência or "NENHUMA" in experiência:
             print("😏Nunca é tarde para aprender coisas novas!!!")
         else:
             print("⚡A cada dia; Novo aprendizado!!!")         
         if "MÉDICO" in experiência and meta or "DOUTOR" in experiência and meta or "ADVOGADO" in experiência and meta or "JUIZ" in experiência and meta or "POLÍTICO" in experiência and meta:
             vetor = "👍APROVADO!"
         else:
             vetor = "👎REPROVADO!"                   
         print("😎Agora você irá receber o relatório da entrevista!Aguarde um momento...")
         sleep(2)         
         PROCESSANDO()
         linha(f"  🔰RELATÓRIO FINAL:\n⭐Seu Nome é: {nome}!\n⭐Seu sexo: {sexo}!\n⭐Sua Idade é {idade}!\n⭐Você Mora no: {mora}!\n⭐Seu Trabalho é: {trabalha}!\n⭐Sua Meta é: {meta}!\n⭐Sua Escolaridade (EM): {escola}!\n⭐Sua Experiência é: {experiência}!\n⭐RESULTADO: {vetor}")       
         FIM()
    
#==============[ 2 ]CALCULO DA MÉDIA ARITMÉTICA:==========================================
    elif opcao == 2:   
         print("😎Irei calcular as suas 4 notas das provas...")
         sleep(3)    
         nota1 = VALOR_FLOAT("😎Digite a sua 1° Nota da prova:\n>>>")
         nota2 = VALOR_FLOAT("😎Digite a sua 2° Nota da prova:\n>>>")
         nota3 = VALOR_FLOAT("😎Digite a sua 3° Nota da prova:\n>>>")
         nota4 = VALOR_FLOAT("😎Digite a sua 4° Nota da prova:\n>>>")      
         média = (nota1 + nota2 + nota3 + nota4) / 4    
         PROCESSANDO()
         linha(f"⚡Sua 1° Nota é: ({nota1:.1f});\n⚡Sua 2° Nota é: ({nota2:.1f});\n⚡Sua 3° Nota é: ({nota3:.1f});\n⚡Sua 4° Nota é: ({nota4:.1f});\n⭐A sua MÉDIA é: ({média:.1f})!")    
         if 7 > média >= 5:
             linha("⭐RESULTADO: Você está de RECUPERAÇÃO!")
         elif média < 5:
            linha("⭐RESULTADO: Você está REPROVADO!")
         elif média >= 7:
             linha("⭐RESULTADO: Você está APROVADO!")       
         FIM()         
      
#============[ 3 ]CALCULO DO IMC:==================================================================================
    elif opcao == 3:  
         print('😎Agora irei calcular o seu IMC (Índice de massa corporal),para saber se você está em forma.')
         sleep(3)        
         altura = VALOR_FLOAT("😎Digite sua altura em metros:\n>>>")
         peso = VALOR_FLOAT("😎Digite o seu peso em Kg:\n>>>")         
         imc = peso / altura ** 2       
         PROCESSANDO()
         linha(f"⚡Seu Peso é: ({peso:.2f})!\n⚡Sua altura é: ({altura:.2f})!\n⭐Seu IMC é {imc:.2f}!")       
         if imc < 16:
            linha("⭐RESULTADO: Seu estado é magreza grave!")
         elif imc < 17:
            linha("⭐RESULTADO: Seu estado é magreza moderada!")
         elif imc < 18.5:
         	linha("⭐RESULTADO: Seu estado é magreza leve!")
         elif imc < 25:
            linha("⭐RESULTADO: Você é Saudável!")
         elif imc < 30:
            linha("⭐RESULTADO: Sobrepeso!")
         elif imc < 35: 
            linha("⭐RESULTADO: Obesidade Grau I!")
         elif imc < 40:
            linha("⭐RESULTADO: Obesidade Grau II!")
         else:
            linha("⭐RESULTADO: Obesidade Grau III!")     
         FIM()

#==============[ 4 ]CALCULAR DESCONTOS(%):==================================================================================  
    elif opcao == 4:
        print("😎Agora vamos calcular o seu desconto...")
        sleep(3)
        preço = VALOR_FLOAT("😎Digite o seu valor original(R$):\n>>>")
        desconto = VALOR_FLOAT("😎Digite o seu desconto(%):\n>>>")
        pagar = preço - (preço * desconto / 100)   
        PROCESSANDO()
        linha(f"⚡Preço de R${preço:.2f}!\n⚡Com um desconto de {desconto:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")        
        FIM()
              
#==============[ 5 ]CALCULAR AUMENTOS(%):==================================================================================  
    elif opcao == 5:
        print("😎Agora vamos calcular o seu aumento...")
        sleep(3)
        preço = VALOR_FLOAT("😎Digite o seu valor original(R$):\n>>>")
        aumento = VALOR_FLOAT("😎Digite o seu aumento(%):\n>>>")
        pagar = preço + (preço * aumento / 100)  
        PROCESSANDO()
        linha(f"⚡Preço de R${preço:.2f}!\n⚡Com um aumento de {aumento:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")       
        FIM()        
        
#==============[ 6 ]CONVERSOR DE TEMPERATURAS:===================================================
    elif opcao == 6:
        def menu_inicial():
            print("😎Esse é um programa para Conversão de Temperaturas!(C°/F°).")
            sleep(3)
            linha("📤Envie 1 para converter de Celsius para Fahrenheit;\n📥Envie 2 para converter de Fahrenheit para Celsius!")
            sleep(3)    
        def cel_fahr():
            C = VALOR_FLOAT("😎Agora digite a temperatura em graus Celsius(ex:30):\n>>>")
            F = C * (9 / 5) + 32
            PROCESSANDO()            
            linha(f"⚡Convertendo: {C:.2f}°C!\n⭐Valor em Fahrenheit é {F:.2f}°F!")                
        def fahr_cel():
            F = VALOR_FLOAT("😎Agora digite a temperatura em graus Fahrenheit(ex:120):\n>>>")
            C = (F - 32) * (5 / 9)
            PROCESSANDO()           
            linha(f"⚡Convertendo: {F:.2f}°F!\n⭐Valor em Celsius é {C:.2f}°C!")                      
        if __name__=='__main__':
            menu_inicial()
        while True:   
            escolha = VALOR_INT("😎Escolha o tipo de conversão que deseja realizar:\n>>>")   
            if escolha == 1:
                cel_fahr()
                break
            elif escolha == 2:
                fahr_cel()
                break
            else:
                print("😠Valor inválido. Tente novamente!!!")         
        FIM()      
        
#============[ 7 ]CALCULAR HIPOTENUSA:========================================
    elif opcao == 7:
          CO = VALOR_FLOAT("😎Digite o comprimento do cateto oposto(ex:34):\n>>>")
          CA = VALOR_FLOAT("😎Digite o complemento do cateto adjacente(ex:30):\n>>>")
          HP = (CO**2 + CA**2) ** (1/2)
          PROCESSANDO()         
          linha(f"  🈯Considerando quê:\n⚡O comprimento do CO é: {CO:.2f}!\n⚡O comprimento do CA é: {CA:.2f}!\n⭐A hipotenusa mede: {HP:.2f}!")                       
          FIM()
              
#==========[ 8 ]CALCULAR SCT:=============================================            
    elif opcao == 8: 
         print("😎Irei calcular o seno, cosseno e tangente!")
         sleep(2)        
         ângulo = VALOR_FLOAT("😎Digite o ângulo(ex:30):\n>>>")
         seno = math.sin(math.radians(ângulo))
         cosseno = math.cos(math.radians(ângulo))
         tangente = math.tan(math.radians(ângulo))
         PROCESSANDO()        
         linha(f"⚡Com ângulo de {ângulo};\n⭐Ângulo do Seno é: {seno:.2f}!\n⭐Ângulo do Cosseno é: {cosseno:.2f}!\n⭐Ângulo da Tangente é: {tangente:.2f}!")            
         FIM()
         
#===========[ 9 ]PINTAR PAREDE:========================================================================================================================        
    elif opcao == 9:        
         print("🌝Irei fazer o cálculo para descobrir a quantidade de litros de tinta para você pintar a sua parede!")
         sleep(3)
         base = VALOR_FLOAT("😎Digite a largura da parede(m):\n>>")
         altura = VALOR_FLOAT("😎Digite a altura da parede(m):\n>>>")
         área = base * altura
         tinta = área / 2
         PROCESSANDO()         
         linha(f"⚡Sua dimensão é ({base:.0f})m × ({altura:.0f})m!\n⚡Para pintar a parede de {área:.0f}m²;\n⭐Precisará usar {tinta:.2f}L de tinta!")         
         FIM()
              
#===========[ 10 ]ALUGUEL DE CARROS:==============================================================================================     
    elif opcao == 10:           
         print("😎Irei Calcular para você o valor do aluguel de um carro!")
         sleep(3)
         valor_dia = VALOR_FLOAT("😎Me diga, quanto custa o aluguel por dia(R$)?\n>>>")
         valor_km = VALOR_FLOAT("😎Me responda, quanto custa um quilômetro rodado(R$)?\n>>>")
         dias = VALOR_INT("😎Por quantos dias foi alugado?\n>>>")
         km = VALOR_FLOAT("😎Quantos km você andou?\n>>>")
         pagar = (dias * valor_dia) + (km * valor_km)
         PROCESSANDO()         
         linha(f"  💰Considerando quê:\n⚡O valor por dia é R${valor_dia:.2f}!\n⚡O valor por km é R${valor_km:.2f}!\n⚡Você usou por {dias} dias!\n⚡Andou com o carro: {km:.2f}km!\n⭐O total a pagar é R${pagar:.2f}!")        
         FIM()
                  
#=========[ 11 ]RADAR ELETRÔNICO:=========================
    elif opcao == 11:      
         velocidade = VALOR_FLOAT("😎Qual é a velocidade do seu carro?\n>>>")
         limite = VALOR_FLOAT("😎Qual é o limite de velocidade?\n>>>")
         PROCESSANDO()
         if velocidade > limite:
             print(f"😡MULTADO! Você excedeu o limite permitido; Que é {limite:.2f}km/h!!!")
             sleep(2)
             valor = VALOR_FLOAT("😤Para saber quanto você deve pagar, digite o valor da multa(R$) por cada km acima do limite:\n>>>")
             multa = (velocidade-limite)*valor
             PROCESSANDO()             
             linha(f"⭐Com velocidade do carro: {velocidade:.0f}km/h;\n⭐Sendo o limite de {limite:.0f}km/h;\n⭐Valor da multa por km é: R${valor:.2f};\n⭐Valor a pagar é: R${multa:.2f}!!!")            
             sleep(2)
         else:
             print("😎PARABÉNS!!! Você não excedeu o limite de velocidade!!!")
             sleep(2)
         print("😎Desejo boa sorte!!!")       
         FIM()                       

#===========[ 12 ]CUSTO DA VIAGEM:===================================================
    elif opcao == 12:      
         distância = VALOR_FLOAT("😎Qual é a distância da sua viagem(km)?\n>>>")
         preço = VALOR_FLOAT("😎Qual é o preço por km?\n>>>")        
         pagar = distância * preço
         PROCESSANDO()                
         linha(f"⭐Com a distância de {distância:.0f}km;\n⭐Preço por km sendo R${preço:.2f};\n⭐Valor a pagar é R${pagar:.2f}!")      
         if pagar <= 200:
             linha("😎MUITO BOM!!!")
         else:
             linha("💸QUE ABSURDO!!!")          
         FIM()
                 
#===========[ 13 ]ANO BISSEXTO:===============================================================
    elif opcao == 13:      
         ano = VALOR_INT("😎Que ano você quer analisar?\n🌚Envie 0 para analisar o ano atual:\n>>>")        
         if ano == 0:
             ano = datetime.date.today().year
         PROCESSANDO()      
         if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
             linha(f"⭐ANO {ano}!\n⭐BISSEXTO:👍SIM!\n⭐FEVEREIRO: ➕29 DIAS!")
         else:
             linha(f"⭐ANO {ano}!\n⭐BISSEXTO:👎NÃO!\n⭐FEVEREIRO: ➖28 DIAS!")             
         FIM()
          
#============[ 14 ]APROVANDO EMPRÉSTIMO:==========================
    elif opcao == 14:      
         casa = VALOR_FLOAT("😎Qual é o valor da casa(R$)?\n>>>")
         salário = VALOR_FLOAT("😎Qual é o valor do seu salário(R$)?\n>>>")
         anos = VALOR_INT("😎Quantos anos de financiamento?\n>>>")
         prestação = casa / (anos * 12)
         mínimo = salário * 30 / 100
         PROCESSANDO()
         if prestação <= mínimo:
             resultado = "👍APROVADO"
         else:
             resultado = "👎NEGADO"     
         linha(f"⭐Pagar uma casa de R${casa:.2f};\n⭐Com salário de R${salário:.2f};\n⭐Em {anos} anos;\n⭐Prestação será de R${prestação:.2f};\n⭐Valor mínimo R${mínimo:.2f};\n⭐EMPRÉSTIMO:{resultado}!")                
         FIM()
                 
#============[ 15 ]CONVERSOR DE BASES NUMÉRICAS:===========================
    elif opcao == 15:     
         num = VALOR_INT("😎Digite um número inteiro:\n>>>")
         print("😎Escolha uma das bases para conversão:")       
         linha('''
         	🎂OPÇÕES:
         [ 1 ] BINÁRIO;
         [ 2 ] OCTAL;
         [ 3 ] HEXADECIMAL;''')
         opção = VALOR_INT("\n😎Escolha a sua opção:\n>>>")
         PROCESSANDO()         
         if opção == 1:
             linha(f"⭐Valor: {num:.0f};\n⭐Em BINÁRIO: {bin(num)[2:]}!")
         elif opção == 2:
             linha(f"⭐Valor: {num:.0f};\n⭐Em OCTAL: {oct(num)[2:]}!")
         elif opção == 3: 
             linha(f"⭐Valor: {num:.0f};\n⭐Em HEXADECIMAL: {hex(num)[2:]}!")
         else:
             linha("😡VALOR INVÁLIDO!!!")                                         
         FIM()
                 
#============[ 16 ]ALISTAMENTO MILITAR:============================
    elif opcao == 16:     
         atual = datetime.date.today().year
         sexo = input("😎Qual é o seu sexo[M/F]?:\n>>>").strip().upper()[0]
         while sexo not in "MmFf":
            sexo = input("😬Dados inválidos!!!\n😠Por favor, informe seu sexo[M/F]:\n>>>").strip().upper()[0]     
         if sexo == "M":
             nasc = VALOR_INT("😎Digite o ano do seu nascimento:\n>>>")
             idade = atual - nasc
             PROCESSANDO()             
             if idade == 18:
                  resultado = "⭐Tem que se alistar imediatamente!"
             elif idade < 18:
                 saldo = 18 - idade 
                 ano = atual + saldo
                 resultado = f"⭐Faltam {saldo:.0f} anos para o alistamento!\n⭐Seu alistamento será em {ano:.0f}!"
             elif idade > 18:
                 saldo = idade - 18
                 ano = atual - saldo
                 resultado = f"⭐Deveria ter se alistado há {saldo:.0f} anos!\n⭐Seu alistamento foi em {ano:.0f}!"        
             linha(f"⭐Para quem nasceu em {nasc:.0f};\n⭐Tem {idade:.0f} anos em {atual:.0f};\n{resultado}")     
         elif sexo == "F":
             print("😔Sinto muito!!!; Em nosso país só é permitido homens!!!")
         else:
             print("😡Não compreendo!!!")             
         FIM()
             
#===========[ 17 ]ANALISANDO TRIÂNGULOS:=========================
    elif opcao == 17:    
         r1 = VALOR_FLOAT("😎Digite o primeiro segmento:\n>>>")
         r2 = VALOR_FLOAT("😎Digite o segundo segmento:\n>>>")
         r3 = VALOR_FLOAT("😎Digite o terceiro segmento:\n>>>")
         PROCESSANDO()         
         if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
             if r1 == r2 == r3:
                 triângulo = "👍SIM;\n⭐TIPO: EQUILÁTERO!"
             elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
                 triângulo = "👍SIM;\n⭐TIPO: ISÓSCELES!"
             elif r1 != r2 != r3 != r1:
                 triângulo = "👍SIM;\n⭐TIPO: ESCALENO!"
         else:
             triângulo = "👎NÃO!"
         linha(f"⭐SEGMENTOS: {r1}, {r2} e {r3}!\n⭐TRIÂNGULO?:{triângulo}")              
         FIM()
                
#===============[ 18 ]DETECTOR DE PALÍNDROMO:===============================
    elif opcao == 18:             
         frase = input("😎Digite uma frase:\n>>>").strip().upper()
         palavras = frase.split()
         junto = "*".join(palavras)
         inverso = " "
         PROCESSANDO()
         for letra in range(len(junto) -1, -1, -1):
             inverso += junto[letra]
         if inverso == junto:
             resultado = "👍SIM!!!"
         else:
             resultado = "👎NÃO!!!"         
         linha(f"⭐Você inscreveu: {junto}!\n⭐Inverso é {inverso}!\n⭐É Palíndromo?:{resultado}")         
         FIM()
                
#===============[ 19 ]JOGO ADIVINHAÇÃO:================================================ 
    elif opcao == 19:      
         computador = randint(0,10)
         print("😠Acabei de pensar em um número entre 0 e 10!")
         sleep(2)
         acertou = False
         palpites = 0
         while not acertou:
             jogador = VALOR_INT("😎Qual é o seu palpite?:\n>>>")
             palpites += 1
             PROCESSANDO()
             if jogador == computador:
                 acertou = True
                 resultado = f"👍ACERTOU!\n🔔Foram {palpites} Tentativas!"
             else:
                 if jogador < computador:
                     linha(f"👎ERRADO!\n➕É MAIOR DO QUE {jogador}!")
                 elif jogador > computador:
                     linha(f"👎ERRADO!\n➖É MENOR QUÊ {jogador}!!!")            
         linha(f"⭐Eu pensei no n° {computador}!\n⭐Você digitou: {jogador}!\n⭐RESULTADO:{resultado}")        
         FIM()
                                
#==========[ 20 ]PROGRESSÃO ARITMÉTICA (3.0):====================================
    elif opcao == 20:      
         n = VALOR_INT("😎Digite o valor:\n>>>")
         r = VALOR_INT("😎Digite a razão:\n>>>")
         termo = n
         cont = 1
         total = 0
         mais = 10
         while mais != 0:
             PROCESSANDO()
             total = total + mais
             while cont <= total:
                 print(f"⭐{termo}›", end= "")    
                 termo += r
                 cont += 1
             print("\n⛔PAUSA!!!")
             mais = VALOR_INT("😎Quantos termos você quer mostrar a mais?\n😎Digite 0 caso queira parar:\n>>>")
         linha(f"⛔FINALIZADO COM TOTAL {total} TERMOS!")         
         FIM()
                                                                          
#=============[ D ]FIM DO PROGRAMA:==================================================
    elif opcao == 0:
         PROCESSO("⌛Finalizando", 00, 110, 10, 0.7)           
         print("=" *25, "\n  🌎CRÉDITOS:", "\n👤CRIADOR: Samuel Martins;\n📆DATA: 21/12/2021;\n🌎CANAL: Curso em vídeo;\n👅SOUCER: Python.\n", "=" *25)
         sleep(2)
         print("-" *20, "\n⛔FIM DO PROGRAMA!\n".center(10), "-" *20)
         exit()
    else:
        print("😠Opção inválida.Tente novamente!")
        sleep(2)