import csv
import os
import xml.etree.ElementTree as ET

#we write the paths

path_to_xml_folder = "/home/lucien/project_ornithoScope_lucien/convertion/task_20210625_balacet"

#we want to read all the xml files in the xml folder

xml_files = os.listdir(path_to_xml_folder)
path_to_images = "/home/lucien/project_ornithoScope_lucien/data_ornithoscope/"

with open("/home/lucien/project_ornithoScope_lucien/convertion/input_all.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for xml_file in xml_files:
        
        #we want to read the xml file
        tree = ET.parse(path_to_xml_folder + "/" + xml_file)
        root = tree.getroot()
        
        for x in root.iter("filename"):
            filename = path_to_images + x.text
            print(filename)
        for x in root.iter("xmin"):
            xmin = x.text
            print(xmin)
        for x in root.iter("ymin"):
            ymin = x.text
            print(ymin)
        for x in root.iter("xmax"):
            xmax = x.text
            print(xmax)
        for x in root.iter("ymax"):
            ymax = x.text
            print(ymax)
        for x in root.iter("value"):
            value = x.text
            print(value) #a changer dans le cas où il y a plusieurs espèces car pour l'instant on s'arrête juste au premier tag
            break
        for x in root.iter("width"):
            width = x.text
            print(width)
        for x in root.iter("height"):
            height = x.text
            print(height)
        
        csv_writer.writerow([filename, xmin, ymin, xmax, ymax, value, width, height])
    
        
  
