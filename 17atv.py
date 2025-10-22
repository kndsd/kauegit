import os 



def lip():
    os.system("cls")



lip()

from dataclasses import dataclass

@dataclass
class pessoa:
    nome:str
    idade:int
    cpf=str
pessoa1= pessoa("alice",30)
pessoa2= pessoa("bob",25)

print(f"nome:{pessoa1.nome}\n idade: {pessoa1.idade} ")
print(f"nome:{pessoa2.nome}\n idade: {pessoa2.idade} ")

