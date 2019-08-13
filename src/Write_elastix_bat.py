#-*- coding:utf-8 -*-
# Author: Lajipeng
# Data: 2019/8/12
# Fuction: Make .bat for controlling elastix which will used for registration
import os
import sys
import SimpleITK as sitk
import numpy as np
import pydicom

# elastix -f exampleinput/fixed.mhd -m exampleinput/moving.mhd -out exampleoutput -p exampleinput/parameters_BSpline.txt
filename = '1.bat'
Text1 = "elastix -f"
Text2 = " -p exampleinput/parameters_BSpline.txt"
PathDicom = "E:/Research/Liver 20181228/#2"		# where to save dicom files 

SaveRawDicom = "E:/Research/Liver 20181228 mhd/#2"     # where to save mhd and raw files

SaveRegDicom = "E:/Research/Liver 20181228 reg/#2"     # where to save mhd and raw files

Series_ID = []
with open (filename,'a') as file_object :
    F1 = os.listdir(SaveRawDicom)
    for i in F1:
        F2 = os.listdir(SaveRawDicom + '/' + i)
        F1_i = i
        fix_list = []
        for j in F2:
            F1_j = SaveRawDicom + '/' + F1_i + '/' + j + '/' + j + '.mhd' 
            F2_j = PathDicom + '/' + i + '/' + j + '00000001.dcm'
            F3_j = SaveRegDicom + '/' + i + '/' + j
            RefDs = pydicom.read_file(F2_j)
            fix_list.append((F1_j,RefDs.SeriesNumber))
            #sys.exit(0)
        count = 0
        for fix_mhd in fix_list:
            if fix_mhd[1] == fix_list[-1][1]:
                if fix_mhd == fix_list[-1]:
                    print('error, no counterpart/n Please input an integer after checking the files')
                    index = input("input:")
                    fix_mhd_path = fix_list[index][0]
                    fix_list.pop(index)
                    fix_list.pop(-1)    
                else:
                    fix_mhd_path = fix_mhd[0]
                    fix_list.pop(count)
                    fix_list.pop(-1) 
                    break 
                count = count + 1
        for mov_mhd in fix_list:
            file_object.write(Text1 + ' ' +  fix_mhd_path + ' -m ' + mov_mhd + ' -out ' + F3_j + Text2 + '\n' )

            
       


