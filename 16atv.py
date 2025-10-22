import os 



def lip():
    os.system("cls")



lip()

def cauculo():
    peso=float(input("digite seu peso:"))
    autura = float(input("digite sua autura:"))
    imc= peso / (autura * autura)
    return imc


def  situasa(n1):
    if n1 < 18.5:
        return "peso baixo"
    
    if 18.5 <= n1 < 25:
     return "peso medio"
