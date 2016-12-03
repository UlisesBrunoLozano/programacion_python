a=input("Introduzca los dias que viajo: ")
b=input("Introduzca las horas que viajo: ")
c=input("Introduzca los minutos que viajo: ")
d=input("Introduzca los segundos que viajo: ")
def funcion2(d,h,m,s):
    dias=a*86400
    horas=b*3600
    minutos=c*60
    segundos=d
    suma=dias+horas+minutos+segundos

    print ("Su viaje duro", suma, "segundos")
salida2=funcion2(a,b,c,d)
