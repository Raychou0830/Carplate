# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:05:39 2020

@author: User
"""
import glob

#dirpath = r"C:\Users\User\.spyder-py3\*.jpg*"
dirpath = r"C:\Users\Ray\Desktop\car\YOLO_labeledFile\*.png*"

result = glob.glob(dirpath)

for f in result:
    print(f)
    file = open('train1.txt', 'a', newline='')
    file.write(f)
    file.write('\n')
    #count+=1    
    file.close()