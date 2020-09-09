# Mostrar imagen en diferentes tamanios en pantalla
import matplotlib.pyplot as plt
import cv2
import os
# url de la imagen que se quiere cargar
woman_sun_flowers = os.getcwd()+'/woman.jpg'
# Lectura de la imagen con cv2
imagen_mujer = cv2.imread(woman_sun_flowers)
# Cambiamos los paramentros de colores de la imagen despues de su lectura
imagen_mujer = cv2.cvtColor(imagen_mujer, cv2.COLOR_BGR2RGB)
# Modificamos la manera que se va a mostrar en en el plot 
# Creamos una figura que tendra un tamanio de 20 por 20 en zoom
figura = plt.figure(figsize=(10,6))
# Creamos un lienzo para agregarle la figura que se ha creado
lienzo = figura.add_subplot(111)
# al lienzo, se le agrega la imagen que se va a mostrar en el plot
lienzo.imshow(imagen_mujer)

# mostramos la imagen
# plt.imshow(imagen_mujer)
plt.show()
