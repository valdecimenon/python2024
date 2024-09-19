# Para fazer herança usamos a regra: É UM
# a palavra "super" é usada pela classe filha, para acessar variáveis
# e métodos NÃO privados da classe mãe

# Classe mãe ou superclasse
class Veiculo:
    # inicializador ou construtor
    def __init__(self, cor):
        self.cor = cor

    def mover(self):
        print('O veículo está se movendo')


# Classe filha ou subclasse
class Carro(Veiculo):   # Carro (É UM Veiculo)

    def __init__(self, cor, marca):
       # chama o construtor da classe mãe, passando a cor
       super().__init__(cor)
       self.marca = marca
    

bmw = Carro('Azul', "BMW")
print('Cor do carro:', bmw.cor)
bmw.mover()


