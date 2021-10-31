import cv2
import os
import numpy as np
import sys

data_path = os.getcwd()+'./Face_Mask_Dataset/Test'
if os.path.exists(data_path):  
  dir_list = os.listdir(data_path)
  print("Lista directorios y archivos:", dir_list)
  labels = []
  facesData = []
  label = 0
  for name_dir in dir_list:
    print (name_dir)
    sub_dir = data_path +"/" + name_dir;
    print ("Sub dir, ",{sub_dir})
    for file_name in os.listdir(sub_dir):
      imagen_path= sub_dir + "/" + file_name
      print ("Image File name, ",{imagen_path})
      imagen_redimencionada = cv2.resize(imagen_path, (72,72))
      imagen = cv2.imread(imagen_redimencionada)
      image = cv2.imread(imagen_path)
      cv2.imshow("Imagenes", image)
      cv2.waitKey(10)
      facesData.append(image)
      labels.append(label)
    label += 1  
  
  print("Etiqueta 0: ", np.count_nonzero(np.array(labels) == 0))
  print("Etiqueta 1: ", np.count_nonzero(np.array(labels) == 1))
  # LBPH FaceRecognizer
  face_mask = cv2.face.LBPHFaceRecognizer_create()
  
  # Entrenamiento
  print("No molestar estoy entrenando ahora ... 😆💪")
  face_mask.train(facesData, np.array(labels))
  
  # Almacenar modelo
  # face_mask.write("mascarillas_model.xml")
  print("El modelo ya esta listo y etrenado 😎")
  

else:
  print("👎 NO ES POSIBLE CARGAR LOS DATOS PARA EL ENTRENAMIENTO, {}".format(data_path))
  sys.exit(1)




