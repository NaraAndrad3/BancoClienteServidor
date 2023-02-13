class Pessoa: 
    __slots__ = ['_nome','_cpf','_nascimento']
    def __init__(self, nome, cpf, nascimento):
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,n):
        self._nome = n
    
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,c):
        self._cpf = c
    
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self,nasc):
        self._nascimento = nasc
    
    def __repr__(self) -> str:
        return f'Nome completo: {self._nome}\nCPF: {self._cpf}\nNascimento: {self._nascimento}' 
