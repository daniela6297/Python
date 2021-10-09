#Esto es un comentario
import random
numero=random.randint(1,10)
cont=1
b=0
print(numero)
print("Estoy pensando un numero entre 1 y 10.Cual?") 
nro=int(input())

while numero != nro:
        print ("No es ese! Cual?? ")
        nro=input()
        nro=int(nro)
        cont=cont+1
        if (cont==6): 
            print("Ya wey...-_-...")
        if(cont>10):
            print("GAME OVER")
            b=1
            break

if(b!=1): print("Lo lograste!! En",cont,"intentos!!")

#if(cadena=="DANIELA"): print("PUSISTE DANIELA")
#else: print("No ingreso DANIELA")

