import cv2
import numpy as np

cap=cv2.VideoCapture('video.mp4')
net=cv2.dnn.readNetFromONNX('D:\vihave\object_detection\multiple_object_detection\object_detection_using_yolov5\yolov5n.onnx')
file=open('coco.txt','r')
classes =file.read().split('\n')
print(classes)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(1000,1000))
    cv2.imshow('video',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
