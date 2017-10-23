#FUNCIONES

def MENU():						#Menu principal definido como funcion para no repetirlo constantemente en el codigo
	print("\n")
	print("ESTE ES EL MENU DE OPCIONES, DIGITE EL NÚMERO CORRESPONDIENTE PARA REALIZAR LA OPERACION")
	print("\n")
	print("0 - Modo Comando")
	print("1 - Cambiar todas las letras minúsculas a mayúsculas")
	print("2 - Cambiar de minúscula a Mayúscula la primera letra de todas las palabras")
	print("3 - Cambiar de Mayúsculas a minúsculas todas las letras")
	print("4 - Quitar todos los espacios a la izquierda del texto")
	print("5 - Quitar todos los espacios a la derecha del texto")
	print("6 - Reemplazar todas las ocurrencias de un carácter o palabra por otro")
	print("7 - Cifrado utilizando cifrado Cesar")
	print("8 - Descifrado utilizando cifrado Cesar")
	print("9 - Salir")
	print("\n")

def ModoComando():				#Modo Comando definido como funcion para no repetirlo constantemente en el codigo
	print("\n")
	print("Ingrese el Comando y presione Enter")
	print("Puede concatenar mas de un comando con el caracter \"pipe\" (|)")
	print("\n")
	print("'mM' - Min a Mayus")	
	print("'Mm' - Mayus a Min")
	print("'aA' - Mayus la primera letra de todas las palabras")
	print("'-espacio' - Quita espacios al principio y final")
	print("'b>j' - Reemplaza las 'b' por 'j'")
	print("'más>+ - Reemplaza todas las ocurrencias de la palabra 'más' por '+'")
	print("'cif x' - Cifra el texto utilizando cifrado Cesar con un deplazaiento x")
	print("'decif x' - Decifra el texto utilizando cifrado Cesar con un desplazamiento x")
	print("\n")

def funcion1(a):     #Transforma todas las letras del parámetro en mayúsculas
	a = a.upper()
	return a

def funcion2(a):			#Tranforma la primera letra de cada palabra del parametro en mayúscula
	b =""
	a = a.split(" ")
	for palabra in a:  				#Este for recorre todas las palabras
		for i in range(len(palabra)):    #Este for recorre las letra de cada palabra para reemplazar la primera por mayúscula
			if i == 0:
				b = b + palabra[0].upper()
			else:
				b = b + palabra[i]
		b = b + " "
	b = b.rstrip()				#El rstrip es necesario porque siempre queda un espacio al final
	return b

def funcion3(a):		#Transforma todas las letras del parametro en mayúsculas
	a = a.lower()		
	return a

def funcion4(a):		#Quita los espacios a la izquierda del parametro
	a = a.lstrip()	
	return a

def funcion5(a):		#Quita los espacios a la derecha del parametro
	a = a.rstrip()
	return a

def funcion6(a,b,c):	#Reemplaza todos los caracteres b del parametro a por el caracter c
	d = ""
	for i in range(len(a)):  #Analiza letra por letra al parametro a para reconocer los caracteres b
		if a[i] == b:			
			d = d + c
		else:
			d = d + a[i]
	return d

def funcion7(a,b):		#Cifra el parametro a con un cifrado Cesar de desplazamiento b
	abc1 = "abcdefghijklmnñopqrstuvwxyzabcdefghijklmnñopqrstuvwxyz"
	abc2 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c = ""
	for elemento in a:
		if elemento in abc1:		#Es necesario hacer este if porque Python reconoce las mayusculas y minusculas como caracteres separados
			g = abc1.find(elemento)   #La funcion find nos devuelve la posicion en la cual esta ubicado un elemento de una cadena
			c = c + abc1[g + b]
		elif elemento in abc2:
			f = abc2.find(elemento)
			c = c + abc2[f + b]
		else:
			c = c + elemento		#Si el caracter analizado no es una letra no se modifica
	return c

def funcion8(a,b):			#Descifra el parametro a con un cifrado Cesar de desplazamiento b
	abc1 = "abcdefghijklmnñopqrstuvwxyzabcdefghijklmnñopqrstuvwxyz"
	abc2 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c = ""
	for elemento in a:
		if elemento in abc1:
			g = abc1.find(elemento)
			c = c + abc1[g - b]
		elif elemento in abc2:
			f = abc2.find(elemento)
			c = c + abc2[f - b]
		else:
			c = c + elemento
	return c







