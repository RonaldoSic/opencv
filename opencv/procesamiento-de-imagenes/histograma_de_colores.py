# Histograma de colores de una imagen
import matplotlib.pyplot as plt
import numpy as np
import cv2

woman_light = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/adolescence.jpg'
imagen_mujer = cv2.imread(woman_light)
imagen_mujer = cv2.cvtColor(imagen_mujer, cv2.COLOR_BGR2RGB)
print('Foma de la imagen {}'.format(imagen_mujer.shape))
# histograma_red = cv2.calcHist(imagen_mujer,channels=0,mask=None,histSize=256,ranges=(0,256))
histograma_red = cv2.calcHist(imagen_mujer,[0],None,[256],[0,256])
histograma_green = cv2.calcHist(imagen_mujer,[1],None,[256],[0,256])
histograma_blue = cv2.calcHist(imagen_mujer,[2],None,[256],[0,256])

# Obetenemos los colores en una sola mascara 
colores = ('b','g','r')
for i, colores in enumerate(colores):
    histo = cv2.calcHist(imagen_mujer,[i],None, [256], [0,156])
    plt.plot(histo)
    plt.xlim([0,256])
    
# Dibujamos el histograma del color rojo por ser el de la posicion 0
# plt.plot(histograma_red)
# plt.show()
# Dibujamos el histograma del color verde por ser el de la posicion 0
# plt.plot(histograma_green)
# plt.show()
# Dibujamos el histograma del color azul por ser el de la posicion 0
# plt.plot(histograma_blue)
# plt.show()
# plt.imshow(imagen_mujer)
plt.show()
