import Funciones

#Se importan las funciones y se hace el input para que el usuario agregue el texto

print("Inicio del programa")
print("\n")
cadena = str(input("Ingrese su texto y presione Enter para continuar: "))
print("\n")
print("Texto recibido y guardado")
print("\n")

Funciones.MENU()

indicacion = int(input("Ingrese la opción que quiera ejecutar: "))

#Se da la opcion al usuario de elegir la opcion que quiera ejecutar

cadena1 = cadena

while indicacion >= 0 and indicacion < 9:
    if indicacion == 0:
        Funciones.ModoComando()
        indcomando = str(input())
        indcomando = indcomando.split("|")
        for elemento in indcomando:
            if elemento == "mM":
                cadena1 = Funciones.funcion1(cadena1)
            elif elemento == "Mm":
                cadena1 = Funciones.funcion3(cadena1)
            elif elemento == "aA":
                cadena1 = Funciones.funcion2(cadena1)
            elif elemento == "-espacio":
                cadena1 = Funciones.funcion4(cadena1)
                cadena1 = Funciones.funcion5(cadena1)
            elif elemento == "b>j":
                cadena1 = Funciones.funcion6(cadena1, "b", "j")
            elif elemento == "más>+":
                cadena2 = ""
                cadena1 = cadena1.split(" ")
                for palabra in cadena1:
                    if palabra == "más":
                        cadena2 = cadena2 + " " + "+"
                    else:
                        cadena2 = cadena2 + " " + palabra
                cadena2 = cadena2.lstrip()
                cadena1 = cadena2
            elif "decif" in elemento:
                elemento = elemento.split(" ")
                descesar = int(elemento[1])
                cadena1 = Funciones.funcion8(cadena1, descesar)
            elif "cif" in elemento:
                elemento = elemento.split(" ")
                cesar = int(elemento[1])
                cadena1 = Funciones.funcion7(cadena1, cesar)
    elif indicacion == 1:
        cadena1 = Funciones.funcion1(cadena1)
    elif indicacion == 2:
        cadena1 = Funciones.funcion2(cadena1)
    elif indicacion == 3:
        cadena1 = Funciones.funcion3(cadena1)
    elif indicacion == 4:
        cadena1 = Funciones.funcion4(cadena1)
    elif indicacion == 5:
        cadena1 = Funciones.funcion5(cadena1)
    elif indicacion == 6:
        titular = str(input("Ingrese el caracter que quiere reemplazar: "))
        suplente = str(input("Ingrese el caracter con el cual quiere reemplazar al anterior: "))
        cadena1 = Funciones.funcion6(cadena1,titular,suplente)
    elif indicacion == 7:
        cesar = int(input("Ingrese el desplazamiento para el cifrado: "))
        cadena1 = Funciones.funcion7(cadena1,cesar)
    elif indicacion == 8:
        descesar = int(input("Ingrese el desplazamiento para el descrifrado: "))
        cadena1 = Funciones.funcion8(cadena1,descesar)
    print("\n")
    print("Ahora su texto es : " + cadena1)
    print("\n")
    Funciones.MENU()
    indicacion = int(input("Ingrese la opción que quiera ejecutar: "))

    
#Si la opcion es 9 se devuelve la cadena original y la cadena final    

if indicacion == 9:
    print("\n")
    print("Texto original: " + cadena)
    print("\n")
    print("Texto final: " + cadena1)




  
   
