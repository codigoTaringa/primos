#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isprime(n):
    '''chequear si un entero es primo'''
    # chequear que la entrada sea un entero positivo
    n = abs(int(n))
    # 0 y 1 no son primos
    if n < 2:
        return False
    # 2 es el unico primo par
    if n == 2: 
        return True    
    # El resto de pares no son primos
    if not n & 1: 
        return False
    #El rango comienza en 3 y solo necesita subir hasta la raiz cuadrada de n 
    # para todos los impares
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

#Declaramos la lista para guardar el resultado
primos = []
try:
	limit = int(raw_input('Ingrese un número: '))
except ValueError:
	print "Oops!  No es un número valido.."

#Corremos un  loop para guardar los resultados en primos[]
i = 1
if limit > 0:
	while i <= limit:
		check = isprime(i)
		if check == True:
			primos.append(i)
		elif check == False:
			pass
		i = i+1

	#Obtenemos el primos mas grande
	mayor = primos.pop()
	print 'Se encontraron %d numeros primos' % (len(primos))
	print 'El mas alto es %d y contiene %d digitos' %(mayor,len(str(mayor)))

	print_all = raw_input('Imprimir resultados (s/n)')
	if print_all == str('s'):
		i = 1
		for x in primos:
			print i,'->',x
			i=i+1
	elif print_all == str('n'):
		pass
	else:
		pass
