# %% Funcion print : mostrar mensajes en pantalla 
# rutina de escritura

# Forma primaria del print
print("Bienvenidos a la segunda clase ")

# Segunda forma : Usando algunos wildcards de C/C++
a = 12.2
b = 14
c = 'Usos del print'

print("El valor almacenado en la variable a es : %2f" %(a))
print("Un valor entero es la variable b : %d" %(b))
print("Un ejemplo de string es : %s " %(c))

# Tercera forma es
print ("a es : %2f \nb es : %d \nc es : %s"%(a,b,c))



# %% Ejemplito
# Considere la compra de 3 productos 
# 1.8Kg de azucar
# 3.5Kg de arroz 
# media docena de latas de atun 
#
# Precios 
# Azucar : S/5 (kg)
# Arroz : S/3.8 (kg)
# Doc. latas de atun : S/24 
#
#Suponiendo que los precios tienen grabadoio el IGV (18%)

MontoTotal = (1.8*5 + 3.5*3.8 + 0.5*24)*1.18

print ("La lista de compras es : \n1.8kg de azucar \n3.5kg de arroz \
          \n6 latas de atun \nEl total a apagar es %.2f \
             \n ========================================" %(MontoTotal))

# Usando el docstring 
print ("""
       La lista de compra es :
       1.8kg de azucar
       3.5kg de arroz
       6 latas de atun
       El total a apagar es %.2f
       """%(MontoTotal))
       
# %% Rutinas de entrada 
# Rutnina que nos va ayudar a recibir datos del usuario 
# El usuario (por defecto) va ingresar los datos por el teclado
#
# Funcion input

# Pidamos al usuario su nombre, edad, estatura
nombre  = input("Ingresa tu nombre : ")
edad = int(input("Ingresa tu edad :"))
estatura = float(input("Ingresa tu estatura : "))


# %% 
# Importacion de modulos
# modulo matematico
import math as m 

# %%
# Documentacin del modulo matematico : alias m
help(m)

# %%
help(m.sin)
help(m.radians)

# Calcular el seno de 120 grados
x = 120
x_rad = m.radians(x)
y = m.sin(x_rad)

print("""
El seno de %.0f es %.3f
      """%(x,y))

# %%
#Lista de funciones matematicas /metodos que se componen math 
dir(m)


# %%
# La fija del dia de hoy para la primera ecaluacion 
# Leer/entender/comprender/estudiar cada una 

# %%
import random as rnd
help(rnd)
dir (rnd)

# %%
help(rnd.gauss)

# Generemos dos variables aleatorias con distribucion gaussiana : usando rnd.gauss
a = rnd.gauss(12.8, 2.3)
b = rnd.gauss(58, 6.3)

print("""
El primer aleatorio generado es : %f
El segundo aleatorio generado es : %f 
      """%(a,b))
      
# %%      
# Aprendamos a usar ranint
help(rnd.randint)

# Generemos un numero aleatorio en el intervalo [0,12]

nota1 = rnd.randint(0, 12) 
print ("La nota alcanzada es : %d" %(nota1))


# %%
# Otra fija para el lunes 
# Aprender a utilizar las funciones que listamos a continuacion pertenecientes 
# Al modulo random (alias rnd)
# 'betavariate',
# 'choice',
# 'choices',
# 'expovariate',
# 'gammavariate',
# 'gauss',
# 'getrandbits',
# 'getstate',
# 'lognormvariate',
# 'normalvariate',
# 'paretovariate',
# 'randint',
# 'random',
# 'randrange',
# 'sample',
# 'seed',
# 'setstate',
# 'shuffle',
# 'triangular',
# 'uniform',
# 'vonmisesvariate',
# 'weibullvariate'


# %%
# Conocer el tipo de dato de una variable u objeto de python
type (a)
type (x)

# Nunca olvidar :
# type
# dir 
# help

# %%
# Datos estructurados
# Listas : Datos estructurados de python
# Definicion
Lista1 = []
type(Lista1)

Lista2 = ["Segunda" , "Clase" , "programacion en python"]
type(Lista2)

# Algunas operaciones : +
Lista2 + [1,2,3,9,8,7] 

Lista1 + Lista2 + ["X" , "XI" , "XII"]

# Otra operacion : *

["true" , "false"] * 2

# Acceso a los elementos de una lista 
# Primer elemento de Lista2
Lista2[0]
#ultimo elemento de Lista2
Lista2[-1]

#Los metodos que aplicaremos a listas es :
dir (list)

#veamos que hace cada uno de estos metodos
# Metodo append
help(Lista1.append)

Lista1

Lista1.append(12)

# Agreguemos otro objeto a lista 1
Lista1.append("doce")

Lista1.append(["clase ", "dos"])

# %%
# A una lista en blanco , agregue de manera consecutiva 3 numeros aleatorios usando
# 3 distribuciones de probabilidad distinta

