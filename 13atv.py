import os

# Função se
def limpa_tela():
    
    os.system("cls")




def media (n1,n2):
    calculo= (n1 + n2) / 2
    return calculo 


def mostrar(media):
    print(f"resutado :{media}")
    if media >= 7 :
        print("aprovado")
    else:
        print("reprovado")
limpa_tela()

numero1=int(input("digite um numero:"))

numero2=int(input("digite segundo numero:"))

media1= media(numero1,numero2)

mostrar(media1)

