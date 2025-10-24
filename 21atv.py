import os 
from dataclasses import dataclass

def lip():
    os.system("cls")


lip() 

@dataclass
class cliente:
    nome:str
    endereso:str
    telefome:str

    def mostrar_dados_do_cliente(self):
        print(f"nome:{self.nome}")
        print(f"endereço:{self.endereso}")
        print(f"telefone:{self.endereso}")
        

lisa_de_clientes=[]



for i in range(3):
    dados_cliente=cliente(nome=input("digite seu nome:"),
                          endereso=input("digite seu endereso:"),
                          telefome=input("digite seu numero:"))
    lisa_de_clientes.append(dados_cliente)
    lip()



for cliente in lisa_de_clientes:
    cliente.mostrar_dados_do_cliente()

                        