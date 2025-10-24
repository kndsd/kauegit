import os 
from dataclasses import dataclass
def linpesa():
    os.system("cls")


linpesa()

@dataclass
class enderereso:
    logadouro:str
    numero:int
    sidade:str
@dataclass
class cliente:
    nome:str
    cpf:str
    email:str
    enderereso1:enderereso
    def dados_do_cliente(self):
        print(".................................................")
        print("dados dos clientes")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(F"nome:{self.nome}")    
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"cpf:{self.cpf}")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"e-mail:{self.email}")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"endereso:{self.enderereso1.logadouro}")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"numero:{self.enderereso1.numero}")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"sidade:{self.enderereso1.sidade}")
quantidade=int(input("quantos cadastros deseja adicionar:"))
linpesa() 

for i in range(quantidade):
    print(";;;;;;;;;;;;;;;;;;;;;;")
    print(f"cliente {i+1} ")
    nome=input("degite o nome:")
    

