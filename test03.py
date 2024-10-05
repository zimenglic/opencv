#opencv的常见绘图操作
import cv2
import numpy as np
image=np.zeros([300,300,3],dtype=np.uint8)
cv2.line(image,(100,200),(250,250),(255,0,0),2)#画一个起点坐标为100,200终点坐标为250,250的蓝色的线段
cv2.rectangle(image,(30,100),(60,150),(0,255,0),2) #画一个起点坐标为30,100对角点坐标为60,150的矩形
cv2.circle(image,(150,100),20,(0,0,255),3) #画一个起点坐标为150,100的半径为20的圆
cv2.putText(image,"hello",(100,50),0,1,(255,255,255),2,1)#打印一个字符串
cv2.imshow("image",image)
cv2.waitKey()
