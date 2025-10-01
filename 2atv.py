import os
os.system("cls")

lista=[]

for i in range(4):  
   nota=int(input(f"notas {i+1}ª : "))
   lista.append(nota)


soma=sum(lista)
media=soma/4

for i in range(4):
    print(f"{i}° nota: {lista[i]}")
print(f"media final: {media}")

if media >= 7:
  print("aprovado")


elif media >= 5:
   print("recuperacao")

else:
   print("reprovado")    
