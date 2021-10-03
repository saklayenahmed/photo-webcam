import datetime
import cv2

capture = cv2.VideoCapture(0)
dateTime = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')

while True:
    ret, frame = capture.read()
    cv2.imshow('-------- Capturing ---------', frame)
    cv2.imwrite(filename=dateTime+'.jpg',img=frame)
    capture.release()
    captured = cv2.imread(dateTime+'.jpg', cv2.IMREAD_GRAYSCALE)
    captured = cv2.imshow('Succefully Captured', captured)
    cv2.waitKey(1650)
    cv2.destroyAllWindows()

