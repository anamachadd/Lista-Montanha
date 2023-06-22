#1 - Faça um Programa que peça dois números e imprima o maior deles.
num1= int(input('Digite um número: '))
num2= int(input('Digite outro número: '))
if num1 > num2:
    print('O numero 1 é maior! :')

else:
    print('Num2 é maior! : ')
print()
#2- Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('Digite um valor: '))
if valor < 0:
    print("O valor é negativo")
else:
    print("O valor é positivo")
print()
# 3- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme
#a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
s = input("Digite F para Feminino ou M para Masculino: ")
if s == "F" or s == "f":
    print("Feminino")
elif s == "M" or s == "m":
    print("Masculino")
else:
    print("Sexo Inválido")
print()
# 4 -Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def verificarLetra():

    # lista vogais
    vogal = ['a', 'e', 'i', 'o', 'u']
    
    # lista consoantes
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'k', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'y']

    letra = input("Informe uma letra:")

    if letra.lower() in vogal:
        print ("Letra %s é uma vogal!" % letra.upper())

    elif letra.lower() in consoantes:
        print ("Letra %s é um consoante!" % letra.upper())

    else:
        print ("Por favor, informe somente uma letra!")
        verificarLetra()

print()
# 5 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e apresentar:
# 1)A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# 2)A mensagem "Reprovado", se a média for menor do que sete;
# 3)A mensagem "Aprovado com Distinção", se a média for igual a dez.
A1= int(input('Digite a nota da prova A1: '))
A2= int(input('Digite a nota da prova A2: '))
media = (A1 + A2) / 2 
print(media)
if media >= 7:
    print('APROVADO')
if media < 7 :
    print('REPROVADO')
else:
    print('APROVADO COM DISTINÇÃO! ')
print()
#6- Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))
num3 = int(input('Digite o numero 3: '))
if num1 > num2:
    print('O número 1 é o maior! ')   
if num1 > num3:
    print('O número 1 é o maior! ')
elif num2 > num1:
    print('O número 2 é o maior! ')   
else:
    print('O numero 3 é o maior')
print()
#7- Faça um Programa que leia três números e mostre o maior e o menor deles.
a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
print()
#8 -Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))
if preco1 < preco2 and preco1 < preco3:
    print(f"O produto com o menor preco é o 1, custando R${preco1:.2f}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto com o menor preco é o 2, custando R${preco2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${preco3:.2f}")
print()
#9- Faça um Programa que leia três números e mostre-os em ordem decrescente.a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >=c and c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a and c >= b and a >=b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b and b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')
print()
#10- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.turno = input(
    "Digite seu turno, M - matutino, V - vespertino, N - noturno: "
).upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")
print()
#11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.salario = float(input("Digite o seu salário"))

valor_baixo = salario * 0.20
baixo = salario * 1.20
valor_medio = salario * 0.15
medio = salario * 1.15
valor_alto = salario * 0.10
alto = salario * 1.10
valor_altissimo = salario * 0.05
altissimo = salario * 1.05

print("Antes Reajuste: ", salario)

if salario <= 280: print("Aumento: 20%\nValor: ", valor_baixo, "\nFinal: ", baixo)
elif salario > 200 and salario <= 700: print("Aumento: 15%\nValor: ", valor_medio, "\nFinal: ", medio)
elif salario > 700 and salario <= 1500: print("Aumento: 10%\nValor: ", valor_alto, "\nFinal: ", alto)
else: print("Aumento: 5%\nValor: ", valor_altissimo, "\nFinal: ", altissimo)
print()
#12 -Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
valor_da_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = valor_da_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${total_de_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)
print()
#13- Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia_int = int(input("Digite o número do dia da semana: "))
dia_str = ""
if dia_int == 1:
    dia_str = "Domingo"
elif dia_int == 2:
    dia_str = "Segunda"
elif dia_int == 3:
    dia_str = "Terça"
elif dia_int == 4:
    dia_str = "Quarta"
elif dia_int == 5:
    dia_str = "Quinta"
