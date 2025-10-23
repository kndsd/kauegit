import os 



def lip():
    os.system("cls")



lip()

from dataclasses import dataclass

@dataclass
class pessoa:
    nome:str
    email:str
    endereso:str
    def dados_entrega(self):
        print(f"nome:{self.nome}")
        print(f"endereso:{self.endereso}")
    def maeket(self):
        print(f"nome:{self.nome}")
        print(f"nome:{self.email}")
        
pessoa1=pessoa( nome=input("digite seu nome:"),
                email=str(input("digite seu e-mail:")),
                endereso=str(input("digite seu endereso")))
               
pessoa1.dados_entrega()
pessoa1.maeket()
