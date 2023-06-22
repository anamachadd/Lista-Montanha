# 1- Classe Bola: Crie uma classe que modele uma bola:
# a) Atributos: Cor, circunferência, material
# b) Métodos: trocaCor e mostraCor

class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor= cor
        self.circunferencia= circunferencia
        self.material= material
    def trocaCor (self,cor):
        self.cor= cor

    def mostraCor (self):
        return self.cor
     
bolaA= bola('rosa', 10 ,'fibra')
print(bolaA.mostraCor())
bolaA.trocaCor('cinza')
print(bolaA.mostraCor())
print()
# 2- Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
     def __init__(self, lado):
        self.lado= lado
    
     def mudaValor (self,valor):
        self.valor= valor

     def mostraValor (self):
        return self.valor

     def calculoArea (self):
        return self.lado*self.lado

qA= Quadrado(24)

print(qA.calculoArea())
print()
# 3- Classe Retangulo: Crie uma classe que modele um retangulo:
#a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, 
# deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def trocarValorbase(self, base):
        self.nova__base = base

    def trocarValoraltura(self, altura):
        self.nova__altura = altura

    def retornaValorbase(self):
        return self.base

    def calculoArea(self):
        return self.base*self.altura

    def calculoPerimetro(self):
        return self.base+self.base+self.altura+self.altura

bas= int(input('Informe o valor da base do retangulo'))
alt= int(input('Informe o valor da altura do retangulo'))
r1= Retangulo(bas,alt)
print('A área é: ', r1.calculoArea())
print('O perímetro é: ', r1.calculoPerimetro())
print()
#4- Classe Pessoa: Crie uma classe que modele uma pessoa:
#a) Atributos: nome, idade, peso e altura
#b) Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela
# menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome= nome
        self.idade= idade
        self.peso= peso
        self.altura= altura

    def envelhecer (self,anos):
        self.idade +=anos
        if self.idade <21:
           self.cresce(anos)

    def crescer (self, anos):
        if self.idade <21:
           self.altura += 0.5 * anos

    def engordar (self, peso):
        self.peso += peso

    def emagrecer (self, peso):
        self.peso -= peso

    def altura (self):
        self.altura += altura

y= Pessoa("Aline", 16, 68, 1.68)
print(y.nome)
print(y.idade)
print(y.peso)
print(y.altura)
print()
#5- Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
#Os métodos são os seguintes: alterarNome, depósito e saque; 
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatório
print()
#6- Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
import time

class televisor:
    def __init__(self, canal="1", volume="50"):
        self.canal = canal
        self.volume = volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num > 0 and num <= 150:
                self.__canal = num
            else:
                print("Canal Inválido")

        else:
            print("O canal deve ser apenas números!")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 0 and num <= 100:
                self.__volume = num
            else:
                print("O volume deve ser entre 0 e 100")

        else:
            print("O volume deve ser apenas números!")


    def mudaCanal(self):
        num = input("Mudar para CANAL: ")
        self.canal = num

    def mudaVolume(self):
        num = input("Mudar para VOLUME: ")
        self.volume = num

    def __str__(self):
        return "CANAL: {} \nvolume: {}\n ".format(self.canal, self.volume)

def main():
    tv01 = televisor()

    while True:
        print("\n"*40)
        print(tv01)

        print("opções ---------")
        print("1 - mudar canal")
        print("2 - mudar volume")
        print("3 - desligar\n ---------------")
        selec = input("Selecionar:")

        if selec == "1":
            tv01.mudaCanal()

        elif selec == "2":
            tv01.mudaVolume()

        elif selec == "3":
            print("Desligando ...")
            break

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)

main()
print()
#7 -Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#A. Atributos: Nome, Fome, Saúde e Idade 
#b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. 
class BichinhoVirtual:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    self.__hunger = 100
    self.__health = 100

  def get_name(self):
    return self.__name

  def set_name(self, new_name):
    self.__name = new_name

  def get_age(self):
    return self.__age

  def set_age(self, new_age):
    self.__age = new_age

  def get_hunger(self):
    return self.__hunger

  def set_hunger(self, new_hunger):
    self.__hunger = new_hunger

  def get_health(self):
    return self.__health

  def set_health(self, new_health):
    self.__health = new_health

  def get_humor(self):
    if self.get_hunger() >= 70 and self.get_health() >= 70:
      return "EU ESTOU FELIZ!"

    elif self.get_hunger() >= 50 and self.get_health() >= 50:
      return "NÃO SOU TÃO BOM !"

    elif self.get_hunger() >= 30 and self.get_health() >= 30:
      return "OI MUITA FOME!"

    else:
      return "EU QUERO COMER !"

bichinho = BichinhoVirtual("TOBY", 4)

print( bichinho.get_name() )
print( bichinho.get_age() )
print( bichinho.get_humor() )

bichinho.set_health(30)
bichinho.set_hunger(70)

print( bichinho.get_humor() )
print()
#8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida): 
        self.bucho.append(comida)

    def verBucho(self):
        print(f'O bucho do Macaco {self.nome} possui dentro dele:\n {self.bucho}')

    def digerir(self):
        comida_permitida = ['banana','pera','manga']
        for i in range(len(self.bucho)):
            if self.bucho[i] in comida_permitida:
                print(f'O item {self.bucho[i]} foi digerido no bucho do Macaco {self.nome}')
            else:
                print(f'O item {self.bucho[i]} não foi digerido no bucho do Macaco {self.nome}, ele o vomitou')

