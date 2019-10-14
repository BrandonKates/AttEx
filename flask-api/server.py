import os
import json
import numpy as np

from flask import Flask, request, send_file
#from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_cors import CORS

from bson import ObjectId

from settings import IMAGE_COLLECTION, jsonEncoder
from grammar import getGrammarJSON

from helpers import *


app = Flask(__name__)

IMAGE_DB = PyMongo(app, uri="mongodb://localhost:27017/images")
RESULT_DB = PyMongo(app, uri="mongodb://localhost:27017/results")

CORS(app)
	

getImages     = lambda n: getRandomImages(IMAGE_DB, IMAGE_COLLECTION, n)
getClassLabel = lambda n: getRandomClassLabel(IMAGE_DB, IMAGE_COLLECTION, n)
getAttributes = lambda n: getRandomAttributes(IMAGE_DB, IMAGE_COLLECTION, n)
getAdjectives = lambda n: getRandomAdjectives(IMAGE_DB, IMAGE_COLLECTION, n)
getAdverbs 	  = lambda n: getRandomAdverbs(IMAGE_DB, IMAGE_COLLECTION, n)


@app.route("/recognitionTask", methods=["GET"])
def recognitionGet():
	images = getImages(1)
	classLabel = getClassLabel(1)

	return jsonEncoder.encode({
		'images': images,
	 	'classLabel': classLabel
 	}), 200

@app.route("/recognitionTask", methods=["POST"])
def recognitionPost():
	data = json.loads(request.data)
	image = getPostedImages(data['images'])
	classLabel = data['classLabel']
	choice = data['choice']

	post = {**image, 'classLabel': classLabel, 'choice': choice}

	RESULT_DB.db['recognition'].insert_one(post)
	return json.dumps("Received!"), 200

@app.route("/grammarTask", methods=["GET"])
def grammarGet():
	images = getImages(2)
	grammar = getGrammarJSON(getGrammar())
	return jsonEncoder.encode({
		'images': images,
		'grammar': grammar,
	}), 200

@app.route("/grammarTask", methods=["POST"])
def grammarPost():
	return None;

@app.route("/clickTask", methods=["GET"])
def clickGet():
	images = getImages(1)
	attribute = getAttributes(1)
	return jsonEncoder.encode({
		'images': images,
		'attribute' : attribute,
	}), 200

@app.route("/clickTask", methods=["POST"])
def clickPost():
	data = json.loads(request.data)
	image = getPostedImages(data['images'])

	attribute = data['attribute']
	choice = data['choice']
	point = data['point']
	post = {
		**image,
		'attribute': attribute,
		'choice': choice,
		'x': point['x'],
		'y': point['y'],
	}
	RESULT_DB.db['click'].insert_one(post)
	print(post)

	with open('clickTaskResult.json', 'w') as out:
		out.write(jsonEncoder.encode(post))
	return jsonEncoder.encode(post), 200

@app.route("/chooseTask", methods=["GET"])
def chooseGet():
	images = getImages(2)
	adverb = getAdverbs(1)
	adjective = getAdjectives(1)
	return jsonEncoder.encode({
		'images': images,
		'adverb': adverb,
		'adjective': adjective,
	}), 200

@app.route("/chooseTask", methods=["POST"])
def choosePost():
	data = json.loads(request.data)
	images = getPostedImages(data['images'])

	adverb = data['adverb']
	adjective = data['adjective']
	choice = data['choice'] # which image did they choose (image0 or image1)
	post = {
		**images,
		'adverb': adverb,
		'adjective': adjective,
		'choice': choice,
	}
	RESULT_DB.db['choose'].insert_one(post)
	return jsonEncoder.encode(post), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
