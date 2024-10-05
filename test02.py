#先横行后纵列 类似于图像裁剪工具
import cv2
image=cv2.imread("opencv_logo.jpg")
crop=image[10:170,40:200]
cv2.imshow("image",image)
cv2.waitKey()
