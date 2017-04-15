import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image_name = 'news.jpg'

img = cv2.imread(image_name)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray_img,
  scaleFactor=1.1,
  minNeighbors=5)

print(type(faces))
print(faces)


for x, y, w, h in faces:
  new_img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

cv2.imwrite("detected_"+image_name, new_img)


cv2.imshow("Gray", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()