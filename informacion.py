#programa en phyton que lea la altura y la anchura de un rectangulo y atravez de una funcion dibuje el rectangulo con asteriscos
def dibujar_rectangulo_relleno(altura, anchura):
    for i in range(altura):
        print('*' * anchura)

try:
    altura = int(input("Introduce la altura del rectángulo: "))
    anchura = int(input("Introduce la anchura del rectángulo: "))

    if altura <= 0 or anchura <= 0:
        print("La altura y la anchura deben ser números enteros positivos.")
    else:
        dibujar_rectangulo_relleno(altura, anchura)
except ValueError:
    print("Por favor, introduce números enteros válidos para la altura y la anchura.")
# presione enter para pasar al siguiente punto
input("Presiona Enter para salir...")

#programa en phyton funcion dibuje el rectangulo con asteriscos
def dibujar_rectangulo_relleno(a):
    for k in range(1,a+1):
        for j in range(k):
            print("*" , end = " ")
        print(" ")
    pintaparteinterior

def pintar_parte_interior(a):
    for k in range(1,a):
        for j in range(a-1,1):
             print("* ",end = " ")
    print(" ")
