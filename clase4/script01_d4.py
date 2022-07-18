# %% Funciones
# SIntaxis
# def Nombre_de_la_funcion(arg1,arg2,arg3):
import random as rnd
# sentencias1
# sentencias2
# return objeto1,objeto2,objeto3

# %% Funcion que muestre un mensaje


def msj1():
    print("Bienvenidos a la clase 4")

# Una vez ejecutado el codigo fuente de la funcion, esta se carga
# en memoria


# Veamos una ejecucion de la funcion msj1
msj1()

# Ejecutemos 100 veces la funcion msj1
for j in range(100):
    msj1()

# %% Funcion que reciba un nombre y hago un saludo


def msj2(var1):
    print("Estimado %s" % (var1))
    print("Bienvenido a la clase 4")


# Ejemplo de uso
msj2("Alejandro")

# %% Definamos una funcion que genere 20 numeros aleatorios
# en [a,b], donde a y b son argumentos de mi funcion.
# Dicha funcion debe retornar los 3 promedios (aritmetico,
# geometrico y armonico)


def CalculoPromedios(a, b):
    """
    Funcion que calcula 3 promedios para un conjunto de 20
    elementos. Dichos elementos se generan de manera aleatoria
    usando la dist. de probabilidad gauss del modulo random

    Parameters
    ----------
    a : float
        Representa la media de rnd.gauss.
    b : float
        Representa la desviacion estandar de rnd.gauss.

    Returns
    -------
    3 floats (media aritmetica,media geometrica y la media armonica)

    """

    # generar una lista con los 20 elementos
    import random as rnd
    lista1 = []
    for numGen in range(20):
        lista1.append(rnd.gauss(a, b))

    # Calcular los 3 promedios
    MA = sum(lista1)/len(lista1)

    # Calulo de la media geometrica
    # Calculamos la productoria de los elementos
    prod = 1
    for n in lista1:
        prod = prod*n
    MG = prod**(1/len(lista1))

    # Calculo de la media armonica
    sumaInv = 0
    for n in lista1:
        sumaInv = sumaInv + 1/n
    MH = len(lista1)/sumaInv

    # devolvemos los resultados :
    return MA, MG, MH


# Usemos CalculoPromedios
CalculoPromedios(12, 9.8)

# Deseamos ejecutar la funcion Calculo promedios 1000 veces
# y almacenar las salidas.
ListaOutput = []
for k in range(1000):
    ListaOutput.append(CalculoPromedios(12, 9.8))

# Deseo conocer el mayor valor de todas las medias aritmeticas
# Recordar que la deficion de nuestra funcion CalculoPromedios
# retorna como primer elemento a la media aritmetica
# Recuperemos la lista de todas las medias aritmeticas
#
ListaMA = []
for otp in ListaOutput:
    ListaMA.append(otp[0])

# Rspta :
max(ListaMA)

# %% Usemos CalculoPromedios con argumentos argumentos
# aleatorios generados usando 20 pares de numeros con dist
# triangular. Y muestre los maximos y minimos de cada una
# de las medias que devuelve CalculoPromedios


Lista2 = []
for NumVez in range(20):
    Lista2.append(CalculoPromedios(
        rnd.triangular(12, 9.8), rnd.triangular(12, 9.8)))

# Calcular los maximos y minimos de cada una de las listas que retorna
# mi funcion CalculoPromedios
#
# Creemos la lista de Medias aritmeticas
Lista_MA = []
for otp in Lista2:
    Lista_MA.append(otp[0])

# Creamos la lista de medias geometricas
Lista_MG = []
for otp in Lista2:
    Lista_MG.append(otp[1])

# Creamos la lista de medias armonicas
Lista_MH = []
for otp in Lista2:
    Lista_MH.append(otp[2])

# El maximo y minimo de Lista_MA y Lista_MH
max_MA = max(Lista_MA)
min_MA = min(Lista_MA)
max_MH = max(Lista_MH)
min_MH = min(Lista_MH)

# El maximo y minimo de Lista_MG
# Observar que algunos elementos son numeros complejos
# En este caso se calculara el modulo de cada uno de esos complejos
# Crear una lista de medias geometricas (basadaen Lista_MG) de tal manera
# que para los elementos complejos guarde el modulo
Lista2_MG = []
for g in Lista_MG:
    if type(g) == float:
        Lista2_MG.append(g)
    else:
        Lista2_MG.append((g.real**2 + g.imag**2)**(1/2))

# Habiendo calculado la norma/modulo de los elementos complejos
# Obtenemos Lista2_MG
max_MG = max(Lista2_MG)
min_MG = min(Lista2_MG)

# %% Empaquetemos nuestro metodo de la biseccion en una funcion


def f(x): return x**2 - x - 1


def Biseccion(f, a, b, N):
    """
    Funcion que calcula una aproximacion a la solucion de 
    f(x) = 0 en el intervalo [a,b] usando el metodo explicado 
    en clase (Metodo de la biseccion)


    Parametros de entrada
    ----------
    f : Funcion / regla de correspondencia
        Esta es la funcion para la cual estamos tratando de aproximar
        el calculo de una raiz .
    a : float
        Limite inferior del intervalo [a,b].
    b : float
        Limite superior del intervalo [a,b].
    N : int
        Numero de iteraciones.

    Returns
    -------
    X_n : float
    Es el punto medio del N-esimo intervalo calculado usando la 
    estrategia de la biseccion

    """
    if f(a)*f(b) >= 0:
        print("LOs valores ingresados son inadecuados")
        print("Estudie el TVM")
        return None
    else:
        # guardar unas copias de los originales a y b
        a_n = a
        b_n = b
        for n in range(1, N+1):
            # Calculamos el punto medio del intervalo
            m_n = (a_n + b_n)/2
            # Calculamos la imagen del punto medio mediante f
            f_m_n = f(m_n)
            # Estructura de seleccion : Deacuerdo a la estrategia
            # esplicada en clase se debe elegir el subintervalo
            # cuyo producto de imagenes es menor a cero.
            if f(a_n)*f_m_n < 0:
                # actualizamos el intervalo de busqueda
                a_n = a_n
                b_n = m_n
            elif f(b_n)*f_m_n < 0:
                # actualizamos el intervalo de busqueda
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Solucion exacta")
                return m_n
            else:
                print("El metodo de la biseccion falla !!!!")
                return None
        return (a_n + b_n)/2


