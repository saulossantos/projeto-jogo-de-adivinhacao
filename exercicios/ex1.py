'''5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: Alterar nome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''


class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido para saque.")


# Criando uma instância da classe ContaCorrente
conta = ContaCorrente("ContaCor1234", "João da Silva")

# Exibindo os atributos da conta
print("Número da conta:", conta.numero_conta)
print("Nome do correntista:", conta.nome_correntista)
print("Saldo:", conta.saldo)

# Alterando o nome do correntista
conta.alterar_nome("João Oliveira")
print("Novo nome do correntista:", conta.nome_correntista)

# Realizando um depósito
conta.deposito(1000)
print("Saldo após depósito:", conta.saldo)

# Realizando um saque
conta.saque(500)
print("Saldo após saque:", conta.saldo)