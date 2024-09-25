import cv2

image = cv2.imread("image.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
haarcascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_rect = haarcascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=9)
for x, y, width, height in face_rect:
    cv2.rectangle(image, (x, y), (x+width, y+height), (0, 0, 0), 5)
cv2.imshow("ho", image)
if cv2.waitKey(0):
    cv2.destroyAllWindows()