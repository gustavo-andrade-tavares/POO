# POO - TriAtleta

name = input()

class Atleta(object):
    def __init__(self,nome):
        self.nome = nome
    
    def get_nome(self):
        return(self.nome)
    
    def __str__(self):
        return(self.nome)
    
class Corredor(Atleta):
    def __init__(self,nome):
        Atleta.__init__(self, nome)
        
    def correr(self):
        return("Corredor "+Atleta.get_nome(self)+" correndo")
    
class Nadador(Atleta):
    def __init__(self,nome):
        Atleta.__init__(self, nome)
        
    def nadar(self):
        return("Nadador "+Atleta.get_nome(self)+" nadando")
    
class Ciclista(Atleta):
    def __init__(self,nome):
        Atleta.__init__(self, nome)
        
    def pedalar(self):
        return("Ciclista "+Atleta.get_nome(self)+" pedalando")
    
class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self,nome):
        Corredor.__init__(self, nome)
        Nadador.__init__(self, nome)
        Ciclista.__init__(self, nome)
        
    def __str__(self):
        return(Corredor.correr(self)+"\n"+Nadador.nadar(self)+"\n"+Ciclista.pedalar(self))
    
t = TriAtleta(name)
print(t)