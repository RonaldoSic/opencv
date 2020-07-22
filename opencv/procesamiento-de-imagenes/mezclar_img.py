# Mezclar imagenes con el mismo tamanio
import matplotlib.pyplot as plt
import cv2

woman_sun_flowers = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/woman.jpg'
woman_light = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/adolescence.jpg'
# Imagen 1
imagen1 = cv2.imread(woman_light)
imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
# Imagen 2
imagen2 = cv2.imread(woman_sun_flowers)
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)

# Se obtien los tamanios de las 2 imagenes
tamanio_img_1 = imagen2.shape  # (3557, 5335, 3)
tamanio_img_2 = imagen2.shape  # (6000, 4000, 3)

print("El tamanio de la imagen 1 es de \n {} y el de la imagen 2 es de {}".format(tamanio_img_1, tamanio_img_2))

# Modificamos el tamanio de las imagenes y se deje del mismo tamnio

imagen1 = cv2.resize(imagen1, (1200, 1200))
imagen2 = cv2.resize(imagen2, (1200, 1200))

imagen_mezcla = cv2.addWeighted(src1=imagen1, alpha=0.5, 
                                src2=imagen2, beta=0.5, gamma= 0)
plt.imshow(imagen_mezcla)
plt.show()

