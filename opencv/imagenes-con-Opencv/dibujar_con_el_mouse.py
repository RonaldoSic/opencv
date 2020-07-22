# Dibujar con el dar un Clic del mouse sobre una imagen
import numpy as np
import cv2
# Funcion para dibujar con el raton
def dibujar(event, x, y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_lienzo, center=(x,y), radius=50, color=(255,255,255), thickness=-1)

# Creamos la imagen de fondo negro
img_lienzo = np.zeros(shape=(500,500, 3), dtype=np.int8)
tecla_esc = 27;  # Se define el valor de la tecla de ESC

# Conectamos la funcion con la imagen
cv2.namedWindow(winname='Mi Lienzo')  # Lo que hace es buscar una ventana con el mismo nombre
cv2.setMouseCallback('Mi Lienzo', dibujar)  #Le damos el nombre de la ventana a buscar y llamanos la funcion a ejecutar

# Mostramos la imagen donde vamos a pintar
# Mientras Todo este en True que se muestre la imagen
while True:
    cv2.imshow('Mi Lienzo', img_lienzo)  # Leemos la image para mostrarlo en el bucle
    if cv2.waitKey(10) & 0xFF == tecla_esc:  #Si se preciona ESC se cierra todo
        break
    
# Al finalizar el bucle se cierran las ventas 
cv2.destroyAllWindows()