Macaco1 = Macaco('Xita') 
Macaco2 = Macaco('Mamaco') 

Macaco1.comer('abacaxi')
Macaco1.comer('limão')
Macaco1.comer('pera')
Macaco1.verBucho()
Macaco1.digerir()
print('\n')
Macaco2.comer('banana')
Macaco2.comer('laranja')
Macaco2.comer('manga')
Macaco2.comer(Macaco1) 
Macaco2.verBucho()
Macaco2.digerir()
print()
#9 - Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
#Possua uma classe chamada Ponto, com os atributos x e y.
#Possua uma classe chamada Retangulo, com os atributos largura e altura.
#Possua uma função para imprimir os valores da classe Ponto
#Possua uma função para encontrar o centro de um Retângulo.
#Você deve criar alguns objetos da classe Retangulo.
#Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
#A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
#O valor do centro do objeto deve ser mostrado na tela
#Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self): 
        if self.largura %2 == 1 and self.altura %2 == 1:
            larguraCentro = (self.largura /2) + 0.5
            alturaCentro = (self.altura /2) + 0.5
            print(f'\nO centro do retangulo está na posição:\nLargura: {larguraCentro:.0f}\nAltura: {alturaCentro:.0f}')
        else:
            print(f'\Impossivel achar o centro pois os valores não são impares')

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimirPonto(self):
        if self.x == 0 or self.y == 0:
            p = Ponto.pontoPartida(self)
            print(f'\nO ponto está na posição inicial:\nLargura: {p[0]}\nAltura: {p[1]}')
        else:
            print(f'\nO ponto está na posição:\nLargura: {self.x}\nAltura: {self.y}')

    def pontoPartida(self):
        larguraInicial = 2
        alturaInicial = self.y - 1
        print(f'\nO ponto está na posição inicial:\nLargura: {larguraInicial}\nAltura: {alturaInicial}')
        inicioPonto = [larguraInicial, alturaInicial]
        return inicioPonto  
quad1 = Retangulo(7,5)
quad1.encontrarCentro()

quad1 = Ponto(5,6)
quad1.imprimirPonto()
quad1.pontoPartida()
print()
#10 - Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)
bomba1 = BombaCombustivel('Gasolina', 7.50, 1000)
bomba1.abastecerPorLitro(100)
print(f'A quantidade na bomba é: {bomba1.quantidadeCombustivel:.2f} litros')
bomba1.abastecerPorValor(100)
print(f'A quantidade na bomba é: {bomba1.quantidadeCombustivel:.2f} litros')
print()
#12 - Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))
conta = ContaInvestimento(12345678, 'Joaquim', 10)
conta.deposito(1000)
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
print()
# 13 - Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario
func1 = Funcionario('MACHADO, ANA', 1150.90)
print (f'Nome: {func1.getNome()}')
print (f'Salario: R$ {func1.getSalario():.2f}')
print()
#14 - Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)
ana = Funcionario("ana", 25000)
ana.aumentarSalario(10)
print (f'Nome: {ana.getNome()}')
print (f'Salario: R$ {harry.getSalario():.2f}')
print()
# 15- Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude

    def alt_Idade(self, Idade):
        self.Idade = Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
    #tambem é possivel inserir um valor de pontuação no nivel do humor como no enunciado

    def DarComida(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Fome -= self.Fome * (Quantidade / 100.0)

    def brincar(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Saude += self.Saude * (Quantidade / 100.0)
dino = Tamagushi('Toby')
dino.alt_Nome('estrela')
dino.alt_Fome(9)
dino.alt_Saude(5)
dino.alt_Idade(10)
dino.DarComida(50)
dino.brincar(8)

print('Nome:',dino.Nome)
print(dino.Fome,'de fome')
print(dino.Saude,'de saúde')
print(dino.Idade,'anos')
print('O bichinho',dino.CheckHumor())
print()
#16 - Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.alt_Nome(Nome)
        self.alt_Fome(Fome)
        self.alt_Saude(Saude)
        self.alt_Idade(Idade)

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def get_Nome(self):
        return self.Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def get_Fome(self):
        return self.Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude

    def get_Saude(self):
        return self.Saude

    def alt_Idade(self, Idade):
        self.Idade = Idade

    def get_Idade(self):
        return self.Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
    def get_Humor(self):
        return self.get_Fome() * self.get_Saude()

    def DarComida(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Fome -= self.Fome * (Quantidade / 100.0)

    def brincar(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Saude += self.Saude * (Quantidade / 100.0)

    def str(self):
        print('\n--STATUS--')
        print('Nome:', self.get_Nome())
        print('Idade:', self.get_Idade())
        print('Fome:', self.get_Fome())
        print('Saude:', self.get_Saude())
        print('Humor:', self.get_Humor())
dino = Tamagushi('Toby')
dino.alt_Nome('estrela')
dino.alt_Fome(9)
dino.alt_Saude(5)
dino.alt_Idade(10)
dino.DarComida(50)
dino.brincar(8)

print('Nome:',dino.Nome)
print(dino.Fome,'de fome')
print(dino.Saude,'de saúde')
print(dino.Idade,'anos')
print('O bichinho',dino.CheckHumor())
dino.str()
