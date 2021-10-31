""" 
import cv2
import os
import mediapipe as mp
LABELS = ["Con_mascarilla", "Sin_mascarilla"]
def main():
  mp_face_detection = mp.solutions.face_detection
  # leer el modelo
  # Leer el modelo
  face_mask = cv2.face.LBPHFaceRecognizer_create()
  face_mask.read("face_mask_model.xml")
  cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

  mp_face_detection.FaceDetection(min_detection_confidence=0.5) 
  as face_detection:

    while True:
      ret, frame = cap.read()
      if ret == False: break
      frame = cv2.flip(frame, 1)
      height, width, _ = frame.shape
      frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      results = face_detection.process(frame_rgb)          ret, frame = cap.read()
      if ret == False: break
      frame = cv2.flip(frame, 1)
      height, width, _ = frame.shape
      frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      results = face_detection.process(frame_rgb)
      break

  # LeerWebCam()

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
"""

import cv2
import os
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

LABELS = ["Con_mascarilla", "Sin_mascarilla"]
# cargar el modelo 
# modelo_entrenado = os.getcwd()+"/face_mask_model.xml"
modelo_entrenado2 = os.getcwd()+"/mascarillas_model.xml"
# print(modelo_entrenado)
print(modelo_entrenado2)

# Leer el modelo
face_mask = cv2.face.LBPHFaceRecognizer_create()
# face_mask.read("face_mask_model.xml")
face_mask.read(modelo_entrenado2)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(
  min_detection_confidence=0.5) as face_detection:
  while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame, 1)

    height, width, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)

    if results.detections is not None:
      for detection in results.detections:
        xmin = int(detection.location_data.relative_bounding_box.xmin * width)
        ymin = int(detection.location_data.relative_bounding_box.ymin * height)
        w = int(detection.location_data.relative_bounding_box.width * width)
        h = int(detection.location_data.relative_bounding_box.height * height)
        if xmin < 0 and ymin < 0:
          continue
        
        # cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 5)
        face_image = frame[ymin : ymin + h, xmin : xmin + w]
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        face_image = cv2.resize(face_image, (72, 72), interpolation=cv2.INTER_CUBIC)
        
        result = face_mask.predict(face_image)
        #cv2.putText(frame, "{}".format(result), (xmin, ymin - 5), 1, 1.3, (210, 124, 176), 1, cv2.LINE_AA)
        if result[1] < 150:
          color = (0, 255, 0) if LABELS[result[0]] == "Con_mascarilla" else (0, 0, 255)
          cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)
          cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    
    if k == 27:
      break

cap.release()
cv2.destroyAllWindows()
