class conta_bancaria:
    def __init__(self, num_conta, nome_cliente, tipo_conta):
        self.num_conta = num_conta
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.saldo_conta = 0
        self.limite_Cheque_especial = 0
        self.status_conta = False

    def ativar_conta(self):
        if (self.status_conta == False):
            self.status_conta = True
            return "A conta está ativada!"
        else:
            return "A conta já está ativa!"

    def desativar_conta(self):
        if (self.status_conta == True) and (self.saldo_conta == 0):
            self.status_conta = False
            return "Conta desativada com sucesso!"
        elif (self.status_conta == False) and (self.saldo_conta == 0):
            return "A conta já está desativada."
        else:
            return "Para desativar a conta o saldo precisa ser de R$ 0,00."

    def deposito(self, valor_deposito):
        if (self.status_conta == True):
            self.saldo_conta += valor_deposito
            return "depoisito efetuado com sucesso"
        else:
            return "Deposito não realizado, conta desativada!"

    def saque(self, valor_saque):
        if self.status_conta == True:
            if self.saldo_conta > 0:
                if self.saldo_conta >= valor_saque:
                    self.saldo_conta -= valor_saque
                    return "Saque Efetuado com Sucesso"
                else:
                    return "Saque não realizado, verifique o seu saldo!"
            else:
                return "Você não tem Saldo suficiente para realizar essa transação."
        else:
            return "Saque não realizado, Conta Desativada!"
        
    def verificar_saldo(self):
        if (self.status_conta == True):
            return f"Saldo em conta: R$ {self.saldo_conta:.2f}"
        else:
            return "não foi possivel verificar o seu saldo, Conta desativada. por favor ative sua conta!"

    def cheque_especial(self, valor_cheque_especial):
            return "Você possui um valor em seu cheque especial!"

    def consultar_cheque_especial(self):
        return f"saldo chegue especial é: R$ {self.limite_Cheque_especial}"
cliente1 = conta_bancaria("0001", "Arthur", "Conta-Corrente")

print(cliente1.ativar_conta())
"""print(cliente1.desativar_conta())"""
print(cliente1.deposito(10))
print(cliente1.saque(20))
print(cliente1.verificar_saldo())
print(cliente1.cheque_especial(20))
