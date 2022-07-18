# %%
# 1.Listar los primeros 128 números primos cuya suma de dígitos sea un numero par.
def primo(num):
    """
    detecta si un numero es primo o no
    Parameters
    ----------
    num : int
        el numero que se estudia si es primo o no.
    Returns
    -------
    retorna True : si es primo
            False : si no es primo.
    """
    if num > 1 :
        for i in range(2,num):
            resto=num%i
            if resto == 0 : 
                return False
        return True
    elif num == 1 :
        return True
    else :
        return False 
    
def Sum_digit(num):
    """
    retorna la suma de digitos del numero ingresado
    Parameters
    ----------
    num : int
        el numero ingresado.
    Returns
    -------
    sum : int
        suma de digitos.

    """
    sum = 0
    for digit in str(num):   
      sum += int(digit)        
    return sum
        
#Definimos las variables y la lista  
i = 0 
i1 = 1
lista = []
#hacemos un conteo de 128 numeros que solo toma en cuenta los numero que son primos y su suma de digitos es par    
while i < 128 :
    if primo(i1) == True and Sum_digit(i1)%2 == 0  :
        # Agregamos el numero a la lista
        lista.append(i1)
        i = i + 1
    i1 = i1 + 1

# %% 
#2.Construya los primeros 100 elementos de la sucesión de Golomb, cuya formula de recurrencia
# es la siguiente:
#    a(1)=1
#    a(n+1)=1+ a( n+ 1−a (a(n)))
def a(n):
    """
    calcula el elemento de numero n de la sucesion de golomb
    Parameters
    ----------
    n : int
        el numero del elemento de la sucesion.

    Returns
    -------
    retorna el valor entero del elemento de la sucesion
    """
    if n > 1 :
        n = n-1
        return (1 + a(n + 1- a( a(n))))
    return n
    
Lista1 = []
for i in range(1,100):
    Lista1.append(a(i))

# %%
#3.Pida que el usuario ingrese una variable a (numero entero mayor a 100) y una variable b
#  (numero entero mayor a 5000). Cuando a<b el programa debe mostrar los números naturales
#  comprendidos entre ellos en orden ascendente y descendente utilizando una sola estructura
#  repetitiva
num1 = int(input("Ingresa un numero entero mayor a 100 :"))
num2 = int(input("Ingresa un numero entero mayor a 5000 :"))
Lista2 = []
if num1 < num2 : 
    for i in range (num1+1,num2 ):
            Lista2.append(i)
elif num1 == num2 : 
    print("\nLos numeros ingresados son iguales")
else :
    for i in range (num1-1,num2,-1):
            Lista2.append(i)

# %%
#4.Genere 500000 números aleatorios en el intervalo [0, sys.maxsize] y muestre los siguientes
#  resultados:
#  ◦ Genere y muestre la lista de todos los que son cubos de algún numero natural
#  ◦ Cuantos números se tuvo que generar para obtener 200 números primos.
#  ◦ Muestre aquellos números aleatorios que se repitieron mas de 13 veces
import sys
import numpy as np
import random as rnd
cont = 0
lista4 = []
lista_cubos = []
lista_primos = []
for i in range(0,500000):
    lista4.append(rnd.randint(1,sys.maxsize))
    if (np.cbrt(lista4[i])*10)%10 == 0 :
        lista_cubos.append(lista4[i])
    if primo(lista4[i]) == True :
        lista_primos.append(lista4[i])
        cont = cont + 1

print(cont) 
cont1= 0
for i in range(0,500000):
    for e in range(0,500000):
        if lista4[i]==lista4[e] :
            cont1 = cont1 + 1
    if cont1 > 13 :
        print(lista4[i])
    
# %%
#5.Muestre una lista con los divisores primos de int(sys.maxsize/200000)

a = int(sys.maxsize/200000)
for i in range(1,a):
    if a%i == 0 and primo(i)==True :
        print(i)

# %%
#6.Implemente una función que reciba un par ordenado del plano cartesiano R2 y retorne las
#  coordenadas polares del par ordenado ingresado.

def cal_polar(x1,x2):
    """
    calculadora de cordenadas carteasiana R2 a polares
    Parameters
    ----------
    x1 : float
        abcisa.
    x2 : float
        ordenada.
    Returns
    -------
    r : float
        es la distancia de punto al origen.
    a : float
        ángulo formado entre el eje polar y la recta dirigida.
    """
    r = np.sqrt(x1**2 + x2**2)
    a = np.arctan2(x2,x1)
    return r,a

cal_polar(1,1)