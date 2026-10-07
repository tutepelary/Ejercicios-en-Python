a = 10
b = 20

#Operadores de comparacion 
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

################################
edad = int(input("Edad: "))
if edad >= 18:
        print("Mayor de edad")
else:
        print("Menor de edad")

#################################################
temperatura = float(input("Temperatura: "))
if temperatura < 20:
        print("Temperature baja")
elif temperatura < 30:
        print("Temperatura Normal")
else:
        print("Temperatura alta")