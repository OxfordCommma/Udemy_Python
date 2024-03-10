""" Vamos a hacer una app que nos muestre la diferencia entre el primer frame (el fondo sólo, sin nada)
y otro en el que estemos nosotros. La app identificará si el nuevo frame contiene o no un nuevo elemento
u objeto en base a compararlo con la imagen base.
"""

import cv2, time, pandas
from datetime import datetime

first_frame = None # Declaramos esta variable, que guardará el 1er frame
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"]) # Tabla de Pandas, que indica la llegada de un objeto al frame y su salida

video = cv2.VideoCapture(0) #0 como argumento para decir que nos referimos a nuestra cámara web

while True:

    check, frame = video.read() # Vemos que info nos da el video
    status = 0 # Variable que identifica si hay un objeto nuevo en el frame

    #print(check) # Un booleano, si el video corre o no
    #print(frame) # Un array, que imprime la primer imagen que toma la cámara (capturada por "video.read()")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #transformo la 1ra imagen en BN
    gray = cv2.GaussianBlur(gray, (21, 21), 0) # Para reducir el ruido de la 1er imagen

    if first_frame is None: 
        first_frame = gray # Si no hay primer frame, entonces asignemoslo al BN. Ocurre en la 1ra iteración
        continue # Cuando se obtiene el 1er frame, se itera nuevamente. No quiero que se ejecute imshow con el 1er frame, porque no lo quiero usar para eso (lo quiero tener como referencia solamente)

    delta_frame = cv2.absdiff(first_frame, gray) # Devuelve una imagen que fue comparada entre la 1er imagen y la actual imagen    
    thresh_frame = cv2.threshold(delta_frame, 80, 255, cv2.THRESH_BINARY)[1] #Método que dice que si hay una diferencia de 30 entre los colores de gray y 1st frame (delta_frame), se pinte de blanco (255)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) # Hace mas smooth las partes blancas (de contraste > 30)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Encuentra los contornos externos (representados como listas de puntos) en thresh_frame. Guarda los contornos en una tupla

    for contour in cnts:
        if cv2.contourArea(contour) < 1000: #Si el área de un contorno es menor a 1000 no pasa nada
            continue
        status = 1 # Si hay un nuevo objeto, se cambia a 1
        (x, y, w, h) = cv2.boundingRect(contour) # Si es mayor a 1000, se obtienen las ubicaciones
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3) # Y con las ubicaciones, se dibuja el rectángulo

    status_list.append(status) # Guarda en la lista, un 0 o un 1 dependiendo si en el frame aparece o no un objeto

    if status_list[-1] == 1 and status_list[-2] == 0: # Si hay discrepancia entre el último y anteúltimo número (aparece un objeto), se registra el horario
        times.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2] == 1: # Lo contrario, si el objeto sale del frame
        times.append(datetime.now())

    cv2.imshow("Gray frame", frame) # Muestra las imagenes BN
    cv2.imshow("Delta frame", delta_frame) # Muestra las imagenes y cómo se comparan con el 1er frame
    cv2.imshow("Threshold Frame", thresh_frame) # Muestra las imagenes con el contraste Blanco si hay diferencia entre imagenes (actual y 1° frame)
    cv2.imshow("Color Frame", frame)
    
    key = cv2.waitKey(10) # 10 es un número normal para una fluidez de fotogramas

    if key == ord("q"): # si toco la tecla "q", se cierra el programa
        if status == 1: # Si sacamos el programa y justo había un objeto
            times.append(datetime.now()) # Indicamos igual la hora de salida del objeto, cuando se cierra el programa
        break

    print(status)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index = True)

df.to_csv("Times.csv")

video.release()

cv2.destroyAllWindows