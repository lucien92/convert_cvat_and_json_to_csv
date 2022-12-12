import json
import csv

path_to_json = "/home/lucien/project_ornithoScope_lucien/convertion/792985.json"

with open(path_to_json) as config_buffer:
    annot = json.loads(config_buffer.read())

path_to_images = "/home/lucien/project_ornithoScope_lucien/data_ornithoscope/"
#image = {'File_path': '792985/177703363.jpeg', 'visited': 0, 'width': 500, 'height': 375, 'boxes': [{'xmin': 0.322, 'ymin': 0.424, 'xmax': 0.582, 'ymax': 0.784, 'specie': 'PICMAR', 'score': 0.86}]}
with open("/home/lucien/project_ornithoScope_lucien/convertion/input_all_2.csv", "w") as f:
    csv_writer = csv.writer(f, delimiter=',')
    for image in annot:
        filename = path_to_images + image["File_path"]
        if len(image["boxes"]) != 0:
            
            xmin = image["boxes"][0]["xmin"]
            ymin = image["boxes"][0]["ymin"]
            xmax = image["boxes"][0]["xmax"]
            ymax = image["boxes"][0]["ymax"]
            print(image["boxes"][0])
            print("look", image["boxes"][0]["specie"])
            value = image["boxes"][0]["specie"]
            width = image["width"]
            height = image["height"]
            
            csv_writer.writerow([filename, xmin, ymin, xmax, ymax, value, width, height])
        else:
            csv_writer.writerow([filename,'','','','','empty', image["width"], image["height"]])
