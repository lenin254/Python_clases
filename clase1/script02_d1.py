# %% Definimos una celda 

z = "este es mi segundo script"
w = (12.8*36)**(-2.9)
r= 'esto sigue siendo la primera clase del prof. Abraham Zamudio'

# %% Definamos otra celda
# Alamcenar datos de un usuario
nombre = " celestino"
ApellidoP = 'Vasquez'
ApellidoM = "Torres"
NumCelular = 987654321
DNI = 76513740

# %% Observacion
#=====================================================
# Tipos basicos de variables en python 
#=====================================================

# cadenas de caracteres : str
# numeros enteros : int
# numero punto flotante : float
# Datos boolean : bool

# Definimos un True 
t1 = True
x1 = False


# %% Operaciones aritmeticas

s = w + c
r = b - c
m = DNI  * 2
d = NumCelular/666

# Potenciacion : **
m1 = m**(1/3)

# Euclides : D = d * q + r
q = 25//8
resto = 25%8

# %% Operaciones con datos de tipo bool 
# and, or, not

# Operacion and (y logico)
zb1 = t1 and x1

# Operacion or (o logico)
zb2 = x1 or t1

# Operacion not (negacion)
zb3 = not t1

# %% Composiciones de operaciones logicas

wb1 = (t1 and t1) or x1 and (x1 or t1)
wb2 = (not zb1) and (zb2 or zb3) or (True)
wb3 = (not wb2) and (not wb1)

# %% Operacion con cadenas de caracteres 

cl1 = 'Clase 1'
f1 = "30/05/2022"
Asist = "21:45"

# Operacion + : concatenacion 
msj1 = cl1 + " " + f1

#Operacion * : repetir
(msj1 + " ") * 3 

# Caracteristicas de las variables de tipo cadena de caracteres :
# Es un objeto con naturaleza vectorial : Manejo un conjunto
# de indices para acceder a sus componentes

# Primera componente es la de indice cero
cl1[0]

# segundo componente
cl1[1]

# tercera componente
cl1[2]

# Si leemos de derecha (final) a izquierda (inicio)
# Ultima componente
cl1[-1]

# Penultima componente
cl1[-2]

# En resumen 
# En python los indices inician en cero (leyendo de izquieda
# a derecha) Los indicies son : 0 , 1, 2 , .....
# Si leemos de derecha a izquierda : los indices son :
# -1 , -2 , -3 ....

# Numero/cantidad de elementos (caracter) que conforman una
# cadena de caracteres (str) : usamos la funcion len
NumElementosCl1 = len(cl1)




