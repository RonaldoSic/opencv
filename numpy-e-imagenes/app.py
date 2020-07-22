# Importamoas la libreria para los arrays
import numpy as np
lista = [1, 2, 3]
array = np.array(lista)
print(array[0])
# Manera para crear array con numero secuenciales
"""
    El primer parametro indica el valor donde debe de empezar el array
    El segudo paramereo indica el valor donde va a acabar (-1),
    Se puede colocar un tercer valor para inidicarle en que rango debe de colocar el 
    siguiente numero o dara saltos por ejemplo de 2 en 2
"""

array2 = np.arange(0,20)  
array3 = np.arange(0,21, 2)  
print(array2)
print(array3)
# Podemos crear una matriz de 0 (Ceros) o de 1 (Unos)
"""
    El primero parametro indica la cantidad de Filas, el segundo indica la cantidad de columnas
"""
matriz_unos = np.ones(shape=(4,2))
matriz_ceros = np.zeros(shape=(4,2))
print(matriz_ceros, '\n', matriz_unos)

# Para crear numero aleatorios de la siguiente manera
"""
    El primero parametro indica el valor inicial, el segundo indica el valor 
    final del rango de los numero (-1) y el tercer parametro indica la 
    cantidad de numero que se quiere en ese rango de numeros
"""
aleatorio = np.random.randint(0, 51, 10)
print(aleatorio)
# Para saber la posicion del valor maximo del arreglo
print('La posicion del valor maximo esta en el indice: ',aleatorio.argmax())
print("La posicion del valor minimo esta en el indice: {} ".format(aleatorio.argmin()))
# Para saber el valor maximo o monimo
print("El valor maximo es {} \nEl valor minimo es {} ".format(aleatorio.max(), aleatorio.min()))

# Cambiamos la forma del arreglo a una matriz
print("La fomra o la cantidad de datos que tiene el arreglo es {}".format(aleatorio.shape))
# En total tiene dar como reultado el valor del la forma que tiene 
# se transforma en una matriz de 2 filas y 5 columnas
aleatorio = aleatorio.reshape(2,5)  # para que de 10 se miltiplica los valores que esta como paramentros
print('La matriz es \n {}'.format(aleatorio))