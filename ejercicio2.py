
base=float(input("ingrese la base del triangulo = \n"))
altura=float(input("ingrese la altura del triangulo = \n"))

area=(base*altura)/2

if area>1000:
    print("el area del triangulo es = \n",area)
    print(f"el area es mayor de 1000  DATOS INVALIDOS ")
else:
    print(f"el area del triangulo equilatero es = {area}")         
        