# Detector de esquinas 
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Cargamos la imgen o su ruta
tablero = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/tablero-ajedrez.png'
# Leemos la imagen
ajedrez = cv2.imread(tablero)
# Se convierte en escala de grises
ajedrez_gris = cv2.cvtColor(ajedrez, cv2.COLOR_BGR2GRAY)

# Indentificamos las esquina de la imagen
esquinas = cv2.goodFeaturesToTrack(ajedrez_gris,maxCorners=100,qualityLevel=0.01,minDistance=10)
# print('Las esquinas son {}'.format(esquinas))
# Convertimos las esquinas en Entero
esquinas = np.int0(esquinas)
# print('Las esquinas son {}'.format(esquinas))

# color de los circulos
el_color = (0,0,255)
# Colocamos un circulo por cada variable esquina
for i in esquinas:
    x,y = i.ravel()
    cv2.circle(ajedrez, (x,y), 4, el_color, thickness=4)

# mostramos la imagen original ya con las esquinas marcadas
plt.imshow(ajedrez)
plt.show()



# Mostramos la imgen original en escala de grises
plt.imshow(ajedrez_gris, cmap='gray')
plt.show()