# Definamos una lista en blanco
ListaBlanco = []

# Empecemos agregando el 1er numero aleatorio 
ListaBlanco.append(rnd.gauss(12, 2))

# Agregamos el 2do aleatorio
ListaBlanco.append(rnd.randint(0, 20))

# Finalmente agregamos el 3er numero aleatorio 
ListaBlanco.append(rnd.uniform(23, 34))

print(ListaBlanco)


# %%
# Veamos que hace el metodo clear 
help(ListaBlanco.clear)

Lista3 = ["ñ" , "ó" , "í" , "á"]
Lista3.clear()

print ("El ultimo valor de la variable Lista3")
print(Lista3)



# %%
# veamos el metodo copy
Lista2Copy = Lista2
print(Lista2Copy)

# Modificamos el primer elemento de la copia 
Lista2Copy[0] = "2da"
print(Lista2Copy)

#veamos que hay en lista2 
print(Lista2)

# El metodo copy es la opcion para crear una copia de una lista
Participantes = ["Alex" , "Carmen" , "Alfredo" , "Pedro"]
print (Participantes)

# cometi un error y deseo guardar el original
# El error cometido es en "Alfredo" , debe ser "Alfred"

ParticipantesCopy = Participantes.copy()
ParticipantesCopy[2] = "Alfred"

print("La lista corregida : ")
print(ParticipantesCopy)
print("La lista original : ")
print(Participantes)

# %%
# El siguiente metodo es count 
# Veamos la documentacion 
help(list.count)

# Definamos una lista 
Data = [12 ,14 ,19 ,25 ,34,12,13,14,15,12,15,19,25]
print (Data)

# Cuantas veces se repite el valor de 12 
Data.count(12)

# %%
# Veamos al metodo extend 
# Primero que dice la documentacion
help(list.extend)

# Creemos una lista
Lista4 = ["rojo","axul","verde",255,1024,768]

# Aplicamos eñ metodo extend
Lista4.extend(["a","b","c","d","e"])

print("El resultado de aplicar extend es :")
print(Lista4)

# %%
# Metodo index
# Veamos la documentacion
help(list.index)

Data.index(12)
# Le retorna el lugar de la aparicion del elemento

# %%
# Metodo inster
# Veamos la documentacion
help(list.insert)
print(Data)

# Insertemos el valor 20 antes del 34 (indice 4)
Data.insert(4, 20)
print (Data)

# %%
# Metodo pop
# Documentacion
help(Data.pop)

# Si no espesificamos la posicion, quita el ultimo elemento
Data.pop()
print(Data)

# Deseamos remover el valor 34
Data.pop(5)
print(Data)

# %% 
# Metodo remove
# Documentacion
help(list.remove)

# Removamos el primer 19 de Data
Data.remove(19)
print(Data)

# Eliminamos el siguiente 19 
Data.remove(19)
print(Data)

# %%
# Metodo reverse
# Documentacion
help(list.reverse)

Lista2.reverse()
print(Lista2)

# %%
# Metodo sort
# Docuementacion 
help(list.sort)
print(Data)
Data.sort() 
print(Data)

# %%
# Funciones asociadas 
#
# Funcion len : cuenta la cantidad de elementos de una lista
len(Data)

len(Lista2)

ListaP = [[12,13],14,[15,16]]
print(len(ListaP))

# En el que las listas tengan solo valores numericos : min, max, sum
# min : calcula el minimo valor de una lista
# max : calcular el maximo valor de una lista
# sum : Suma los elementos de una lista

MinimaData = min(Data)
MaximoData = max(Data)
SumaElementosData = sum(Data)
print ("""
El minimo valor de data es : %d
El maximo valor de data es : %d       
La suma de elementos de Data es : %d
"""
 %(MinimaData, MaximoData, SumaElementosData))

# %%
# Otro tipo de dato : tuplas
# Definicion
t1 = (10,20,30,40)
print(t1)
type (t1)
# Obs. Las tuplas son inmutables

dir(tuple)

# %% 
# 'count'
# 'index'
help(t1.count)
help(ListaP.index)


# %%
# Ejercicio 1 : Calculo de precios con descuento
# Escribe un programa que reciba como datos el precio , el tanto por ciento de descuento, y te diga el
# precio con descuento. Por ejemplo, si el precio es 300 y el descuento 20, el programa dira que el precio 
# final con descuento es de 240

#entradas / input : precio y dscto
precio = float(input("Ingresa el precio : "))
dscto = float(input("Ingresa el dscto : "))

#Realicemos las operaciones 
PreciosFinal = precio*(100-dscto)/100

# Mostremos los resultados
print("""
Tienda : Mi barrio
====================
Precio : %f
Descuento : %f
--------------------
El precio a pagar es : %f
      """
      %(precio,dscto,PreciosFinal))
      


