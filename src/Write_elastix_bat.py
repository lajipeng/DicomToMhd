#-*- coding:utf-8 -*-
# Author: Lajipeng
# Data: 2019/8/12
# Fuction: Make .bat for controlling elastix which will used for registration
import os
import sys
import SimpleITK as sitk
import numpy as np
# elastix -f exampleinput/fixed.mhd -m exampleinput/moving.mhd -out exampleoutput -p exampleinput/parameters_BSpline.txt
filename = '1.bat'
Text1 = "elastix -f"
Path_dcm = "E:\\Research\\Liver 20181228 mhd\\#2"

Series_ID = []
with open (filename,'a') as file_object :
    F1 = os.listdir(Path_dcm)
    for i in F1:
        F2 = os.listdir(Path_dcm + '\\' + i)
        F1_i = i
        for j in F2:
            F1_j = Path_dcm + '\\' + F1_i + '\\' + j 
            #print(F1_j)
            file_object.write(Text1 + ' ' +  '"' +  F1_j + '"' + '\n')
            #sys.exit(0)


