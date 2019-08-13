#-*- coding:utf-8 -*-
# Author: Lajipeng
# Date: 2019/8/12
# Fuction: creat diretory and folder for saving .mhd 
import os
import sys
#%%
Path_dcm = "E:/Research/Liver 20181228/#2"
# Path_mhd = "E:/Research/Liver 20181228 mhd/#2" 
Path_reg = "E:/Research/Liver 20181228 reg/#2" 
#%%
F1 = os.listdir(Path_dcm)
for i in F1:
    F2 = os.listdir(Path_dcm + '/' + i)
    for j in F2:
        #print(Path_mhd + '/' + i + '/' + j)
        print(Path_reg + '/' + i + '/' + j)
        sys.exit(0)
        #os.makedirs(Path_mhd + '\\' + i + '\\' + j)
        os.makedirs(Path_reg + '/' + i + '/' + j)