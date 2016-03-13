#ALGOTIRMO RSA
#Creado por:
#Jose Manuel Vergara Alvarez
#Estudiante Computacion Cientifica
#Universidad de Medellin


#PROBLEMA NUMERO DOS

#Escriba una funcion que dada la clave publica y un mensaje compuesto de cuatro digitos desencripte el mensaje formado por estos cuatro #numeros

#SOLUCION

#Se crea la funcion que determina si un numero es primo
#Definicion:un numero primo es un numero natural mayor que 1 que tiene uicamente dos divisores distintos: el mismo y el 1.
#si el numero es primo, retorna 1.

def primo (x):
	for i in range (2, x): 
		if x % i == 0:
			return 0
	return 1

#importamos "myrsa", programa que genera la llave publica y privada
import myrsa


#Dadas la llave publica ingresamos el primer valor como e, y el segundo como N.
#Ejemplo:
#Cuando ejecutamos "myrsa" con los numeros primos (7,2), esto nos arrojara el siguiente resultado:
#"verificando valores ingresados...
#Done.los numeros ingresados son primos
#Generando llaves...
#La llave publica es: 5 , 14
#La llave privada es: 11 , 14"
#Entonces e=5 y N=14.

e=(input ("por favor ingrese el primer numero de la llave publica que se muestra anteriormente:" ))
N=(input ("por favor ingrese el segundo numero de la llave publica que se muestra anteriormente: "))


#Se le pide, igualmente al usuario, que ingrese los cuatro digitos que quiere desencriptar
m1=(input ("ingrese el primer digito a desencriptar: ")) 
m2=(input ("ingrese el segundo digito a desencriptar: "))
m3=(input ("ingrese el tercer digito a desencriptar: "))
m4=(input ("ingrese el cuarto digito a desencriptar: "))


#Una vez obtenemos la llave publica (e,N), y los cuatros digitos (m1,m2,m3,m4), buscamos los numeros primos entres 2 y N para
#hallar los valores de p y q con los que anteriormente se genero la llave publica.
#Este proceso se realiza mediante dos ciclos en los cuales se evalua que numeros son primos y su multiplicacion da como 
#resultado el valor de N
#	Esto, recordando que para generar la llave publica se requieren dos numeros primos, en este caso p y q, y N era igual 
#	a la multiplicacion de estos dos. N= p*q

#Una vez hecho esto, encontramos el valor de phi con la funcion de euler(p,q)

#	Recordando que:
#	la funcion euler representa el numero de enteros menores y coprimos a un numero dado.
#	euler(p) = p - 1 # Si p es un numero primo, pues por definicion sera coprimo con todos los menores que el.
#	entonces: euler (p * q) = (p - 1) * (q - 1) # si p y q son primos.

#Luego hallamos 'd'.
#	Recordando que:
	# 'd' se encuentra multiplicando una lista de numeros * e, y si al dividir el producto entre phi, el residuo
#  	es 1, encotraremos una lista de posibles 'd'. Por tal razon se crea un ciclo en el que 'd' es una lista que va desde 
# 	0 hasta el doble de phi, para encontrar el segundo numero 'd' de la lista que cumpla la condicion.	



#Hemos obtenido ya la clave publica (e,N) y la llave privada (d,N)
#desencriptamos el mensaje de la siguiente manera:
#	A la primera variable "n1" le llevamos el primer digito ingresado "m1",
	#este se eleva al numero "d" y le sacamos modulo del numero N.
#	A la segunda variable "n2" le llevamos el segundo digito ingresado "m2",
	#este se eleva al numero "d" y le sacamos modulo del numero N.
#	A la tercera variable "n3" le llevamos el tercer digito ingresado "m3",
	#este se eleva al numero "d" y le sacamos modulo del numero N.
#	A la cuarta variable "n4" le llevamos el cuarto digito ingresado "m4",
	#este se eleva al numero "d" y le sacamos modulo del numero N.
#	luego de esto se retornan los cuatros numero desencriptados n1,n2,n3 y n4.




def hackrsa(e,N,m1,m2,m3,m4):
	for p in range(2,N):
		for q in range(2,N):
			if primo(p)==1 and primo(q)==1 and p*q == N:

		for d in range(phi*2):
			if e * d % phi == 1:
				d
	n1 = m1**d%N
	n2 = m2**d%N
	n3 = m3**d%N
	n4 = m4**d%N
	return n1, n2, n3, n4




print "Mensaje desencriptado"

#A las variables n1,n2,n3,n4 se le asigna los valores que retorna la funcion hackrsa(e,N,m1,m2,m3,m4)
#se imprimen las variables n1,n2.n3 y n4 que es el mensaje decodificado o desencriptado. 
n1,n2,n3,n4 = hackrsa(e,N,m1,m2,m3,m4) 
print n1,n2,n3,n4