# Ejemplo 1
Biseccion(f, 1, 2, 100)

# Ejemplo 2 
def func3(t):
    return t*t*t - t*t +2

Biseccion(func3, -200, 300, 50)
# OBservar que la raiz (por simple inspeccion es 1), sin embargo
# nuestra implementacion del algoritmo de la biseccion no llega
# al valor de 1 con 50 iteraciones 
# Probemos con mas iteraciones 
Biseccion(func3, -2,2, 100)

# Ejemplo 3 
import math as m 
def f2(p):
    return m.exp(p) * (3.2* m.sin(p) - 0.5* m.cos(p))

Biseccion(f2, -1 ,2, 100)


# %% Implementemos la estrategia explicada en clase : Met. de la Secante
def secante(f, a,b,N):
    """
    Aproximacion de la solucion de f(x) = 0 usando la estrategia 
    explicada en clase (Metodo de la secante)

    Parameters
    ----------
    f : funcion / regla de correspondencia
        La funcion para la cual deseamos aproximar una raiz .
    a : float
        limite inferior de [a,b].
    b : float
        Limite superior de [a,b].
    N : int
        Numero de iteraciones.

    Returns
    -------
    m_n : float
    La N-esima interseccion dela N-esima recta secante con el eje X
    La formula a usar es 
    m_n = a_n - f(a_n)* (b_n - a_n)/ (f(b_n) - f(a_n))
    El criterio de actualizacion sigue el TVM.
    
    
    """

    if (f(a) * f(b) >= 0):
        print("El metodo de la secante falla")
        return None
    else:
        a_n = a 
        b_n = b
        for n in range(1,N+1):
            # Calculamos la interseccion de la recta secante con 
            # el eje-X
            m_n = a_n - f(a_n)* ((b_n - a_n)/ (f(b_n) - f(a_n)))
            # Calculamos la imagen de esa interseccion
            f_m_n = f(m_n)
            # Seleccionamos el subintervalo cuyo producto de imagenes
            # es menor que cero .
            if (f(a_n) * f_m_n < 0 ):
                # Me quedo con el subintervalo izquierdo
                a_n =a_n
                b_n = m_n
            elif f(b_n)*f_m_n < 0 :
                # Me quedo con el subintervalo derecho
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Encontramos una solucion exacta")
                return m_n
            else:
                print("El metodo se la secante falla !!!")
                return None
        return a_n - f(a_n)* ((b_n - a_n)/ (f(b_n) - f(a_n)))


# Ejemplo1
def f(x): return x**2 - x - 1
secante(f,1,2,50)


# Ejemplo 2 
def func3(t):
    return t*t*t - t*t +2
secante(func3, -2, 0, 50)



# Ejemplo 3 
import math as m 
def f2(p):
    return m.exp(p) * (3.2* m.sin(p) - 0.5* m.cos(p))
secante(f2,-1,2, 50)

# %% Implementemos el metodo de newton 
def newton(f, Df, x0, epsilon, max_iter):
    """
    Aproximacion de la solucion para f(x)=0 usando el metodo de 
    Newton

    Parameters
    ----------
    f : funcion
        funcion / regla de correspondencia de la funcion
        a la cual se le desea calcular una aproximacion
        a una raiz.
    Df : funcion
        derivada de f .
    x0 : float
        Punto inicial de la iteracion .
    epsilon : float
        criterio de patada  : abs(f(x)) < epsilon.
    max_iter : int
        Numero maximo de iteraciones .

    Returns
    -------
    x_n : float 
    x_n = x[n-1] - (f(x[n-1]))/(Df(x[n-1]))
    Continua hasta que abs(f(x_n)) < epsilon
    
    Observacion:
        Si Df(x_n) == 0 ,entonces retornamos None
        Si el numero de iteraciones excede a mas_iter retornamos None
    """
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn)<epsilon:
            print("Encontramos una solucion despues de ", n, "iter")
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0 :
            print("No se encuentra solucion \nLa derivada es cero")
            return None
        xn = xn - fxn/Dfxn
    print("Numero de iteraciones a sido excedido.\nNo se encuentra solucion")
    return None
    
    


# Ejemplo1
def f(x): return x**2 - x - 1
def Df(x) :
    return 2*x -1
newton(f,Df,1,1e-6, 50)


# Ejemplo 2 
def func3(t):
    return t*t*t - t*t +2
Df3 = lambda x: 3*x**2 - 2*x
newton(func3, Df3, 0.5, 1e-9, 50)




# Ejemplo 3 
import math as m 
def f2(p):
    return m.exp(p) * (3.2* m.sin(p) - 0.5* m.cos(p))
def Df2(p):
    return m.exp(p)* (3.7*m.sin(p) + 2.7*m.cos(p))
newton(f2, Df2, 0, 1e-12, 20)
















