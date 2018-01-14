import os
import shutil
import glob
import cv2

srcFolder = "E:\Hoctrentruong\HK1nam4\ComputerVision\project\dataset\Faces"
srcFolder1 = "E:\Hoctrentruong\HK1nam4\ComputerVision\project\dataset\Faces_easy"
desFolder = "E:\Hoctrentruong\HK1nam4\ComputerVision\project\Faces"
def createFolderFace(source,dest):

    for jpgfile in glob.iglob(os.path.join(source, "*.jpg")):
            shutil.copy(jpgfile, dest)

def renameImages(source):
    for i, filename in enumerate(os.listdir(source)):
        os.rename(source+"/" + filename,source + "/Faces_"+str(i)+".jpg" )
#renameImages(srcFolder1)
#createFolderFace(srcFolder1,desFolder)
#createFolderFace(srcFolder,desFolder)
#renameImages(desFolder)
def createFolderFaces():
    for i,filename in enumerate (os.listdir(srcFolder)):
        os.rename(srcFolder+"/"+filename,desFolder+"/temp"+str(i)+".jpg")
        for i,filename in enumerate (os.listdir(srcFolder1)):
            os.rename(srcFolder1+"/"+filename,desFolder+"/temp_"+str(i)+".jpg")
    #for j,filename in enumerate (os.listdir(srcFolder1)):
    #    os.rename(srcFolder1+"/"+filename,desFolder+"/Faces_"+str(i)+".jpg")
    #    if filename.
    #for jpgfile in glob.iglob(os.path.join(srcFolder,"*.jpg")):
    #    shutil.copy(jpgfile,desFolder)
#def createFolderNFaces():

#Run to rename and move data from dataset to Faces and notFaces Folder
#createFolderFaces()
#renameImages(desFolder)
