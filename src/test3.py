#-*- coding:utf-8 -*-

#-*- coding:utf-8 -*-
# Author: Lajipeng
# Data: 2019/8/12
# Fuction: creat .bat as below
# c3d.exe -dicom-series-read C:/Users/10446/Desktop/1  1.2.840.113619.2.55.3.2831164355.701.1526254298.770.3.31.250000512512 -type short -omc C:/Users/10446/Desktop/moving.mh
# a模式
import os

import sys

import SimpleITK as sitk

import numpy as np

filename = '2.bat'
Text1 = "c3d.exe -dicom-series-read"
Text2 = "-type short -omc"
Path_dcm = "E:\\Research\\Liver 20181228\\#2"
Path_mhd = "E:\\Research\\Liver 20181228 mhd\\#2"
Series_ID = []
with open (filename,'a') as file_object :
    F1 = os.listdir(Path_dcm)
    for i in F1:
        F2 = os.listdir(Path_dcm + '\\' + i)
        F1_i = i
        s = []
        for j in F2:
            F1_j = Path_dcm + '\\' + F1_i + '\\' + j 
            F2_j = Path_mhd + '\\' + F1_i + '\\' + j + '.mhd'
    #        print(F1_i)
            ID=sitk.ImageSeriesReader.GetGDCMSeriesIDs(F1_j)
            # print(F1_j)
            file_object.write(Text1 + ' ' +  '"' +  F1_j + '"' + ' ' + ID[0] + ' ' + Text2 + ' ' + '"' + F2_j + '"' + '\n')
    #       s.append(Text1 + ' ' + F1_j + ' ' + ID[0] + ' ' + Text2 + ' ' + F2_j)
    #       sys.exit(0)
    #   Series_ID.append(s)
#   print(Series_ID)
sys.exit(0)

