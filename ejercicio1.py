
vol1=float(input("ingrese el primer voltaje =\n "))
vol2=float(input("ingrese el primer voltaje =\n "))
vol3=float(input("ingrese el primer voltaje =\n "))
vol4=float(input("ingrese el primer voltaje =\n "))
vol5=float(input("ingrese el primer voltaje =\n "))     
prom=(vol1+vol2+vol3+vol4+vol5)/5
if prom > 220:
    print(f"ALTO VOLTAJE = {prom}")
else:
    print(f"VOLTAJE CORRECTO = {prom}")