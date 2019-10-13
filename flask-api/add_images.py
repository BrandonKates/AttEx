import pymongo
import os, sys
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
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"): 
            print(os.path.join(directory, filename))
            continue
        else:
            continue

if __name__ == "__main__":
    addImages(CUB_2010_DIR)
