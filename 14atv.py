import os
def lp():
    os.system("cls")
lp()


def cm(n1):
    centimetros=n1* 100
    return centimetros


def resutado(cm):
    print(f"comversao de metros para sentimetros:{cm}")


metro=float(input("digite um numero em metros:"))    


selulas=cm(metro)




resutado(selulas)





