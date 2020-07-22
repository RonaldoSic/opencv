# Operacion morfologocos [efectos de erosion, eliminacion de ruido]
import matplotlib.pyplot as plt
import numpy as np
import cv2
# Creamos una imagen de fondo negro
imagen_negro = np.zeros((300, 600))
fuente = cv2.FONT_HERSHEY_PLAIN
blanco = [255,255,255]
# Colocamos el texto en la imagen de color negro
cv2.putText(imagen_negro, text='ABCDE', org=(50, 200), fontFace=fuente, 
            fontScale=4, color=blanco, thickness=3)

# Crearemos un efecto de erosion, recortar letras para que sean mas estrchas
nucleo = np.ones((5,5), dtype=int)
imagen_erocionado = cv2.erode(imagen_negro, kernel=nucleo, iterations=1)

# Creamos un ruido intencional de la siguiente manera, del mismo tamanio de la imagen
ruido = np.random.randint(low=0, high=2, size=(300,600))
# Unificamos el ruido con la imagen 
ruido *= 255
imagen_ruido = imagen_negro + ruido

# Eliminamos el ruido de la imagen con una funcion llamado morphologyEx
image_sin_ruido = cv2.morphologyEx(src=imagen_negro, op= cv2.MORPH_OPEN, kernel=nucleo)

# Elieminamos el relleno de las letras 
gradiente = cv2.morphologyEx(imagen_negro, cv2.MORPH_GRADIENT, nucleo)

# Mostramos la imagen con las letras sin relleno
plt.imshow(gradiente, cmap='gray')
plt.show()

# Mostramos la imagen sin el ruido que se ha generado 
# plt.imshow(image_sin_ruido, cmap='gray')
# plt.show()



# Mostramos el ruido que se ha generado 
# plt.imshow(ruido)
# plt.show()

# Mostramos la imagen con el texto en el 
# plt.imshow(imagen_negro)
# plt.show()

# Mostramos la imagen con el efecto de erosion
# plt.imshow(imagen_erocionado)
# plt.show()

# Mostramos la imagen con el ruido que hemos generado con la imagen negro
# plt.imshow(imagen_ruido, cmap='gray')
# plt.show()