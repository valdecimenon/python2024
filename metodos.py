# Métodos estáticos
# Obviamente todos os métodos são declarados dentro da classe,
# porém existem dois tipos:
# - Método de instância: é executado a partir do objeto
# - Método estático: é executado a partir da classe, pois não precisam
#   de objetos.

class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b
    

# Testes
x = Calculadora.somar(1, 2)
y = Calculadora.subtrair(2, 1)

print(x, y)

calc = Calculadora()
z = calc.somar(3, 4)
print(z)