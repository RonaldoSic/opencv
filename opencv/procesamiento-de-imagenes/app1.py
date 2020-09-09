# Mapeo de colore con OpenCV
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
woman_sun_flowers = os.getcwd()+'/woman.jpg'
woman_light = os.getcwd()+'/adolescence.jpg'

imagen1 = cv2.imread(woman_light)
# imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
# matriz, saturacio, 
# imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
# Matiz, Saturaion, Luminusidad
# imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HLS)


plt.imshow(imagen1)
plt.show()