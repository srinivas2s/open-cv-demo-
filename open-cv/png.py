import cv2

img = cv2.imread("cat.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(img, (20, 20))
crop = img[15:200, 100:400]   # img[y1:y2, x1:x2]
cv2.circle(img, (320, 300), 88, (255, 0, 0), 3)
cv2.line(img, (0, 0), (400, 400), (0, 0, 255), 2)
cv2.putText(img, "Billa gang ", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
cv2.rectangle(img, (10, 5), (210, 20), (123, 251, 44), 3)
cv2.imshow("Image Window", img)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()