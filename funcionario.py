from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    @abstractmethod
    def autenticar(user:str, senha:int):
        pass

    def __str__(self):
        info = (f'Nome: {self.nome}\n'
                f'CPF: {self.cpf}\n')
        return info

class Gerente(Funcionario):
    
    def autenticar(self, user:str, senha:int):
        if user == self.cpf and senha == self.get_senha():
            return True
        else:
            return False

    def cancelar_operador(self):
        return 'operacao cancelada'

class Operador_Caixa(Funcionario):

    def __init__(self, nome: str, cpf: str, senha: int, numero_caixa: int):
        super().__init__(nome, cpf, senha)
        self.numero_caixa = numero_caixa

    def autenticar(self, user:str, senha:int):
        if user == self.numero_caixa and senha == self.get_senha():
            return True
        else: 
            return False

    def registrar_produto(self):
        return 'produto registrado'

class Seguranca(Funcionario):

    def __init__(self, nome: str, cpf: str, senha: int, posto: int):
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def autenticar(self, user:str, senha:int):
        if user == self.posto and senha == self.get_senha():
            return True
        else:
            return False

    def acionar_alarme(self):
        return 'Uooooooooouuuuooooouuuoouuuu!'

