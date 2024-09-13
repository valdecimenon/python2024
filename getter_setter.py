# Encapsulamento de dados: devemos esconder os dados da classe
# e para acessar devemos criar métodos especiais

# Getters and Setters
# Get = pegar => Getter = retorna uma variável privada
# Set = atribuir => Setter = altera uma variável privada

class Pessoa:
    def __init__(self, nome):
        # variável privada
        self.__nome = nome

    @property    #decorador getter
    def nome(self):
        return self.__nome

    @nome.setter #decorador setter
    def nome(self, nome):
        self.__nome = nome


# Teste
p = Pessoa("Bill Gates")
# inacessível
# print(p.__nome)

# método setter para alterar a variável privada
p.nome = 'Steave Jobs'

# método getter para acessar a variável privada
print(p.nome)