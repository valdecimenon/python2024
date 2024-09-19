
class Conta:

    # construtor da classe
    def __init__(self, numero, titular, saldo, limite):
        print('Executando o construtor da conta...')
        # variáveis de instância privadas
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Conta n.: {self.__numero} Titular: {self.__titular} Saldo: {self.__saldo}')
    
    def depositar(self, valor):
        self.__saldo += valor

    # método privado: retorna um boleano (true ou false)
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            return True
        else:
            print(f'O valor {valor} passou do limite')
            return False
    
    def transferirPara(self, destino, valor):
        if (self.sacar(valor)):
            destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    # propriedade somente leitura
    @property
    def limite(self):
        return self.__limite
    
    # método para alterar o limite, usando =
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Método estático
    @staticmethod
    def codigo_banco():
        return "001"
    

    @staticmethod
    def codigos_bancos(banco):
        # dicionário
        bancos = {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
        return bancos[banco]


# Código principal
if __name__ == '__main__':
    conta1 = Conta(123, 'Rafael', 100, 1000)
    conta2 = Conta(456, 'Gabriel', 0, 1000)
    conta1.extrato()
    conta2.extrato()
    conta1.transferirPara(conta2, 50)
    conta1.extrato()
    conta2.extrato()

    # propriedades (getter)
    print('Saldo:', conta1.saldo)
    print('Limite:', conta1.limite)

    # setter
    conta1.limite = 2000
    print('Limite:', conta1.limite)

    print(Conta.codigo_banco())
    print(Conta.codigos_bancos('Caixa'))