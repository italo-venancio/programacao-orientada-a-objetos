class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def deposita(self, valor):
        self.saldo += valor
        
    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:    
            self.saldo -= valor
            return True
    
    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        print("titular: {}".format(self.titular))
    
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == false):
            return False
        else:
            destino.deposita(valor)
            return True
        
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def __srt__(self):
        return (f"nome: {self.nome}, sobrenome: {self.sobrenome}, cpf: {self.cpf}")

def main():
    cl1 = Cliente("italo", "venancio", 12345678901)
    co1 = Conta("01", cl1, 10.0, 100.0)
    print(co1.extrato())

if __name__ == "__main__":
    
    main()     
