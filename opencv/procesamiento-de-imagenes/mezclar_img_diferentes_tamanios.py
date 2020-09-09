# Mezclar imagenes de diferentes tamnios 
import matplotlib.pyplot as plt
import cv2
import os
woman_sun_flowers = os.getcwd()+'/woman.jpg'
woman_light = os.getcwd()+'/adolescence.jpg'
# Imagen 1
imagen1 = cv2.imread(woman_light)
imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
# Imagen 2
imagen2 = cv2.imread(woman_sun_flowers)
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)

# Se obtien los tamanios de las 2 imagenes
tamanio_img_1 = imagen1.shape  # (3557, 5335, 3)
tamanio_img_2 = imagen2.shape  # (6000, 4000, 3)

print("El tamanio de la imagen 1 es de \n {} y el de la imagen 2 es de {}".format(tamanio_img_1, tamanio_img_2))

# Modificamos el ancho de la imagen y se deje del mismo tamnio al que se quiere mostrar 
# en este caso es de 4000

imagen1 = cv2.resize(imagen1, (4000, 3557))
# Recortamos 2000 de la imagen 2
# Con los ':' indicamos todo el ancho y los 2000 indicamos el algo de la imagen
imagen2 = imagen2 [:3557]
# Juntamos las imagenes la que se recorto con la que se ha modificado su tamanio 'imagen1'
imagen_mezcla = cv2.addWeighted(src1=imagen1, alpha=0.6, src2=imagen2, beta=0.5, gamma= 0)

# Agregamso la nueva imagen que se ha unido a la imagen que se le ha recotado los 2000 de alto
imagen2 [:3557] = imagen_mezcla


# Mostramos la imgen que se ha recortado
# plt.imshow(imagen2)
# plt.show()

# Mostrmos la mezcla de las imagens que se ha nunificado
# plt.imshow(imagen_mezcla)
# plt.show()

# Mostramos la imagen que se recorto y se unio con la fusion de las imagens final
plt.imshow(imagen2)
plt.show()