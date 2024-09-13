
# Exemplo de polimorfismo
# Métodos em diferentes classes tem o mesmo nome, porém 
# comportamentos diferentes

class Gato():
    def som(self):
        return "Miau"
    
class Cachorro():
    def som(self):
        return "Au Au"
    
def fazer_som(animal):
    print(animal.som())

# Testando
gato = Gato()
cachorro = Cachorro()

fazer_som(gato)
fazer_som(cachorro)