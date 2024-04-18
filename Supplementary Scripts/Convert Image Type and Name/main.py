import json
import os
from os import listdir
from wand.image import Image
import random




sourceFolder="./images"

#USE THIS ONE IF DOING PORTRAITS (MUST COMMENT OUT THE OTHER BY ADDING # INFRONT)
targetFolder="./portraits"

#USE THIS ONE IF DOING PROJECT PICTURES (MUST COMMENT OUT THE OTHER BY ADDING # INFRONT)
targetFolder="./projs"

#Functions

#HEIC -> JPG

#get student from image name
def getName(fileName):
    for name in names:
        if name in fileName:
            return name
    print(fileName)
    return "notThere" + str(random.randint(1,10000))

def convert(image):
    sourceFile=sourceFolder + "/" + image

    #USE THIS ONE IF DOING PORTRAITS (MUST COMMENT OUT THE OTHER BY ADDING # INFRONT)
    targetFile=targetFolder + "/" + getName(image).replace(" ", "_") + ".JPG"

    #USE THIS ONE IF DOING PROJECT PICTURES (MUST COMMENT OUT THE OTHER BY ADDING # INFRONT)
    targetFile=targetFolder + "/" + getName(image).replace(" ", "_") + "_PROJECT" + ".JPG"
    img=Image(filename=sourceFile)
    img.format='jpg'
    img.save(filename=targetFile)
    img.close()



#getting all the student names
with open("data.json" , "r", encoding = "utf-8") as file:
        data = json.load(file)
names = []
for student in data:
    names.append(student["studentName"].upper())
#going through every image

for image in os.listdir(sourceFolder):
    #generalize all extensions
    image = image.upper()
    convert(image)
    


