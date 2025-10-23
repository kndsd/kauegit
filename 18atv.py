import os 



def lip():
    os.system("cls")



lip()

from dataclasses import dataclass

@dataclass
class pessoa:
    nome:str
    idade:int
    peso:int
    altura:float
pessoa1= pessoa("alice",30,65,1.80)
pessoa2= pessoa("bob",25,70,1.90)

print(f" nome:{pessoa1.nome}\n idade: {pessoa1.idade}\n peso:{pessoa1.peso}\n altura:{pessoa1.altura} ")
print(f" nome:{pessoa2.nome}\n idade: {pessoa2.idade}\n peso:{pessoa2.peso}\n altura:{pessoa2.altura} ")