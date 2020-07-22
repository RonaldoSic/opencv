# Deteccion (o emparejamiento de imagenes) por caracteristicas
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Cargamos las imagenes que se utilizan
caja_cereal = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/cereal.png'
cajas_cereales = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/cereales.png'

# leemos las imagenes
cereal = cv2.imread(caja_cereal)
cereales = cv2.imread(cajas_cereales)
# Cambiamos de colores a las imagenes
cereal = cv2.cvtColor(cereal, cv2.COLOR_BGR2RGB)
cereales = cv2.cvtColor(cereales, cv2.COLOR_BGR2RGB)

# extraemos las caracteristicas de las imagenes
# sift = cv2.xfeatures2d_SIFT_create()
# print('Versiond e OpenCV {}'.format(cv2.__version__))
sift = cv2.xfeatures2d.SIFT_create()  # No este disponible para la version gratuita
# print('Caracteristicas {}'.format(sift))
# La variable kp = son las key points de donde esta las caracteristicas
kp1, descripcion1 = sift.detectAndCompute(cereal, None)
kp2, descripcion2 = sift.detectAndCompute(cereales, None)

# Emparejamiento de las imagenes 
# Creamos un diccionario con 2 parametros
indice = dict(algorithm = 0, trees = 5)
# Creamos un diccionario para la busqueda
busqueda = dict(checks=50)
# el flan se usa paa encontrar el emparejamiento de las 2 imagenes
flan = cv2.FlannBasedMatcher(indice, busqueda)
# Creamos el emparejamiento de las descripciones de las 2 imagenes
emparejamientos = flan.knnMarch(descripcion1, descripcion2, k=2)
print('Los KP de emparejamiento son {}'.format(emparejamientos))

# Buscamos los que mas conciden o que tengan menor distancia entre ellos
mejores = []
for emparejamiento1, emparejamiento2 in emparejamientos:
    if emparejamiento1.distance <0.7 * emparejamiento2.distance:
        mejores.append([emparejamiento1])

# dibujamos las lineas de emparejamiento de la imagen
imagen_emparejada = cv2.drawMatchesKnn(cereal,kp1, cereales,kp2,mejores[0:30],None, flags=0)
imagen_emparejada = cv2.cvtColor(imagen_emparejada, cv2.COLOR_BGR2RGB)
# Modidifcamoes el tamanio del plto
figura = plt.figure(figsize=(9,9))
lienzo = figura.add_subplot(111)

lienzo.imshow(imagen_emparejada)
plt.show()

# 
plt.imshow(imagen_emparejada)
plt.show()
# Mostramos la imagen de la caja de cereal
# plt.imshow(cereal)
# plt.show()
# Mostramos la imagen de las cajas de cereal
# plt.imshow(cereales)
# plt.show()


