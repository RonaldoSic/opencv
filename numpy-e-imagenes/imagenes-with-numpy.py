import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_ruta = os.getcwd() + '/adolescence.jpg'
imagen = Image.open(img_ruta)
type_img = type(imagen)
# print("El tipo de la variable es {}".format(type_img))
tamanio_img = imagen.size
print("El tamanio de la imagen es de {}".format(tamanio_img))

# Se convierte en un array la imagen
array_img = np.asarray(imagen)
# print("La imagen como un valor de array {}".format(array_img))

# para conocer la forma que tiene la imgage 
new_shape = array_img.shape
print("La forma del la imagen es de {}".format(new_shape))

# Para conocer los valores para cada color RGB
# Para el color Rojo 
val_red_color = array_img[: ,:, 0]
# Para el color Verde 
val_green_color = array_img[: ,:, 1]
# Para el color Azul
val_blue_color = array_img[: ,:, 2]

print("""Los valore de los colores son \n 
        Rojo (Red): {} \n 
        Verde (Green): {} \n 
        Azul (Blue):""".format(val_red_color, val_green_color, val_blue_color))

# Para mostrar la imagen por medio del plt
print("Show Image")
plt.imshow(array_img)
plt.show()
