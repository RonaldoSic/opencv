# Dibujar con el arrastrar el mouse sobre una imagen
import numpy as np
import cv2
# Variables globales
are_you_drawing = False
valor_x = 0
valor_y = 0

# Funcion para dibujar con el arraste del raton
def dibujar(event, x, y, etiquetas, parametros):
    # Con esto le digo a la funcion que user las variable globales en la funcion
    global are_you_drawing, valor_x, valor_y
    if event == cv2.EVENT_LBUTTONDOWN:
        are_you_drawing = True
        valor_x = x
        valor_y = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if are_you_drawing:
            cv2.rectangle(img_lienzo,pt1=(valor_x, valor_y), 
                            pt2=(x,y), color=(255,0,0), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        are_you_drawing = False
        cv2.rectangle(img_lienzo,pt1=(valor_x, valor_y), 
                            pt2=(x,y), color=(255,0,0), thickness=-1)

# Conectamos la funcion dibujar con la image
cv2.namedWindow(winname="Mi Lienzo")
cv2.setMouseCallback("Mi Lienzo", dibujar)
# Creamos la imagen de fondo negro
img_lienzo = np.zeros(shape=(500,500, 3), dtype=np.int8)
tecla_esc = 27;  # Se define el valor de la tecla de ESC
while True:
    cv2.imshow("Mi Lienzo", img_lienzo)
    if cv2.waitKey(10) & 0xFF == tecla_esc:
        break

cv2.destroyAllWindows()