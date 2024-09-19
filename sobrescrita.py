# Sobrescrita ocorre quando a subclasse redefine um método herdado da classe mãe

class Animal:
    def som(self):
        return "Animal faz som..."
    

class Gato(Animal):
    # Este método foi redefindo (sobrescrito), pois tem o mesmo nome do
    # método herdado de Animal
    def som(self):
        return "Gato miando..."
    
animal = Animal()
gato = Gato()

print(animal.som())
print(gato.som())