"""Desarrollar un programa que solicite un numero entero desde teclado al usuario, posteriormente, el programa deberá determinar e indicar a traves de un mensaje, si el numero introducido es par o impar.

Requerimientos indispensables:

El mensaje en pantalla deberá mostrar la frase"el numero es par o impar, junto con el numero que el usuario introdujo desde teclado"."""

numero = int(
    input("Introduce un número entero que quieras averiguar si es par o impar: "))

resto = numero % 2

if resto == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
