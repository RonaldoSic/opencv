# Leer videos
import cv2
# Importamo el video con su ruta asi
my_video = 'C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/video.mp4'
# Creamos la variable que haara la captura del vido
captura = cv2.VideoCapture(my_video)

# Verificamos si se abrio el video 
if captura.isOpened() == False:
    print('Erro al abrir el Fichero de video')
    
while True:
    result, video = captura.read()
    if result == True:
        cv2.imshow('Mi Video', video)        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Borramos toda la informacion de la captura
captura.release()
# Cerramos todas la ventanas que se han creado
cv2.destroyAllWindows()

