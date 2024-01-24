
vol1=float(input("ingrese el primer voltaje =\n "))
vol2=float(input("ingrese el primer voltaje =\n "))
vol3=float(input("ingrese el primer voltaje =\n "))

prom=(vol1+vol2+vol3)/3

if prom<115: 
    print(f"el promedio de los voltajes es = {prom} VOLTAJE CORRECTO! ")
elif prom>115 and prom<220:
    print(f"el promedio de los voltajes es = {prom} ALTO VOLTAJE")
elif prom>220:
    print(f"el voltaje supera los 220v  actualmente estas expuesto a = {prom} PELIGRO! ")
    