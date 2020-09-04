import os
import numpy as np
import cv2
import picamera 
"""
  Formas de crear un modulo o una plicacion modular para, donde para 
  implementarlos en el codigo se pueden hacer de dos formas que son:
"""
# Forma 1
# from manejo_cordenadas import saludar
# saludar("Este mensaje lo mando desde el modulo")
# Forma 2
import manejo_cordenadas as mcs
# mcs.saludar('Modulo activado')

file_xml = os.getcwd()+'/haarcascade_frontalface_default.xml'
# print("Rura unificada {}".format(file_xml))

load_haar = cv2.CascadeClassifier(file_xml)

color_rectangle = (82,250,150)

def found_faces(img):
    img_copy = img.copy()
    rectangle = load_haar.detectMultiScale(img_copy)
    for (x, y, w, h) in rectangle:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), 2)
        mcs.getCordenadas(x, y, w, h)
    return img_copy

cap = cv2.VideoCapture(0)

while True:
    _, video = cap.read()
    video = found_faces(video)
    # Mostramos el video
    cv2.imshow('Detectar Rostros', video)
    tecla = cv2.waitKey(1)
    if tecla == 27:
        break

cap.release()
cv2.destroyAllWindows()