elif dia_int == 6:
    dia_str = "Sexta"
elif dia_int == 7:
    dia_str = "Sábado"

if dia_str == "":
    print("Valor inválido")
else:
    print(f"O dia correspondente é {dia_str}")
print()
#15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print ("Não pode ser um triangulo")
elif l1 == l2 == l3:
    print ("Equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print ("Isósceles")
else:
    print ("Escaleno")
print()
#16- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
a = float(input("Digite A: "))
if a == 0:
    print("Valor Invalido")
else:
    b = float(input("Digite B: "))
    c = float(input("Digite C: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
        print("A equação não possui raizes reais")
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
if delta == 0:
        print("1 Raiz real: ", x1)
else:
        print("2 raizes reais, x1: ", x1, "\nx2: ", x2)
print()
#17- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")
print()
#18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print("\tData Válida\n")
data = (input("Data: "))
if int(data[0:2]) != 0  and int(data[0:2]) <= 31 :
    if int(data[3:5]) != 0  and int(data[3:5]) <= 12 :
        if int(data[6:11]) != 0 :
            print("")
            print("Data Válida")
        else :
            print("")
            print("Data Inválida")
    else :
        print("")
        print("Data Inválida")
else:
    print("")
    print("Data Inválida")
print()
#20- Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
else:
    print("APROVADO com DISTINÇÃO")
print()
#21 -Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
if (
    valor < 10 or valor > 600
):  # Os parênteses não são necessários, mas vou passar a usá-los
    print("Valor inválido!")
else:
    cem = valor // 100  # Pegamos a centena com uma divisão inteira
    valor -= cem * 100  # Subtraímos as centenas retiradas do valor total
    cinquenta = valor // 50  # Idem para as outras coisas
    valor -= cinquenta * 50
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    um = valor  # Depois de subtrair as de cinco só sobram as de um
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")
print()
# 22- Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
print()
#23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero = float(input("Digite um número: "))
if numero % 1 == 0:
    print("Inteiro")
else:
    print("Decimal")
print()
# 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")
def checar():
    if (resultado_operacao // 1 == resultado_operacao):
        print("Inteiro")
        if resultado_operacao % 2 == 0:
            print("Par")
            if resultado_operacao > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")


if operacao == '+':
    resultado_operacao = numero1 + numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '-':
    resultado_operacao = numero1 - numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '/':
    resultado_operacao = numero1 / numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '*':
    resultado_operacao = numero1 * numero2
    print("Resultado: ", resultado_operacao)
    checar()
else:
    print("Valor Invalido")
print()
#25- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
positivos = 0
resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Mora perto da vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1

if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")
print()
#26- Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0
if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100
    else:
        preco -= 1.9 * litros * 5 / 100
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")
print()
#27-Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
morangos = int(input("Digite a quantidade de morangos [kg]: "))
macas = int(input("Digite a quantidade de maças [kg]: "))
preco_morango1 = morangos * 2.50
preco_morango2 = morangos * 2.20

preco_maca1 = macas * 1.80
preco_maca2 = macas * 1.50

print("quantidade de maçãs: ", macas, "\nQuantidade de morangos: ", morangos)

if morangos > 5:
    preco_certo_morango = preco_morango1
else:
    preco_certo_morango = preco_morango2

if macas > 5:
    preco_certo_maca = preco_maca1
else:
    preco_certo_maca = preco_maca2

preco_total = preco_certo_maca + preco_certo_morango

if preco_total > 25 or (macas + morangos) > 8:
    print("Preço final: ", (preco_total - (preco_total * 0.1)))
else:
    print("Preço final: ", preco_total)
print()
#28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
print("1- File Duplo\n2- Alcatra\n3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1p/ SIM - 2p/ NAO: "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80
        
if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80

if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    r = "NAO"
    total = preco
    
print("\n***************************CUPOM FISCAL**************************************")
print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço......................................................... %2.f R$ " %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total com desconto............................................ %2.f R$ " %total)
print("******************************************************************************")