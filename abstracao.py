# Classes abstratas:
# são classe que não podem ser utilizadas para criar objetos,
# sendo utilizadas apenas como recurso de herança


from abc import ABC, abstractmethod

# Classe mãe abstrata
class Animal(ABC):

    @abstractmethod
    def som(self):
        pass

# Classe filha concreta
class Gato(Animal):
    def som(self):
        print('Miau Miau')


# Instância de Gato
tom = Gato()
tom.som()

# Erro ao instanciar Animal, pois o método som() é abstrato
#a = Animal()
#a.som()
