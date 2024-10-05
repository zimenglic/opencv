import cv2
#显示三张灰度图像
image=cv2.imread("opencv_logo.jpg")
cv2.imshow("blue",image[:,:,0])
cv2.imshow("green",image[:,:,1])
cv2.imshow("red",image[:,:,2])

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)   #描述图像灰度变化的灰度函数
cv2.imshow("gray",gray)
cv2.waitKey()
