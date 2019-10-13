import pymongo
import os, sys
import base64
from pathlib import Path

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['images']
mycol = mydb['CUB_2010']

CUB_2010_DIR = "/phoenix/S5a/ukm4/datasets/CUB/CUB_200_2010/images"


image = {
    'title': None,
    'folder': None,
    'binary': None,
}
def addImages(directory):
    pathlist = Path(directory).glob('**/*.jpg')
    for path in pathlist:
        with open(str(path), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        print(encoded_string)


        image = {
            'name': path.name,
            'folder': path.parent.name,
            'binary': encoded_string,
        }
        mycol.insert_one(image)
        # because path is object not string
        #print("Folder: ", path.parent.name)
        #print("FileName: ", path.name)
        #path_in_str = str(path)
        #print(path_in_str)
        print(image)


if __name__ == "__main__":
    addImages(CUB_2010_DIR)

