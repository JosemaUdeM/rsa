#ALGOTIRMO RSA
#Creado por:
#Jose Manuel Vergara Alvarez
#Estudiante Computacion Cientifica
#Universidad de Medellin


#PROBLEMA NUMERO UNO:
#Escriba una funcion que dados dos numeros p y q genere las llaves publica y privada del algoritmo RSA

#SOLUCION

#Se crearon cinco funciones.

#Funcion para saber, dados dos numeros cual es el minimo.

def minimo (x, y):
	if x<y:
		return x
	else:
		return y
#Funcion para hallar el maximo comun divisor entre dos numeros.
#Definicion:  Mayor numero o polinomio que divide exactamente dos o mas numeros o polinomios.
def mcd (x, y):
	m = minimo (x,y)
	for i in range (m, 0,-1):
		if x%i == 0 and y%i ==0:
			return i

#funcion para saber si dos numeros con coprimos.
#Definicion: dos numeros son coprimos si no comparten ningun factor primo
#Si los dos numeros son coprimos retorna 1, de lo contrario retorna 0.
def arecoprime (x,y):
	if mcd(x,y) == 1:
		return 1
	else:
		return 0
#Funcion para saber si un numero es primo.
#Definicion:un numero primo es un numero natural mayor que 1 que tiene uicamente dos divisores distintos: el mismo y el 1.
#si el numero es primo, retorna 1.
def primo (x):
	for i in range (2, x): 
		if x % i == 0:
			return 0
	return 1

#funcion de euler
#la funcion euler representa el numero de enteros menores y coprimos a un numero dado.
#euler(p) = p - 1 # Si p es un numero primo, pues por definicion sera coprimo con todos los menores que el.
#entonces: euler (p * q) = (p - 1) * (q - 1) # si p y q son primos.
def euler(p,q):
	return (p-1) * (q-1)


#FUNCION PARA GENERAR CLAVE RSA



#Con la condicion "if" se valora si los numeros ingresados por el usuario no son primos, en caso tal de que alguno no lo sea
#aparece el siguiente mensaje en pantalla: "Alguno de los numeros ingresados no es primo, verifique por favor".

# En caso de que ambos lo sean,se multiplica el numero p con el numero q para hallar el numero N.
#N = p * q 

# Se halla phi a traves de la funcion euler(p,q) con la que se encontraran los numeros e y d.
 
# el numero e debe cumplir las siguientes condiciones: [1 < e < phi)] y coprimo con phi.
#Para que se cumpla esto, se crea una lista que va desde 2 hasta el numero anterior a phi:
#Range (2,phi) ya que este va desde 2 hasta phi-1
#A continuacion se utiliza la funcion arecoprime para buscar en la lista 'e' el ultimo numero que sea coprimo con phi y se escoge este.

# 'd' se encuentra multiplicando una lista de numeros * e, y si al dividir el producto entre phi, el residuo
#  es 1, encotraremos una lista de posibles 'd'. Por tal razon se crea un ciclo en el que 'd' es una lista que va desde 0 hasta
#  el doble de phi, para encontrar el segundo numero 'd' de la lista que cumpla la condicion.


p=(input ("ingrese el primer numero primo: ")) #El usuario puede ingresar el primer numero primo a evaluar
q=(input ("ingrese el segundo numero primo: ")) #El usuario puede ingresar el segundo numero primo a evaluar


def myrsa(p,q):
	print "verificando valores ingresados..."
	
        if primo(p)== 0 or primo(q)== 0:
	       	return "Alguno de los numeros ingresados no es primo,verifique por favor"
	else:
		print "Done.los numeros ingresados son primos"
		print "Generando llaves..."
		N = p * q
        	phi = euler(p,q)
		
		for e in range(2,phi):
	     		if arecoprime (phi, e) == 1:
				e
		for d in range(phi*2):
			if e * d % phi == 1:
				d
 		
		print 'La llave publica es:',e,',',N #se imprime la llave publica
		print 'La llave privada es:',d,',',N #Se imprime la llave privada

print myrsa(p,q) #se imprime la funcion myrsa(p,q) evaluando los numeros ingresados por el usuario
	
