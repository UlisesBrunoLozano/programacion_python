#Ejercicio 5 Tarea 3
#Ulises Bruno Lozano
#29/11/2016
a=raw_input("Introduzca su nombre: ")
def vocalconsonante(x):
    x=a
    b=str(x)

    if b[0]=="A" or b[0]=="E" or b[0]=="I" or b[0]=="O" or b[0]=="U":
        print ("Vocal")
    else:
        print ("Consonante")

output=vocalconsonante(a)
