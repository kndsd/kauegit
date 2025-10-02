
import os
os.system("cls")


pares = 0
impares = 0
lista=[]
for i in range(6):  
   numero=int(input(f"numero {i+1}ª : "))
   lista.append(numero)


   if numero % 2 == 0:
     pares += 1
     
   else:
    impares += 1

print ("")