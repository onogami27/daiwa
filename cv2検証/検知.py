import cv2

img = cv2.imread(r"C:\Users\60837\Desktop\ocv\pos\poss_1.jpg")
cll = cv2.CascadeClassifier(r"C:\Users\60837\Desktop\ocv\cascade\cascade.xml")
aaa = cll.detectMultiScale(image=img,scaleFactor=1.1)
print(aaa)

for (ex,ey,ew,eh) in aaa:
    cv2.rectangle(img , (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
cv2.imshow("",img)
cv2.waitKey(0)