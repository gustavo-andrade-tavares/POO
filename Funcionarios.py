# POO - funcionarios
from abc import ABC, abstractmethod

class Pessoa(object):
    __nome: str
    __endereco: str
    __codigo: int
    def __init__(self,cod = None, nome = None, end = None):
        self.__codigo = cod
        self.__nome = nome
        self.__endereco = end
    
    def set_nome(self,nome):
        self.__nome = nome
        
    def get_nome(self):
        return(self.__nome)
    
    def set_cod(self,cod):
        self.__codigo = cod
        
    def get_cod(self):
        return(self.__codigo)
    
    def set_end(self,end):
        self.__endereco = end
        
    def get_end(self):
        return(self.__endereco)
    
    def __str__(self):
        return(str(self.__codigo)+" "+self.__nome+" "+ self.__endereco)
    

class Funcionario(Pessoa, ABC):
    __salario_base: float
    def __init__(self,cod = None, nome = None, end = None, salario_base = None):
        Pessoa.__init__(self, cod, nome, end)
        self.__salario_base = salario_base
        
    def set_salario_base(self,salario_base):
        self.__salario_base = salario_base
        
    def get_salario_base(self):
        return(self.__salario_base)
    
    @abstractmethod
    def get_total_recebido(self):
        pass
    
class Clt(Funcionario):
    __vale_transporte: float
    __vale_alimentacao: float
    def __init__(self,cod = None, nome = None, end = None, salario_base = None,vale_transporte = None,vale_alimentacao = None):
        Funcionario.__init__(self, cod, nome, end, salario_base)
        self.__vale_transporte = vale_transporte
        self.__vale_alimentacao = vale_alimentacao
        
    def set_vt(self,vale_transporte):
        self.__vale_transporte = vale_transporte
        
    def set_va(self,vale_alimentacao):
        self.__vale_alimentacao = vale_alimentacao
        
    def get_vt(self):
        return(self.__vale_transporte)
    
    def get_va(self):
        return(self.__vale_alimentacao)
    
    def get_total_recebido(self):
        return(Funcionario.get_salario_base(self) + self.__vale_transporte + self.__vale_alimentacao)
    
    def __str__(self):
        s = ("Tipo: Clt"+"\nNome: "+Pessoa.get_nome(self)+"\nEndereco: "+
             Pessoa.get_end(self)+"\nSalario Base: "+str(Funcionario.get_salario_base(self))+
             "\nTransporte: "+str(Clt.get_vt(self))+"\nAlimentacao: "+str(Clt.get_va(self))+
             "\nTotal Recebido: "+str(Clt.get_total_recebido(self)))
        return(s)
    

class Comissionado(Funcionario):
    __vendas: int
    __comissao: float
    def __init__(self,cod = None, nome = None, end = None, salario_base = None, vendas = None, comissao = None):
        Funcionario.__init__(self, cod, nome, end, salario_base)
        self.__vendas = vendas
        self.__comissao = comissao
        
    def set_vendas(self,vendas):
        self.__vendas = vendas
        
    def get_vendas(self):
        return(self.__vendas)
    
    def set_comissao(self,comissao):
        self.__comissao = comissao
        
    def get_comissao(self):
        return(self.__comissao)
    
    def get_total_recebido(self):
        tr = Funcionario.get_salario_base(self) + (Comissionado.get_vendas(self) * Comissionado.get_comissao(self))
        return(tr)
    
    def __str__(self):
        s = ("Tipo: Comissionado"+"\nNome: "+Pessoa.get_nome(self)+"\nEndereco: "+
             Pessoa.get_end(self)+"\nSalario Base: "+str(Funcionario.get_salario_base(self))+
             "\nVendas: "+str(Comissionado.get_vendas(self))+
             "\nComissao: "+str(Comissionado.get_comissao(self))+
             "\nTotal Recebido: "+str(Comissionado.get_total_recebido(self)))
        return(s)
    
def acessa_cd(p):
    return(p.get_cod())

def imprime(L):
    L.sort(key = acessa_cd)
    for o in L:
        print(o,"\n")
        
#inputs
N = int(input())
V = []
for i in range(0,N):
    tipo = int(input())
    codigo = int(input())
    nome = input()
    endereco = input()
    sb = float(input())
    if(tipo == 1):
        vale_t = float(input())
        vale_a = float(input())
        f1 = Clt()
        f1.set_cod(codigo)
        f1.set_nome(nome)
        f1.set_end(endereco)
        f1.set_salario_base(sb)
        f1.set_vt(vale_t)
        f1.set_va(vale_a)
        V.append(f1)
    else:
        nro_vendas = int(input())
        comissao = float(input())
        f2 = Comissionado()
        f2.set_cod(codigo)
        f2.set_nome(nome)
        f2.set_end(endereco)
        f2.set_salario_base(sb)
        f2.set_vendas(nro_vendas)
        f2.set_comissao(comissao)
        V.append(f2)
        
    

imprime(V)
