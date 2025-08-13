import cv2

cat_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
image = cv2.imread("depositphotos_78211934-stock-photo-man-with-red-cat.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in cats:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2) # кот обводится синим
humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in humans:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  # человек обводится зелёным
cv2.imshow("Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
