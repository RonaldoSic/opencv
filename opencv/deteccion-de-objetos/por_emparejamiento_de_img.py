# Detectar imagenes por emparejamienteo con otra imagen
import matplotlib.pyplot as plt
import cv2
import os 

# Imagen de la Adolecente
adolescence = os.getcwd()+'/adolescence.jpg'
face_adolescence = os.getcwd()+'/adolescence-face.jpg'

# se carga la imagen de la adolecente
imagen = cv2.imread(adolescence)
# se modifica su color de la imagen para mostrarlo
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Se carga la imgen de la cara de la adolecente
imgen_face = cv2.imread(face_adolescence)
imgen_face = cv2.cvtColor(imgen_face, cv2.COLOR_BGR2RGB)

# Se busca la el rostro de la mujer en la imagen original con este metodo
metodo = cv2.TM_CCOEFF
# La variable resultado es un mapar de calor donde indica donde esta el objeto que se busca
resultado = cv2.matchTemplate(imagen, imgen_face, method=metodo)

# Obtenemos las cordenadas de donde esta el mapa de calor
valor_min, valor_max, pos_min, pos_max = cv2.minMaxLoc(resultado)

# Para dibujar un rectangulo del tamanio de la cara se obtiene el tamanio de la cara asi 
print('El tamanio del rostro es de {}'.format(imgen_face.shape))
# Con esto asignamos cada valor en cada variable 
alto, ancho, colores = imgen_face.shape
# Se calcula las posiciones del rectangulo
top_izquierda = pos_max
bottom_derecha = (pos_max[0]+ancho, pos_max[1]+alto)

# Dibujamos el rectangulo en la imagen de la mujer donde este el rostro de ella
cv2.rectangle(imagen, top_izquierda, bottom_derecha, (255,255,255), 8)

# Mostramos la imagen con el rectangulo
plt.imshow(imagen)
plt.show()

# Mostramos el resultado 
# plt.imshow(resultado)
# plt.show()

# Moastramos la imgen de la mujer
# plt.imshow(imagen)
# plt.show()

# Moastramos la imgen del rostro de la mujer
# plt.imshow(imgen_face)
# plt.show()
