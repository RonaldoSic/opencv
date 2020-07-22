# Gradientes y contornos en Opencv
import matplotlib.pyplot as plt
import numpy as np
import cv2
# url de la imagen que se quiere cargar
sodoku = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/sudoku.jpg'
# Lectura de la imagen con cv2
imgen = cv2.imread(sodoku, 0)

# MANERA 1 DE CONSEGUIR LOS CONTORNOS DE UNA IMAGEN
# Identificamos los contornos de la imagen de modo vertical 
"""
    El metodo Solbel recive como parametro la imagen que se va a reconocer, y se le pasa
    una constante, que es 'cv2.cvw.CV_64f' luego se le pasa 1 en x para que los lea en
    la misma linea de Vertical y 0 en la linea de horizontal, para que reconozca los 
    contornos de manera horizontal, se cambia los valores de, dx: a 0 y dy: a 1
"""
sobelx = cv2.Sobel(imgen, ddepth=cv2.CV_64F, dx= 1, dy= 0, dst=None, ksize= 5)
sobely = cv2.Sobel(imgen, ddepth=cv2.CV_64F, dx= 0, dy= 1, dst=None, ksize= 5)
# Unificamos las 2 imagenes que se han creado con Sobel

img_con_contorno = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)

# plt.imshow(imgen, cmap='gray')
# Mostramos la imagen con los contornos Verticales
plt.imshow(sobelx, cmap='gray')
plt.show()
# Mostramos los contornos de manera Horozontales
plt.imshow(sobely, cmap='gray')
plt.show()
# Mostramos la imagen con los contornos Verticales y Horizontales
plt.imshow(img_con_contorno, cmap='gray')
plt.show()

# MANERA 2 PARA CONSEGUIR LOS CONTORNOS DE UNA IMAGEN
laplacian = cv2.Laplacian(imgen, ddepth=cv2.CV_64F)
plt.imshow(laplacian, cmap='gray')
plt.show()