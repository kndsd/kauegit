import os 
from dataclasses import dataclass
def lp():
    os.system("cls")


lp()
@dataclass
class autores:
    autor:str
    biografia:str
@dataclass
class livros:
    titulo:str
    ano:int
    autore:autores
    def buscar(self):
        print(f"nome do autor:{self.autore.autor}")
        print(f"biografia dele:{self.autore.biografia}")
        print(f"titulo:{self.titulo}")
        print(f"ano:{self.ano}")
    def escolhas():
      escolha=int(input("digite qual livro:"))
      match escolha:
        case 1:5
def tabela():            
    print("""codigo\ttitulo
      1\tgisia
      2\tcristina
      3\tlusimar
      4\trose


     """)


            


