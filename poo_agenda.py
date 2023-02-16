# POO - AGENDA

class Hora(object):
    def __init__(self,h = None,m = None,s = None):
        self.h = h
        self.m = m
        self.s = s
    
    def set_hora(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
        
    def __str__(self):
        return(("%02d" %self.h)+":"+("%02d" %self.m)+":"+("%02d" %self.s))
    
    
class Data(object):
    def __init__(self,dia = None,mes = None,ano = None):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def set_data(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def __str__(self):
        return(("%02d" %self.dia)+"/"+("%02d" %self.mes)+"/"+("%02d" %self.ano))
    
    
class Agenda(Data,Hora):
    def __init__(self,atv = None,dia = None,mes = None,ano = None,h = None,m = None,s = None):
        Data.__init__(self, dia, mes, ano)
        Hora.__init__(self, h, m, s)
        self.atv = atv
        
    def set_atv(self, atv):
        self.atv = atv
        
    def __str__(self):
        return Data.__str__(self) + " - "+ Hora.__str__(self)+"\n"+str(self.atv)
    
    
def Imprimir(L):
    for i in L:
        print(i)
    
    
# inputs    
n = int(input())
L = []

for i in range(0,n):
    d = int(input())
    m = int(input())
    a = int(input())
    h = int(input())
    mi = int(input())
    s = int(input())
    atv = input()
    #objeto
    trf = Agenda()
    trf.set_data(d, m, a)
    trf.set_hora(h, mi, s)
    trf.set_atv(atv)
    
    L.append(trf)
    
    
Imprimir(L)
