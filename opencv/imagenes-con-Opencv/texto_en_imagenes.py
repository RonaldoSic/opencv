# Crear texto sobre una imagen con OpenCV desde Python
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
adolescence_woman = os.getcwd()+'/adolescence.jpg'
imagen_fondo_negro = np.zeros(shape=(800, 900, 3), dtype=np.int)

# Leyendo la imagen de la mujer
imagen = cv2.imread(adolescence_woman);
# Modificando el oreden de los colres 
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
# Seleccion de un tipo de fuente de texto
fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX;
# Funcion para colocar el texto en la imagen que se quiere mostrar
"""
    Se le pasa la image que se quiere modifiacar, el texto que se quiere mostrar, en el 
    campo de org(), se le pasa las cordenadas de donde empieza el texto, 
    se la pasa el timpo de fuente que se ha elegido, y se le pasa el grosor por ultimo el tipo de linea que se va amostrar.
"""
imagen_con_texto = cv2.putText(imagen, text='Im Yiveli', org=(400,800), 
                                fontFace=fuente, fontScale=10, color=(0,255,0),
                                thickness=10, lineType=cv2.LINE_8)

otra_fuete = cv2.FONT_HERSHEY_DUPLEX;
texto_msj = 'Hola esto es OpenCV'
imagen_fondo_negro = cv2.putText(imagen_fondo_negro, text=texto_msj,
                                org=(10,100), fontFace= otra_fuete, 
                                fontScale=2, color=(0,0,255), thickness=4, 
                                lineType=cv2.LINE_AA)

# Creacion de un poligano 
# Vertices del poligono
vertices = np.array([[100, 300], [300, 200], [400, 400], [200, 400]], dtype = np.int)
print('Forma {}'.format(vertices.shape))

# Modificamos la forma de los vertices y se pasa a 3 Dimensiones asi
puntos = vertices.reshape(-1, 1, 2)
print('Nueva forma de 3D {}'.format(puntos.shape))

# Creamos la fomra
imagen_fondo_negro = cv2.polylines(imagen_fondo_negro, [puntos], isClosed= True,
                                    color=(255,255,255), thickness=6)

# Mostrar imagen de la mujer con texto
# plt.imshow(imagen_con_texto);
# plt.show()

# Mostrar imagen de fondo negro con el texto
plt.imshow(imagen_fondo_negro);
plt.show()
