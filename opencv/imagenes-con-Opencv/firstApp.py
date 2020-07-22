# Abrir una Imagen con OpenCV desde Python
import numpy as np
import matplotlib.pyplot as plt
import cv2

ruta_imagen = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/numpy-e-imagenes/mountain.jpg'
img_woman_ruta = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/woman.jpg'
# Leeemos el fichero 
imagen = cv2.imread(img_woman_ruta)
tipo_variable = type(imagen)
forma_imagen = imagen.shape
print("Tipo de variable = {} \nForma de la image = {}".format(tipo_variable, forma_imagen))
# OpenCV lee los colore de la siguiente forma
"""
    OpenCV: BGR (Blue, Green, Red)
    Matplotlib: RGB (Red, Green, Blue)
"""
# Convertir la imagen que se lee como BGR a RGB de esta forma
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB);
# Mostramos la imagen con plt 
plt.imshow(imagen)
plt.show()