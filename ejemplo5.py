'''

contador = 0 
while contador < 10:
    print(contador)
    #contador += 1

'''

while True:
    numero = int(input("numero: "))
    if numero == 0:
        break
    print("Ingresaste el numero: ", numero)

'''
La instruccion break detiene y sale del bucleo por completo de manera inmediata.
El programa salta de inmediato a la primera linea de codigo que esta fuera del bucle 

continue

for i in range(10):
    print(i)
'''
''' 
for i in range(1,6):
    if i == 3:
        continue
    print(numero)
    La instruccion continue salta el resto del codigo de la iteracion actual y pasa directamentea
    la siguiente repeticion del bucle. No detiene el bucle completamente
    '''