import os 
from dataclasses import dataclass
def linpesa():
    os.system("cls")


linpesa()


@dataclass
class cliente:
    nome:str
    idade:int
    peso:float
    altura:float
    def dados_do_cliente(self):
        print(".................................................")
        print("dados dos clientes")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(F"nome:{self.nome}")    
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"idade:{self.idade}")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"peso:{self.peso}")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print(f"autura:{self.altura}")
       
       



for i in range(4):
    print(";;;;;;;;;;;;;;;;;;;;;;")
    print(f"cliente {i+1} ")
    nome=input("degite o nome:")
    idade=input("sua idade:")
    peso1=input("seu peso:")
    altura1=input("sua autura")
    