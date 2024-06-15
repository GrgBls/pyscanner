import cv2
from pyzbar .pyzbar import decode
cap=cv2.VideoCapture(0)

while True:
    success, img =cap.read()

    if not success:
        break
    for code in decode(img):
        print(code.data.decode("utf-8"))

    cv2.imshow("image",img)
    cv2.waitKey(1)

