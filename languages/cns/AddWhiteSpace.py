#coding=utf8

import os

csvFileList = []
for filename in os.listdir("."):
    if (filename.split(".")[1] == "csv"):
        csvFileList.append(filename)

print "有以下文件要处理" 
print csvFileList

for aFile in csvFileList:
    aFileHandle = open(aFile, 'r')
    newFilename = aFile.split('.')[0]+"_1.csv"
    aFileHandleNew = open(newFilename, 'w')
    for aLine in aFileHandle:
#         aLine.replace('　', '')
        aFileHandleNew.write(aLine.rstrip() + " \n")
    aFileHandle.close()
    aFileHandleNew.close()
    print "文件", aFile,  "加空格处理完毕"
    os.remove(aFile)
    os.rename(newFilename, aFile)
