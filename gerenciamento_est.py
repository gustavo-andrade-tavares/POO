# Gerenciamento de Estudantes
L = []

class Aluno(object):
    def __init__(self,ident = None,nome = None,curso = None,idade = None):
        self.ident = ident
        self.nome = nome
        self.curso = curso
        self.idade = idade
    
    def set_nome(self,nome):
        self.nome = nome
        
    def set_ident(self, ident):
        self.ident = ident
        
    def set_curso(self, curso):
        self.curso = curso
        
    def set_idade(self, idade):
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def get_ident(self):
        return self.ident
    
    def get_curso(self):
        return self.curso
    
    def get_idade(self):
        return self.idade
    
    def __str__(self):
        s = ("Nome: "+self.nome+"\nCurso: "+self.curso+
             "\nN USP: "+str(self.ident)+"\nIDADE: "+str(self.idade))
        return(s)
 
#inputs
while True:
    num = int(input())
    if(num == -1):
        break
    nome = input()
    curso = input()
    idade = int(input())
    A = Aluno()
    A.set_ident(num)
    A.set_nome(nome)
    A.set_curso(curso)
    A.set_idade(idade)
    L.append(A)
    
#inputs operacoes
V = []
while True:
    op = int(input())
    if(op == -1):
        break
    elif(op == 1):
        n = int(input())
        V.append([op,n])
    elif(op == 2):
        c = input()
        V.append([op,c])
    else:
        V.append([op,0])


#Aluno com determinado numero    
def operacao_1(L,num):
    for i in L:
        if(i.get_ident() == num):
            print(i,"\n")
            break
        else:
            continue
             
#Alunos de determinado curso
def operacao_2(L,c):
    A = []
    for i in L:
        if(i.get_curso() == c):
            A.append(i)
        else:
            continue
    if len(A) != 0:
        for o in A:
            print(o,"\n")
    
def operacao_3(L):
    for i in L:
        print(i,"\n")

      
#chamada das operacoes
for j in range(len(V)):
    if(V[j][0] == 1):
        operacao_1(L, V[j][1])
    elif(V[j][0] == 2):
        operacao_2(L, V[j][1])
    else:
        operacao_3(L)


