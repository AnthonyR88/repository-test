# 1 - Programa Que Imprime El Nombre Del Usuario en:
# Mayusculas
# Minusculas
# Primera Letra De Cada Palabra En Mayusculas

# Ingreso De Nombre
Nombre = input("\nIngrese Su Nombre Completo: ")

# Valida Que Variable No Esté Vacía
while not Nombre :
    print("Erorr, Valor Vacio")
    Nombre = input("Ingrese Su Nombre Completo: ")

# Impresion De Nombre En Mayusculas
print("\nNombre Mayusculas: ")
print(Nombre.upper())

# Impresion De Nombre En Minusculas
print("\nNombre Minusculas: ")
print(Nombre.lower())

# Impresion De Nombre - Primeras Letras En Mayusculas
print("\nNombre Primera Letras Mayusculas: ")
print(Nombre.title())