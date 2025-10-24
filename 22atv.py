import os 



def lip():
    os.system("cls")



lip()

from dataclasses import dataclass

@dataclass
class Cliente:
    nome:str
    cpf:str
    telefone:str
    def dados_entrega(self):
        print(f"cliente{i+1}")
        print(f"nome:{self.nome}")
        print(f"cpf:{self.cpf}")
        print(f"telefone:{self.telefone}")
    def maeket(self):
        print()
        print(f"telefone:{self.telefone}")
lisa_de_client=[]     
for i in range(3):
    dados_cliente=Cliente(nome=input("digite seu nome:\n"),
                          cpf=input("digite seu cpf:\n"),
                          telefone=input("digite seu numero:\n"))
    lisa_de_client.append(dados_cliente)

    lip()


for Cliente in lisa_de_client:
    Cliente.dados_entrega()    
    Cliente.maeket()

