#!/usr/bin/env python
#-------------------------------------------------------

def altura_rectangulo(x):
    return 1/(1 + x**2)

# funcion que calcula la altura de cada rectangulo que se va a sumar
#------------------------------------------------------
def simpson(Lim_a, Lim_b ,n_rectangulo, altura,arg_fun):
    ancho_rect = (Lim_b - Lim_a) / n_rectangulo
    arg_fun = ancho_rect/2
    result = 0                                    # acumulador
    for i in range (n_rectangulo):
        result+= ancho_rect*altura
        arg_fun+= ancho_rect

    return 4*result

#---------------------------------------------------------

#-------------Bloque principal---------------------------
extremo1=0
extremo2=1
rectangulos = 300000
ancho_rect = (extremo2 - extremo1) / rectangulos
arg_fun = ancho_rect/2
x = simpson(extremo1,extremo2,rectangulos,altura_rectangulo(arg_fun),arg_fun)
print(f"El valor aprox de pi es: {x}")
