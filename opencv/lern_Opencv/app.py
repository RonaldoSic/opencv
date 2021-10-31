# IMPORTAMOS UNA IMAGEN RAPIDA Y UN VIDEO Tuturial de YouTube
# https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=10182s 
import cv2
import os
import numpy as np

# Coloca las imagenes en una sola ventana 
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# CAPITULO 1 Codigo para cargar una imagen simple y mostarlo
def CargaImgSimple():
    # CODIGO PARA CARGAR UNA IMAGEN RAPIDA
    ruta = os.getcwd()
    print('Package Imported, la ruta donde estamos es: {}'.format(ruta))
    # CARGAMOS LA IMAGE O LA RUTA DE LA IMAGEN
    img_ruta = str(ruta+"/woman.jpg")
    # LEEMOS LA IMAGEN
    img = cv2.imread(img_ruta)
    img = cv2.resize(img, (1450, 800))
    # MOSTRAMOS LA IMAGEN
    cv2.imshow('Output', img)
    # HACEMOS QUE SE ESPERO PARA PODER MOSTRAR
    cv2.waitKey(0)

# CAPITULO 2 Codigo para leer video de una camara 0 es webcam de pc 1 es camara de otro lado
def LeerWebCam():
    # CODIGO PARA CARGAR UN VIDEO RAPIDO
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  #Ancho
    cap.set(4, 480)  #Alto
    cap.set(10, 100)
    while True:
        success, img = cap.read()
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# CAPITULO 2 CODIGO PARA CREAR IMAGENES CON DIFERENTES EFECTOS
def ImagensConProcesamiento():
    kernel = np.ones((5,5), np.uint8)
    ruta = os.getcwd()
    img_woman = str(ruta+"/adolescence-face.jpg")
    img = cv2.imread(img_woman)
    img = cv2.resize(img, (450,450))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
    img_canny = cv2.Canny(img, 100, 100)
    img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
    img_erode = cv2.erode(img_dialation,kernel,iterations=1)
    # Mostramos la imagenes
    cv2.imshow('Gray Image', img_gray)
    cv2.imshow('Blur Image',img_blur)
    cv2.imshow('Canny Image',img_canny)
    cv2.imshow('Dialation Image',img_dialation)
    cv2.imshow('Erode Image',img_erode)
    cv2.waitKey(0)

# CAPITULO 3 OpenCV Convention
def ResizeImage():
    ruta = os.getcwd()
    # CARGAMOS LA IMAGE O LA RUTA DE LA IMAGEN
    img_ruta = str(ruta+"/family.jpg")
    img = cv2.imread(img_ruta)
    print('Tamanio del img Original {}'.format(img.shape))
    img = cv2.resize(img, (1200, 800))
    img_resize = cv2.resize(img, (800,800))
    print('Tamanio del img Modificado {}'.format(img_resize.shape))
    
    img_cropped = img[0:700, 700:1000]
    
    # Mostrmaos la imagen
    cv2.imshow('Imagen Original', img)
    cv2.imshow('Imagen Modificado', img_resize)
    cv2.imshow('Imagen Recorado', img_cropped)
    cv2.waitKey(0)

# CHAPTER 4 SHAPES AND TEXTS 
def DibijarEscribirEnImg():
    img_black = np.zeros((512,512, 3),np.uint8)
    # print(img_black)
    # segmentanod una parte en la primera posicion que es BGR [0]=Blue, [1]=Green, [2]=Red
    # img_black[200:300, 100:300] = 255,0,0  # Segmento azul
    # img_black[:] = 255,0,0  # todo de azul
    
    # Dibujamos una linea
    cv2.line(img_black, (0,0), (300,300), (0,0,255),3)
    # Para abarcar todo el ancho y el alto en una imagen se usa 
    cv2.line(img_black, (0,0), (img_black.shape[0],img_black.shape[1]), (0,0,255),3)
    
    # Dibujarmos un rectangulo 
    cv2.rectangle(img_black, (0,0), (250,350), (0,255,0),2)
    # para rellenar un rectangulo de color se hace 
    # cv2.rectangle(img_black, (0,0), (250,350), (0,255,0),cv2.FILLED)
    
    # Dibujarmos un curculo
    cv2.circle(img_black, (400, 50), 30, (255,30,200), cv2.FILLED)
    
    # Colocamos texto en la imagen
    cv2.putText(img_black, 'OPENCV', (300,200), cv2.FONT_HERSHEY_COMPLEX, 1.2,(25,180,200), 2)  #, cv2.FILLED)
    # mostramos la imagen    
    cv2.imshow('Imagen Negra', img_black)
    cv2.waitKey(0)

