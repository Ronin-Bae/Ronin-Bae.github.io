#notes
#start = [timestamp, email, first, last, mentor, category, projectname, description, link, image1, image2]
#end = [studentName, gradYear, projectName, desc, projectLink, mentor, category*, imageOne*, imageTwo*]
#*category should have space replaced with _
#*image1 should be FIRST_LAST.JPG
#*image2 should be FIRST_LAST_PROJECT.jpg

import csv
import json

the_data = open("start.csv")
raw_data = list(csv.reader(the_data))

new_data = [["studentName", "gradYear", "projectName", "desc", "projectLink", "mentor", "category", "imageOne", "imageTwo"]]

gradYear = input("What is the graduation year of the class for the data you're entering?")

for row in raw_data[1:]:
    #this specific student's data
    data = []
    #student name
    data.append(row[2].strip() + " " + row[3].strip())
    #grad year
    data.append(gradYear)
    #projectName
    data.append(row[6])
    #desc
    data.append(row[7])
    #link
    data.append(row[8])
    #mentor
    data.append(row[4])
    #category
    data.append(row[5].replace(" ", "_"))
    #imageOne
    if(row[9] != ""):
        data.append(row[2].upper().strip() + "_" + row[3].upper().strip() + ".JPG")
    else:
        data.append("")
    #imageTwo
    if(row[10] != ""):
        data.append(row[2].upper().strip() + "_" + row[3].upper().strip() + "_PROJECT" + ".JPG")
    else:
        data.append("")
    new_data.append(data)


with open('finish.csv', 'w', newline='') as csvfile:
    finish = csv.writer(csvfile, delimiter=',')
    for row in new_data:
        finish.writerow(row)

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'finish.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)