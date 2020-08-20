# Detectar Rostros en un video
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Archivo donde esta las caracteristicas de las caras
# caracteristicas_cara_xml = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/haarcascade_frontalface_default.xml'
# Archivo donde esta las caracteristicas de los ojos en xml
# caracteristicas_ojos_xml = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/haarcascade_eye.xml'

caracteristicas_cara_xml = os.getcwd()+'/haarcascade_frontalface_default.xml'
caracteristicas_ojos_xml = os.getcwd()+'/haarcascade_eye.xml' 
# Cargamaos las caracteristicas para que se detecte una cara frontal
cascada_cara = cv.CascadeClassifier(caracteristicas_cara_xml)
# cargamos las caracteristicas para que se detecten los ojo en una cara
cascada_ojos = cv.CascadeClassifier(caracteristicas_ojos_xml)
# color del rectangulo de las caras
color_rectangle = (145, 255, 245)
# color del rectangulo de las ojos
color_rect = (254, 226, 97)

# Funcion para detectar los rostros en el video
def detectar_cara (imagen):
    img_copy = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(img_copy)
    for (x,y,w,h) in rectangulos:
        cv.rectangle(img_copy,pt1= (x,y),pt2=(x+w, y+h), color=color_rectangle, thickness=4)
    return img_copy

# Creamos una funcion que detecata los ojos en una caras frontal en una imagen
def detectar_ojos (imagen):
    imagen_copy = imagen.copy()
    rectangulos = cascada_ojos.detectMultiScale(imagen_copy)
    # dibujamos los rectangulos en la imagen
    for (x,y,w,h) in rectangulos:
        cv.rectangle(imagen_copy, (x,y), (x+w, y+h),color_rect, 2)
    return imagen_copy    


# Campturamos la imagen de la video camara
captura = cv.VideoCapture(0)

while True:
    res, video = captura.read()
    # Cargamos la funcion de detectar caras al video
    video = detectar_cara(video)
    video = detectar_ojos(video)
    # Mostramos el video
    cv.imshow('Detectar Rostros', video)
    tecla = cv.waitKey(1)
    if tecla == 27:
        break

# Limpiamos y destruimos todas la ventanas creadas
captura.release()
cv.destroyAllWindows()
