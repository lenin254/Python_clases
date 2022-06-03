# %% Multipls mensajes
# Funcion print : sirve para mostrar mensajes en pantalla

# 1era forma de usar print 

print("curso : programacion en python")
print("Lunes y miercoles de 7 a 10PM")
print("prof. Abraham Zamudio")

# %% Python hereda ciertas cosas de C (printf)

# \t : tab
# \n : salto de linea

print("Esta es nuestra \nprimera clase")
print("Horario : Lunes \t y \t miercoles (7-10 PM)")

# %% Mostremos numeros y cadenas

print("El valor almacenado en la variable w es : %f" %(w))

print ("El numero entero : variable q es : %d" %(q))

print ("El prof del curso es %s" %(e))

# Comentario
# %f : imprimir numeros punto flotante
# %d : imprimir numeros enteros (%i)
# %s : imprimir cadenas de caracteres

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
              ========================================" %(MontoTotal))
