import cv2

image = cv2.imread("we.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
haarcascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
face_rect = haarcascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=3)
for x, y, width, height in face_rect:
    cv2.rectangle(image, (x, y), (x+width, y+height), (0, 0, 0), 5)
cv2.imshow("vghvbnhvggn", image)
if cv2.waitKey(0):
    cv2.destroyAllWindows()