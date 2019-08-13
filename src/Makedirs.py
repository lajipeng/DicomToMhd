#-*- coding:utf-8 -*-
# Author: Lajipeng
# Data: 2019/8/12
# Fuctiion: creat diretory and Folder for saving .mhd 
import os
import sys
Path_dcm = "E:/Research/Liver 20181228/#2"
Path_mhd = "E:\Research\Liver 20181228 mhd\#2" 
F1 = os.listdir(Path_dcm)
F2 = os.listdir(Path_mhd)
for i1,i2 in zip(F1,F2):
    F12 = os.listdir(Path_dcm + '/' + i1)
    F22 = os.listdir(Path_mhd + '/' + i2)
    print(i1)
    print(i2)
    for j1,j2 in zip(F12,F22):
        #print(Path_mhd + '\\' + i + '\\' + j)
        sys.exit(0)
        #os.makedirs(Path_mhd + '\\' + i + '\\' + j)
   
    
                    
