# Manipulacion de imagenes con cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2
img_woman_ruta = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/woman.jpg'

imagen_original = cv2.imread(img_woman_ruta);
# Convertir la imagen que se lee como BGR a RGB de esta forma
imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB);
print("Tamanio de la imagen  original es de \n{}".format(imagen_original.shape))

# Cambiamos el tamanio de la imagen con Opencv2
"""
    Los valores para la funcion resize, primero la imagen que se quiere modificar,
    se le pasa el ancho (600) luego del alto (500).
    
    Se puede modificar el tamanio de la imagen con un porccentaje de valores por ejemplo si se quiere 
    mostrar solo el 50% del tamnio de la imagen original se hace de la segunda forma
"""
# Modificando el tamnio de la imagen a un tamnio de 600px de ancho y 500px de alto
imagen_modificado = cv2.resize(imagen_original, (600, 500))
tamanio_fijo_asignado = imagen_modificado.shape
print("El tamanio nuevo al darle un tamanio fijo es de {}".format(tamanio_fijo_asignado))
# Modificando el tamnio de la imagen a un 50% del tamnio y alto de la imagen original
ancho_y_alto_img = 0.5
"""
    Puede ser asi de esta mandera tambien si no son los mimsos tamanio para el alto y el ancho que se desea
    ancho_porcentaje = 0.5  es igual al 50%
    alto_porcentaje = 0.8   es igual al 80%
"""
imagen_a_medias = cv2.resize(imagen_original, (0,0), imagen_original, ancho_y_alto_img, ancho_y_alto_img)
tamanio_nuevo = imagen_a_medias.shape
print("El tamanio nuevo al darle un porcentaje del tamnio es de {}".format(tamanio_nuevo))

# Girando la imagen 
"""
    El metod flip recive como parametros 2 cosas primero es la imagen que se desea modificar y el segundo
    paramentro es un numero que puede ser el 1 o el 0.
    Que el 1 indica que la imagen solo se gira a los lados (Izquierda o Derecha) en el eje X.
    Que si es 0 inidica que la imagen solo se gira de Arriba a Abajo en el eje Y.
    
"""
imagen_girado = cv2.flip(imagen_original, 1)

"""
    NOTA:
    PARA GUARDAR UNA IMAGEN, HAY QUE DEJAR LA IMAGEN EN SUS PATRONES DE COLORES 
    ORIGINALES ES DECIR QUE SE TIENE QUE GUARDAR NO EN "RGB" SINO EN "BGR", 
    SOLO SE PASA A "RGB" PARA MOSTRARLO CON EL MATPLOTLIB.
    EL CUAL SE MODIFICA DE ESTA FORMA Y SE GUARDA DE ESTA FORMA
"""
# Regresando al color original que lee Opencv
imagen_girado = cv2.cvtColor(imagen_girado, cv2.COLOR_RGB2BGR);
# Guardando la imagen en una carpeta o lugar que se desea 
"""
    Al metodo imwrite se le pasa el nombre con el que se quiere guardar la imagen 
    y se le pasa la imagen que se quiere guardar.
"""
cv2.imwrite('woman_flip.jpg', imagen_girado);

# Mostramos la imagen con plt 
# Imagen Original
plt.imshow(imagen_original)
plt.show()
# Imagen con un tamnio establecido fijamente
plt.imshow(imagen_modificado)
plt.show()
# Imagen con un tamanio por porcentaje
plt.imshow(imagen_a_medias)
plt.show()
# Imagen con giro a lado derecha a izquierda
plt.imshow(imagen_girado)
plt.show()