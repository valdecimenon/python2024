# Classe é um modelo usado para criar um objeto
# método: é uma função dentro da classe
# Uma classe pode conter variáveis e métodos,
# podendo ser de INSTÂNCIA (self) ou da própria classe (static)

# As variáveis da classe podem ser:
# - públicas: acessível de qualquer lugar
# - privadas: acessível somente pela própria classe
# - protegido: similar ao privado, porém acessível pela subclasse

class Carro:

    # método construtor ou inicializador da classe
    def __init__(self, marca, modelo, preco):
        # variáveis de instância
        # Variáveis públicas
        self.marca = marca
        self.modelo = modelo
        # Variável privada
        self.__preco = preco

    # método de instância
    def descrever(self):
        return f'Carro: {self.marca} {self.modelo}'
    
    def mostraPreco(self):
        return f'{self.__preco}'
    

gol = Carro('VW', 'Gol 2018', 30000)
print(gol.descrever())
print('Marca:', gol.marca)
print('Modelo:', gol.modelo)
print('Preço: ', gol.mostraPreco())
    
palio = Carro('Fiat', 'Palio 2020', 35000)
print(palio.descrever())
print('Marca:', palio.marca)
print('Modelo:', palio.modelo)

