# Dibujar en videos
import cv2

# Creamos la variable que captura la imagen el 0 indica que leera lo de la webcam
captura = cv2.VideoCapture(0)
# Se captura el alto y el ancho del video
ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Esquina Izquierda del rectangulo
x = 330
y = 230

# Dimensiones del rectangulo
w = ancho // 4  # Para que sea un numero entero se usa // barra
h = alto // 4


while True:
    result, video = captura.read()
    # Dibujamos el rectangulo
    cv2.rectangle(video,(x,y), (x+w, y+h), color=(255,0,0), thickness=4)
    cv2.imshow('Video con Rectangulo', video)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Borramos toda la informacion de la captura
captura.release()
# Cerramos todas la ventanas que se han creado
cv2.destroyAllWindows()