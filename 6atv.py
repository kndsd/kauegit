import os
os.system("cls")
numero= 0
lista= []
lista_par=[]
lista_inpar=[]

for i in range(5):
    numero = int(input(f"digite o {i + 1}ª numero : "))
    lista.append(numero)

    if numero >= 1:
         lista_par.append(numero)
         comtador_par= i + 1

    else:
         lista_inpar.append(numero)
         comtador_inpar= i + 1


soma=sum(lista_par)

print(f"lista de numeros pares: {lista_par}")
print(f"lista inpar:{lista_inpar}")
print(f"soma dos numeros pares:{soma}")

               





