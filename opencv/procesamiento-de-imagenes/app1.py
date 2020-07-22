# Mapeo de colore con OpenCV
import numpy as np
import matplotlib.pyplot as plt
import cv2

woman_sun_flowers = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/woman.jpg'
woman_light = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/adolescence.jpg'

imagen1 = cv2.imread(woman_light)
# imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
# matriz, saturacio, 
# imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
# Matiz, Saturaion, Luminusidad
# imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HLS)


plt.imshow(imagen1)
plt.show()