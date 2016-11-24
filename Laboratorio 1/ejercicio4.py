entrada2=input("Introduzca el tiempo que paso viajando en dias, horas, minutos y segundos ")
def funcion2(d,h,m,s):
    suma=0
    listax=[d,h,m,s]
    listay=[e for e in listax]
    for e in listay:
        listay[0]=e*86400
        listay[1]=e*3600
        listay[2]=e*60
        listay[3]=e
    for e in listay:
        suma=suma+e
        return suma

salida2=funcion2(entrada2)
print salida2
