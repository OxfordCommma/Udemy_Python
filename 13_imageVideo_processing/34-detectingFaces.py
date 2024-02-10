import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Haarcascade es un archivo xml que guarda toda la información para identificar patrones de rostros
# type = <class 'cv2.CascadeClassifier'>

img = cv2.imread("photo.jpg") # Imagen que queremos identificar un rostro
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Transforma una imagen de RGB a BN y la guarda en la variable

# Vamos a devolver las coordenadas de la cara de la imagen, devuelve un rectángulo que contiene la cara
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05, # Indica que hará una iteración y en cada una, la imagen se achica un 5% para detectar mejor las caras que pueden haber
minNeighbors=5)

for x, y, w, h in faces: #Agarra las coordenadas del rectángulo del rostro
    img = cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 3) # Los usa para dibujar la foto y remarcar el rectángulo (uno verde)

# faces type: numpy.ndarray
print(faces) # [[157  84 379 379]], nos da las coordenadas del  rectángulo

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Face", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

