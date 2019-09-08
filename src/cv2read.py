
#coding=utf-8

# import cv2

# import numpy as np  

 

# img = cv2.imread("C:\Github\DicomToMhd\src\hammer.png", 0)

# canny = cv2.Canny(img, 50, 150)

 

# cv2.imshow('Canny', canny)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("C:\Github\DicomToMhd\src\hammer.png", cv2.IMREAD_UNCHANGED))
# threshold 函数对图像进行二化值处理，由于处理后图像对原图像有所变化，因此img.copy()生成新的图像，cv2.THRESH_BINARY是二化值
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
# findContours函数查找图像里的图形轮廓
# 函数参数thresh是图像对象
# 层次类型，参数cv2.RETR_EXTERNAL是获取最外层轮廓，cv2.RETR_TREE是获取轮廓的整体结构
# 轮廓逼近方法
# 输出的返回值，image是原图像、contours是图像的轮廓、hier是层次类型
image, contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 显示图像
cv2.imshow("contours")
cv2.waitKey()
cv2.destroyAllWindows()