# CHAPTER 5 WARP PRESPECTIVE
def PerpectivasEnImagenes():
    ruta = os.getcwd()
    img_ruta = str(ruta+"/Cartas.jpg")
    img = cv2.imread(img_ruta)
    width, height = 1400,800 
    puntos1 = np.float32([[200,148],[270,603],[566,120],[668,544]])
    puntos2 = np.float32([[0,0],[width, 0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(puntos1, puntos2)
    img_output = cv2.warpPerspective(img, matrix, (width, height))
    # Mostramos la imagen
    cv2.imshow('Imgen Original', img)
    cv2.imshow('Imgen Perpective', img_output)
    cv2.waitKey(0)

# CHAPTER 6 JOINING IMAGES
def UniendoImagenes():
    ruta = os.getcwd()
    img_ruta = str(ruta+"/Cartas.jpg")
    img = cv2.imread(img_ruta)
    img = cv2.resize(img,(600,450))
    # Transformamos la imagen en Horizontal y Vertical
    img_horizontal = np.hstack((img, img))
    img_vertical = np.vstack((img, img))
    
    # Mostramos las imagenes
    cv2.imshow('Horizontal', img_horizontal)
    cv2.imshow('Vertical', img_vertical)
    cv2.waitKey(0)

# CHAPTER 7 COLOR DETECION 
# Funcion Vacia
def empty(a):
    pass
def DeteccionDeColores():
    ruta = os.getcwd()
    img_ruta = str(ruta+"/yellow-sports-car.jpg")
    
    # Creando una ventana con CV2 que nos ayude a detectar las variaciones de colores o rangos
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640,240)
    cv2.createTrackbar('Hue Min', 'TrackBars',0, 179,empty)
    cv2.createTrackbar('Hue Max', 'TrackBars',179, 179,empty)
    cv2.createTrackbar('Sat Min', 'TrackBars',118, 255,empty)
    cv2.createTrackbar('Sat Max', 'TrackBars',255, 255,empty)
    cv2.createTrackbar('Val Min', 'TrackBars',128, 255,empty)
    cv2.createTrackbar('Val Max', 'TrackBars',235, 255,empty)
    
    # Para que la imagen se lea constantemente 
    while True:
        img = cv2.imread(img_ruta)
        img = cv2.resize(img,(600,450))
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
        # Leemos los valors que se obtien en la venta creada 
        hue_min = cv2.getTrackbarPos(trackbarname="Hue Min",winname="TrackBars")
        hue_max = cv2.getTrackbarPos(trackbarname="Hue Max",winname="TrackBars")
        sat_min = cv2.getTrackbarPos(trackbarname="Sat Min",winname="TrackBars")
        sat_max = cv2.getTrackbarPos(trackbarname="Sat Max",winname="TrackBars")
        val_min = cv2.getTrackbarPos(trackbarname="Val Min",winname="TrackBars")
        val_max = cv2.getTrackbarPos(trackbarname="Val Max",winname="TrackBars")
        print(hue_min, hue_max,sat_min,sat_max,val_min,val_max)
        # Creamos arreglos con los valores que se captan en el TrackBars
        lower = np.array([hue_min,sat_min,val_min])
        upper = np.array([hue_max,sat_max,val_max])
        mask = cv2.inRange(img_HSV, lowerb=lower, upperb=upper)
        # Transformamos la mascara en la imagen Original nuevamente
        img_result = cv2.bitwise_and(img, img, mask=mask)
        
        # Mostramos las imagenes
        # cv2.imshow('Imagen Original',img)
        # cv2.imshow('Imagen HSV',img_HSV)
        # cv2.imshow('Imagen Variada',mask)
        # cv2.imshow('Imagen Resultado',img_result)
        
        imgStack = stackImages(0.6,([img,img_HSV],[mask,img_result]))
        cv2.imshow("Stacked Images", imgStack)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# Obtener Colores en Video
def GetColorInVideo():
    frameWidth = 450
    frameHeight = 400
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(1)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10,150)
    
    
    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV",640,240)
    cv2.createTrackbar("HUE Min","HSV",0,179,empty)
    cv2.createTrackbar("SAT Min","HSV",0,255,empty)
    cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
    cv2.createTrackbar("HUE Max","HSV",179,179,empty)
    cv2.createTrackbar("SAT Max","HSV",255,255,empty)
    cv2.createTrackbar("VALUE Max","HSV",255,255,empty)
    
    
    while True:
        _, img = cap.read()
        imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("HUE Min","HSV")
        h_max = cv2.getTrackbarPos("HUE Max", "HSV")
        s_min = cv2.getTrackbarPos("SAT Min", "HSV")
        s_max = cv2.getTrackbarPos("SAT Max", "HSV")
        v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
        v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
        print(h_min)

        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        mask = cv2.inRange(imgHsv,lower,upper)
        result = cv2.bitwise_and(img,img, mask = mask)

        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        hStack = np.hstack([img,mask,result])
        #cv2.imshow('Original', img)
        #cv2.imshow('HSV Color Space', imgHsv)
        #cv2.imshow('Mask', mask)
    #cv2.imshow('Result', result)
        cv2.imshow('Horizontal Stacking', hStack)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# CHAPTER 8 CONTOUTS / SHAPE DETECTION and asignate Name to shape
def getContours(img,copy_img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # Con la variable area nos indica las cordenadas de sonde se encotraron contornos de la imagen dada por Canny
        area = cv2.contourArea(cnt)
        # print(area)
        if area>500:
            # Dibujamos un contorno de fomra de rectangulo por cada objbeto que detectamos
            img_contour = cv2.drawContours(copy_img, cnt, -1,(255,55,185), thickness=3)
            peri = cv2.arcLength(cnt, True)            
            # print("El valor de peri es {}".format(peri))
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # print("El valor de approx es {}".format(approx))
            # Creamos un objeto con esquinas
            obj_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            
            if obj_corners == 3: 
                objectType = "Triangulo"
            elif obj_corners == 4:
                aspect_ratio = w/float(h)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                    objectType = 'Cuadrado'
                else: objectType = 'Rectangulo'
            elif obj_corners>4: objectType= 'Circulo'
            else: objectType = 'None'
            
            
            # Dibujamos un rectangulo en cada objeto detectado para encerrarlo
            img_contour = cv2.rectangle(img_contour, (x,y),(x+w, y+h), (0,255,0),2)
            img_contour = cv2.putText(img_contour, objectType, (x+(w//2)-10, y+(h//2)-10),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
            
            
            
    return(img_contour)

def ReconocimientoDeContoronos():
    ruta = os.getcwd()
    img_ruta = str(ruta+"/shapes.png")
    img_read = cv2.imread(img_ruta)
    img_with_contour = img_read.copy()
    # Convertimos la imgen en gris
    img_gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
    img_canny = cv2.Canny(img_blur, 50,50)
    # Obtenemos los contornos
    new_img_contour = getContours(img_canny, img_with_contour)
    # Creamos una imagen axuliar
    img_black = np.zeros_like(img_read);
    # Mostramos las imagens
    img_stack = stackImages(0.4,([img_read, img_gray, img_blur],
                                    [img_canny,new_img_contour,img_black]))
    # cv2.imshow('Imagen Original',img_read)
    cv2.imshow('Todas las imagenes',img_stack)
    
    
    cv2.waitKey(0)

# CHAPTER 9 FACE DETECTION
def ReconocimientoDeRostros():
    # Cargamos la imagen y el archivo xml para detectar los rostros
    path = os.getcwd()
    img_ruta = str(path+"/adolescence-face.jpg")
    file_cascade = str(path+"/haarcascade_frontalface_default.xml")
    # leemos las rutas de la imagen y del archivo xml con cv2
    face_cascade = cv2.CascadeClassifier(file_cascade)
    # print("Face cascade {}".format(face_cascade))
    img_read = cv2.imread(img_ruta)
    img_read = cv2.resize(img_read,(1200,860))
    # Converimos la imagen a escala de grises
    img_gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    
    # Dibujamos un rectangulo por los rostros que detectamos
    for (x,y,w,h) in faces:
        cv2.rectangle(img_read, (x,y),(x+w, y+h), (255,255,255),3)

    cv2.imshow('Rostro detectado', img_read)
    cv2.waitKey(0)

# PROJECT 1 VIRTUAL PAINT Fail Here 
# Array de los colores que se queiren detectar en este caso el naranja palido y celeste paslido
    # El primer array es para el color Verde
    # El segundo arra es para el color Amarillo
    # El tercero es para el color Celeste
coloresADetectar = [[0,184,21,90,255,255],[21,106,120,46,255,255],[97,235,0,179,255,255]]
# Colores a usar para pintar estan en BGR y no en RGB
"""El arreglo es para los colores que van a pintar en la pantall el primero es para el color 
    Naranja, el segundo es para el color Celeste, y el tercero es pera el color Amarillo"""
colores_pintar =[[20,194,3],
                [1,255,251],
                [255,217,1]]
myPoints = []  #[x, y, colorId]
count = 0
# Funcion para detectar el color de los objetos
def FindColor(img, myColors, imgCopy):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(src=imgHSV, lowerb=lower, upperb=upper)
        # cv2.imshow(str(color[0]), mask)
        x,y, new_img = ContornosImg(mask,imgCopy)
        cv2.circle(new_img, (x,y),10,colores_pintar[count],cv2.FILLED)
        if x != 0 and y !=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints

def ContornosImg(img,copy_img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    img_contour = copy_img
    for cnt in contours:
        # Con la variable area nos indica las cordenadas de sonde se encotraron contornos de la imagen dada por Canny
        area = cv2.contourArea(cnt)
        # print(area)
        if area>500:
            # Dibujamos un contorno de fomra de rectangulo por cada objbeto que detectamos
            img_contour = cv2.drawContours(copy_img, cnt, -1,(197,0,255), thickness=3)
            peri = cv2.arcLength(cnt, True)            
            # print("El valor de peri es {}".format(peri))
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)            
            # Creamos un objeto con esquinas
            obj_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)   
    return x+w//2, y, img_contour                                                 
    # return(img_contour)

def DibujarEnPantalla():
    frameWidth = 640
    frameHeight = 640
    # Empezamos a capturar el video de la webacam
    capturar = cv2.VideoCapture(0)
    # Definimos el tamanio de la ventana
    capturar.set(3, frameWidth)
    capturar.set(4, frameHeight)
    capturar.set(10,100)
    
    while True:
        success, imagen = capturar.read()
        imgCopia = imagen.copy();
        newPoint = FindColor(img=imagen, myColors= coloresADetectar, imgCopy=imgCopia)
        if len(newPoint) !=0:
            for newP in newPoint:
                myPoints.append(newP)
        if len(myPoints) !=0:
            DrawOnCanvas(myPoints, myColorsValues=colores_pintar, img=imgCopia)
        cv2.imshow('Video', imgCopia)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        
    cv2.destroyAllWindows()

def DrawOnCanvas(myPoints, myColorsValues, img):
    for point in myPoints:
        new_img = cv2.circle(img, (point[0], point[1]),10,colores_pintar[point[2]],cv2.FILLED)
    


# Probando con mi propio archivo xml para clasificar botellas
def ReconocerBotellas():
    # Cargamos la imagen y el archivo xml para detectar los rostros
    path = os.getcwd()
    img_ruta = str(path+"/botella.jpg")
    # file_cascade = str(path+"/haarcascade_botella.xml")    
    file_cascade = str(path+"/haarcascade_eye.xml")   
    # file_cascade = "C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/haarcascade_botella.xml" 
    # C:/Users/User/Documents/Mi Escritorio/PROGRAMAS/Programas Python/OpenCV/
    print('la ruta {}'.format(file_cascade))
    # leemos las rutas de la imagen y del archivo xml con cv2
    botella_cascade = cv2.CascadeClassifier(file_cascade)
    print("La cascade de botellas es {}".format(botella_cascade))
    img_read = cv2.imread(img_ruta)
    img_read = cv2.resize(img_read,(400,400))
    # Converimos la imagen a escala de grises
    img_gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
    botellas = botella_cascade.detectMultiScale(img_gray, 1.01, 7)
    
    # Dibujamos un rectangulo por los rostros que detectamos
    for (x,y,w,h) in botellas:
        cv2.rectangle(img_read, (x,y),(x+w, y+h), (255,255,255),3)

    cv2.imshow('Botella detecado', img_read)
    cv2.waitKey(0)


# CargaImgSimple()
LeerWebCam()
# ImagensConProcesamiento()
# ResizeImage()
# DibijarEscribirEnImg()
# PerpectivasEnImagenes()
# UniendoImagenes()
# DeteccionDeColores()
# ReconocimientoDeContoronos()
# ReconocimientoDeRostros()
# ReconocerBotellas()
# DibujarEnPantalla()
# GetColorInVideo()