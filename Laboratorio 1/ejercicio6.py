peso=input("kilogramos")
altura=input("metros")
def masacorporal(peso, altura):
  return peso/altura**altura
if masacorporal<16:
    print "Delgadez"
elif masacorporal<99 and
        masacorporal>16:
elif masacorporal>16 and
        masacorporal<19.99
        print "Delgadez moderada"
elif masacorporal>17 and
        masacorporal<18.49
        print "Delgadez leve"
elif masacorporal>18.5 and
        masacorporal<24.99
        print "Normal"
elif masacorporal>25 and
        masacorporal<30
        print "Sobrepeso"
elif masacorporal>30 and
        masacorporal<40
        print "Obesidad"
elif masacorporal>40
        print "Obesidad morbida"
