# Vamos a detectar una cara usando un video (como un .mp4). En este caso, desde la cámara web.

import cv2, time

video = cv2.VideoCapture(0) #0 como argumento para decir que nos referimos a nuestra cámara web

a = 1

while True:

    a = a + 1

    check, frame = video.read() # Vemos que info nos da el video
    print(check) # Un booleano, si el video corre o no
    print(frame) # Un array, que imprime la primer imagen que toma la cámara (capturada por "video.read()")

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) Si quiero, transformo la 1ra imagen en BN

    #time.sleep(1) #Para verificar que la cámara se prenda cuando se ejecuta el script

    cv2.imshow("Capturing", frame) # Muestra la imagen primera. Si quiero la imagen BN, cambio "frame" por "gray"
    
    key = cv2.waitKey(10) # 10 es un número normal para una fluidez de fotogramas

    if key == ord("q"): # si toco la tecla "q", se cierra el programa
        break

print(a) #Cuenta las veces que se itera en un Run. Con ello, después calculamos los fotogramas por segundo

video.release()

cv2.destroyAllWindows