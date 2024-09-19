# Sobrecarga ocorre quando temos métodos, na mesma classe, com nomes iguais,
# porém assinaturas diferentes:
# Exemplo de assinaturas:
#   somar(a)
#   somar(a, b)
#   somar(a, b, c)

class Calculadora:
    def somar(self, a, b=0, c=0):
        return a + b +c
    
calc = Calculadora()

print(calc.somar(1))
print(calc.somar(1, 2))
print(calc.somar(1, 2, 3))