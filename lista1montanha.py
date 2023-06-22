#1- Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Alo mundo!')
print()
#2- Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
n1 = int(input('Digite um número: '))
print('O numero informado foi' ,n1)
print()
#3- Faça um Programa que peça dois números e imprima a soma.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
print(soma)
print()
#4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = int(input('Digite a nota bimestral 1: '))
nota2 = int(input('Digite a nota bimestral 2: '))
nota3 = int(input('Digite a nota bimestral 3: '))
nota4 = int(input('Digite a nota bimestral 4: '))
med = (nota1+nota2+nota3+nota4)/4
print(med)
print()
#5- Faça um Programa que converta metros para centímetros.
met = float(input('Digite um número: '))
cent = (met )*100
print('Este Número em centimetros sera:{}'.format(cent) )
print()
#6- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
raio = int(input('Digite o raio de um circulo: '))
area= math.pi*raio**2
print(area)
#7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
num=int(input('Digite o número: '))
area= num**2
area*=2
print(area)
print()
#8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hr = float(input('Digite quanto você recebe por hora trabalhada: '))
hora = float(input('Digite o número de horas trabalhadas: '))
hora*= 60
min= float(input('Digite os minutos restantes:'))
valor_total= (((hora+min)*valor_hr)/60)
print('O valor total do salario é:{}'.format (valor_total))
print()
#9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
graus_Fahrenheit = float(input('Digite os graus_Fahrenheit'))
conv = (graus_Fahrenheit-32)*1.8
print(conv)
#10- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input('Digite os graus_celsius'))
graus_Fahrenheit = (celsius*1.8)+32
print(graus_Fahrenheit)
print()
#11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero interiro: '))
real = float(input('Digite um numero real: '))
print(num1)
print(num2)
print(real)
calc1 = (num1*2)*(num2/2)
print(calc1)
calc2 = (num1*3)+(real)
print(calc2)
calc3 = real**3
print(calc3)
print()
#12- Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.1
altura = float(input('Digite a altura da pessoa: '))
pes_ideal = (72.7* altura) - 58.1
print(pes_ideal)
#13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
altura = float(input('Digite a altura da pessoa: '))
pes_ideal = (72.7* altura) - 58.1
print(pes_ideal)
print()
#14-  João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso_peixe = float(input('Informe o peso dos peixes: '))
if peso_peixe < 50:
    print('Você não precisa pagar excesso.')
else:
    excesso = peso_peixe - 50
    multa = excesso*4
    print(f'Quantidade de kilos em excesso: {excesso: .2f}')
    print(f'Multa a pagar é de R$ {multa: .2f}')
print()
#16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area= float(input('Informe o tamanho da área a ser pintada em m^2: '))
tinta_necessaria= area/3
latas_resto= (tinta_necessaria//18)
latas= (tinta_necessaria/18)
preco_total = latas*80
if latas_resto>0:
    latas+=1
    resultado= int(latas)
    resultado2= (f'{preco_total:.2f}')
    print('latas necessárias: {}'.format(resultado))
    print('Valor total a pagar: {}'.format(resultado2))
else:
    print('latas necessárias: {}'.format(latas))
    print('Valor total a pagar: R${}'.format(resultado2))
print()
#17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 
#metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a 
#serem compradas e os respectivos preços em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
area = int(input('Digite o valor da area'))
latas = area / 6 
quantidade= latas /18
if latas % 18 <= 0:
    latas += 1
valor = quantidade * 80
galoes = latas / 3.6
if galoes % 3.6 != 0:
    galoes += 1
valor2 = galoes * 25

mistura_lata = int(latas / 18.0)
mistura_galao = int((latas - (mistura_lata * 18)) / 3.6)

if latas - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

    print('Apenas latas de 18 litros: %d' % latas, 'valor: %d' % valor)
    print('Apenas galões de 3.6 litros: %d' % galoes, 'valor: %d' % valor2)
    print('Mistura: %d latas e %d galoes = %.2f' % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))
print()
#18- Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
#usando este link (em minutos)
tamanho = float(input('Digite o tamanho do arquivo MB: '))
velocidade = float(input('Velocidade de Internet (MBps): '))
print('Tempo de download: %.0f Minutos ' %((tamanho / velocidade) * 60))