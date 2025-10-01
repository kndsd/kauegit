import os
os.system("cls")

lista=[]

for i in range(3):  
   nota=int(input(f"notas {i+1}ª : "))
   lista.append(nota)


soma=sum(lista)
media=soma/3

for i in range(3):
    print(f"{i}° nota: {lista[i]}")
print(f"media final: {media}")


 
