# Conectarse a la camara y grabar video
import cv2
# Creamos la variable que haara la captura del vido
captura = cv2.VideoCapture(1)
# capturamos y asignamos el ancho y el alto del video
ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
# versionse de video 
# Version para PC MAC
# codigo = cv2.VideoWriter_fourcc(*'MJPG')  # aceptamos todos los formatos con extension MJPG
# Le pasamos el nombre del video con el que se grarda el codigo, y los fotogramas, el alto y ancho
# grabador = cv2.VideoWriter('video.avi', codigo, 20, (ancho,altura))

# Version para PC Windows
codigo = cv2.VideoWriter_fourcc(*'DIVX')  # aceptamos todos los formatos con extension MJPG
# Le pasamos el nombre del video con el que se grarda el codigo, y los fotogramas, el alto y ancho
grabador = cv2.VideoWriter('video.mp4', codigo, 20, (ancho,altura))

# Mostramos el video
while True:
    # Asignamo en una variable video lo que leemos en la camptura 
    resultado, video = captura.read()
    # Grabamos el video
    grabador.write(video)
    # Mostramos el video con el nombre de la ventana, y le pasamos la variable Video
    cv2.imshow('El Video', video)
    # Configuramos una letra que indicara la salida o que cierra la ventana del video
    # La letra que hara que cierre sera la letra 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break                

# Borramos toda la informacion de la captura
captura.release()
# Limpiamos el grabador
grabador.release()
# Cerramos todas la ventanas que se han creado
cv2.destroyAllWindows()

