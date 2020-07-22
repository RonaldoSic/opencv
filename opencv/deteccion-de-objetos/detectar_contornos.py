# Detectar contorno en imagenes
import numpy as np
import cv2
import matplotlib.pyplot as plt
# Cargamos la imgen o la ruta
face_woman = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/adolescence-face.jpg'

# leemos la imagen 
imagen = cv2.imread(face_woman)
# Identificamos los contornos 
contorno = cv2.Canny(image= imagen, threshold1=200, threshold2=200)

# mostramos el contorno
plt.imshow(contorno)
plt.show()

# Modificamos la imagen le quitamos el ruido a la imagen
imagen = cv2.blur(imagen, ksize=(5,5))
# Obntenemos el contorno nuevamente sin ruido
contorno_sin_ruido = cv2.Canny(imagen, 200, 200)
# mostramos el contorno ya sin ruido
plt.imshow(contorno_sin_ruido)
plt.show()

# Mostramos la imagen 
plt.imshow(imagen)
plt.show()
