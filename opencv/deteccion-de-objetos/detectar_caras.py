# Deteccion de caras  y ojos en una imagen
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Archivo donde esta las caracteristicas de las caras
caracteristicas_cara_xml = os.getcwd()+'/haarcascade_frontalface_default.xml'
# Archivo donde esta las caracteristicas de los ojos en xml
caracteristicas_ojos_xml = os.getcwd()+'/haarcascade_eye.xml'

# Cargamos las imagenes que se utilizan
woman = os.getcwd()+'/adolescence.jpg'
family = os.getcwd()+'/family.jpg'
# Se leen las imagenes en escala de grises
imagen_mujer = cv2.imread(woman)
imagen_familia = cv2.imread(family)

# Cargamaos las caracteristicas para que se detecte una cara frontal
cascada_cara = cv2.CascadeClassifier(caracteristicas_cara_xml)
# cargamos las caracteristicas para que se detecten los ojo en una cara
cascada_ojos = cv2.CascadeClassifier(caracteristicas_ojos_xml)


# Creamos una funcion que detecata las caras frontales en una imagen
def detectar_cara (imagen):
    imagen_copy = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen_copy)
    # dibujamos los rectangulos en la imagen
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen_copy, (x,y), (x+w, y+h), (255,0,0), 10)
    return imagen_copy    


# Creamos una funcion que detecata los ojos en una caras frontal en una imagen
def detectar_ojos (imagen):
    imagen_copy = imagen.copy()
    rectangulos = cascada_ojos.detectMultiScale(imagen_copy)
    # dibujamos los rectangulos en la imagen
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen_copy, (x,y), (x+w, y+h), (255,255,255), 10)
    return imagen_copy    

# Aplicamos la funcion a cada imagen
# Para la cara de la Mujer
resultado = detectar_cara(imagen_mujer)
resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)
plt.imshow(resultado)
plt.show()

# Para las caras de la familia
resultado = detectar_cara(imagen_familia)
resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)
plt.imshow(resultado)
plt.show()

# Aplicamos la funcion de detectar los ojos 
result_ojos = detectar_ojos(imagen_mujer)
result_ojos = cv2.cvtColor(result_ojos, cv2.COLOR_BGR2RGB)
plt.imshow(result_ojos)
plt.show()

# Aplicamos la funcion de detectar los ojos a la imagen de la familia
result_ojos = detectar_ojos(imagen_familia)
result_ojos = cv2.cvtColor(result_ojos, cv2.COLOR_BGR2RGB)
plt.imshow(result_ojos)
plt.show()

# imagen con 1 rotstro 
# plt.imshow(imagen_mujer, cmap='gray')
# plt.show()
# Imagen con mas de 2 rostros
# plt.imshow(imagen_familia, cmap='gray')
# plt.show()