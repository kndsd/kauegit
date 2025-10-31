from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_LIVROS = 3
lista_livros = []

print("Solicitando dados dos livros.")
for i in range(QUANTIDADE_LIVROS):
    print(f"\nLivro {i + 1}:")
    livro = Livro(
        nome=input("Digite o nome do livro: "),
        autor=input("Digite o autor: "),
        categoria=input("Digite a categoria: "),
        preco=float(input("Digite o preço: "))
    )
    lista_livros.append(livro)

print("\nSalvando dados...")
arquivo = "catalogo_livros.txt"

with open(arquivo, "w", encoding="utf-8") as arquivo_livros:
    for livro in lista_livros:
        arquivo_livros.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, R${livro.preco:.2f}\n")

print("Dados salvos com sucesso no arquivo catalogo_livros.txt!")
