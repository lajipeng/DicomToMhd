#-*- coding:utf-8 -*-
# Author: Lajipeng
# Data: 2019/8/12
# Fuction: Make .bat for getting dicom series list through Convert3D
import os
import sys
import SimpleITK as sitk
import numpy as np
# c3d.exe -dicom-series-read C:/Users/10446/Desktop/1  1.2.840.113619.2.55.3.2831164355.701.1526254298.770.3.31.250000512512 -type short -omc C:/Users/10446/Desktop/moving.mh
filename = '1.bat'
Text1 = "c3d.exe -dicom-series-list"
Path_dcm = "E:\\Research\\Liver 20181228\\#2"

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


