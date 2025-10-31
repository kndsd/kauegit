import os
from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    telefone:int
    emeil:str
QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        telefone=int(input("seu telefone:")),
        emeil=str(input("seu emeil:"))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade},{aluno.telefone}{aluno.emeil}\n")

print("Salvo com sucesso.")
