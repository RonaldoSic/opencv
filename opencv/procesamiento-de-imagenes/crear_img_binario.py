# Crear imagen bianario
import matplotlib.pyplot as plt
import cv2
import os
woman_light = os.getcwd()+'/adolescence.jpg'
# Con el parametro 0 le indicamos que lo lea en formato de escalas de grises sin color
imagen_mujer = cv2.imread(woman_light, 0)
# Convertimos la imagen en escala de grises con el parametro de cmap
plt.imshow(imagen_mujer, cmap='gray')
# Convertimos la imagen de escalas de grises a una imagen binaria
"""
    La funcion threshold, retorna 2 variables no modifica la imagen de una vez,
    retorna la imagen misma, y otro valor que se mitad que considera el valor en binario
    
"""
mitad, imagen_mujer = cv2.threshold(src=imagen_mujer, thresh= 255/2, maxval= 255, type= cv2.THRESH_BINARY)
plt.imshow(imagen_mujer, cmap='gray');

plt.show()