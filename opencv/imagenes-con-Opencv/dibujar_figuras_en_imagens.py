# Crear una imagen de color negro y Dibujar figuras en la Imagen con OpenCV desde Python
import numpy as np
import matplotlib.pyplot as plt
import cv2
# adolescence_woman = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/adolescence.jpg'

# Creamos una image completamente de color negro
imagen_color_negro = np.zeros(shape=(500, 500, 3), dtype=np.int16)
print("El tamnio de la imagen es de {}".format(imagen_color_negro.shape))
# Modificamos la imagen de color negro y le colocamos un rectangulo de color rojo en el 
"""
    El metodo rectangle recive 5 parametros que son los siguietes.
    1: la imagen que se va a modificar.
    2: pt1= indica en que cordenada empieza el rectangulo en este caso es del 20(en X) 
        y 20(en Y), que es la esquina superior izquierda del rectangulo.
    3: pt2= Indica en que cordenada termina el rectangulo en este caso el del 100(en X)
        y 100(en Y), es la esquina inferior derecha del rectangulo.
    4: color(), que es una funcion que recive el valor del color en formato RGB para que sea
        de color rojo se coloca los valores color(255,0,0).
    5: thickness = numero: Indica el grosor de la linea que dibja el rectangulo
"""
imagen_con_rectangulo = cv2.rectangle(imagen_color_negro, 
                                        pt1=(20,20), pt2=(100,100), 
                                        color=(255,0,0), thickness=5)

# Modificamos la imagen de color negro y le colocamos un circulo de color verde en el 
"""
    El metodo circle recive los siguietes parametros que son.
    1: la imagen que se va a modificar.
    2: center =(): indica en que cordenada empieza el centro del circulo en este caso 
    es del 250(en X) y 250(en Y).
    3: radius =(): indica el tamanio del radio que trndra el curculo en este caso es de 100
    4: color(), que es una funcion que recive el valor del color en formato RGB para que sea
        de color verde se coloca los valores color(0,255,0).
    5: thickness = numero: Indica el grosor de la linea que dibja el circulo
"""
imagen_con_circulo = cv2.circle(imagen_color_negro,
                                center=(255,255), radius=100, color=(0,255,0), 
                                thickness=10)

# Modificando la mimsa imagen que tiene el circulo y el rectangul en el 
imagen_modificado = cv2.rectangle(imagen_color_negro, 
                                        pt1=(20,20), pt2=(100,100), 
                                        color=(255,0,0), thickness=5)
imagen_modificado = cv2.circle(imagen_color_negro,
                                center=(255,255), radius=100, color=(0,255,0), 
                                thickness=10)
# Le agrgamos una recta de color azul a la imagen de fongo negro
cv2.line(imagen_color_negro, pt1=(0,400), pt2=(500,400), color=(0,0,255), thickness=5)
# Mostramos la imagen 
# plt.imshow(imagen_color_negro)
# plt.show()

# Mostramos la imgaen con el rectangulo
# plt.imshow(imagen_con_rectangulo)
# plt.show()

# Mostramos la imgaen con el Circulo
# plt.imshow(imagen_con_circulo)
# plt.show()

# Mostrando la imagen con las figuras en el 
plt.imshow(imagen_modificado)
plt.show()
