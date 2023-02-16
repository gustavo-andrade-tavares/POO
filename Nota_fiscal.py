# POO - Nota Fiscal

class Produto(object):
    def __init__(self,C = None,vu = None):
        self.C = C
        self.vu = vu
        
    def set_codigo(self,C):
        self.C = C
    
    def set_v_u(self,vu):
        self.vu = vu
    
    def get_C(self):
        return(self.C)
    
    def get_vu(self):
        return(self.vu)
    
    def __str__(self):
        return(str(self.C)+" "+str(self.vu))
    
class Nota_Fiscal(Produto):
    def __init__(self,C = None,vu = None,q = None):
        Produto.__init__(self, C, vu)
        self.q = q
        
    def set_q(self, q):
        self.q = q
        
    def get_q(self):
        return(self.q)
        
    def get_total(self):
        return(self.q * Produto.get_vu(self))
    
    def __str__(self):
        s = ("#"+str(Produto.get_C(self))+":"+"    "+str(self.q)+"  "+
             "%.2f" %(Produto.get_vu(self))+" "+"%.2f" %(self.q * Produto.get_vu(self)))
        return(s)
    
def get_qt(p):
    return(p.C)

def compra(P,Cmp):
    L = []
    for o in P:
        cd = o.get_C()
        vu = o.get_vu()
        qtd = Cmp[cd]
        item = Nota_Fiscal()
        item.set_codigo(cd)
        item.set_v_u(vu)
        item.set_q(qtd)
        L.append(item)
        
    L.sort(key = get_qt)
    return(L)

def imprime_nota(V):
    total = 0
    print("#COD QTD VL_UN R$")
    for o in V:
        total += o.get_total()
        print(o)
    print("Total: R$ %.2f" %total)
    

def produtos_comprados(P,D):
    P_c = []
    for k in D:
        for o in P:
            if(k == o.get_C()):
                P_c.append(o)
                break
            else:
                continue
    return(P_c)
 

#inputs
P = []

Comprados = {}


n = int(input())
for i in range(0,n):
    cod,v = input().split()
    cod,v = int(cod), float(v)
    obj = Produto()
    obj.set_codigo(cod)
    obj.set_v_u(v)
    P.append(obj)
  
    
cp = int(input())
for i in range(0,cp):
    cd,qu = input().split()
    cd,qu = int(cd), int(qu)
    if cd not in Comprados:
        Comprados[cd] = qu
    else:
        Comprados[cd] += qu

        
#chamada das funçoes
L1 = produtos_comprados(P, Comprados)
L2 = compra(L1, Comprados)

imprime_nota(L2)



