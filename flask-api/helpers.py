import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

jsonEncoder = JSONEncoder()

def decodeBytesImage(obj):
	obj['image'] = obj['image'].decode('utf-8')
	return obj


def getRandomImages(db, collection, n):
	agg_obj = [{'$sample': {'size': n}}]
	images = db.db[collection].aggregate(agg_obj)
	return [decodeBytesImage(img) for img in images]

def getRandomClassLabel(db, collection, n):
	return 'dog'

def getRandomAttributes(db, collection, n):
	return jsonEncoder.encode('snout')

def getRandomAdverbs(db, collection, n):
	return 'more'

def getRandomAdjectives(db, collection, n):
	return 'chubby'


def getPostedImage(image, num):
	label = 'image'
	if(num is not None):
		label += str(num)
	outDict = {}
	outDict[label + "ID"] = ObjectId(image['_id'])
	outDict[label + 'Name'] = image['name']
	outDict[label + 'Folder'] = image['folder']
	outDict[label + 'Binary'] = image['image']
	return outDict

def getPostedImages(images):
	if len(images) == 1:
		return getPostedImage(images[0], None)
	elif len(images) == 2:
		img0 = getPostedImage(images[0], 0)
		img1 = getPostedImage(images[1], 1)
		return {**img0, **img1}
	else:
		return None

def getGrammar():
	return '''S -> is this C ? Y | how is C different from C ? C specializes C because A | how is C different from C ? C is like C except that A | if not C what is it ? C | i don't know what P is ? P is located at L in I | i don't know what R is ? R is M in I than I | i don't know what B is ? B is H in I .
		C -> deer | bear | dog | cat | panda .
		A -> Q and A | Q .
		Q -> it is M R | it is B | it has N O | its P is M R | its P is B .
		M -> more | less .
		R -> small | furry | long | thin | chubby .
		B -> black | brown | red | white .
		N -> no | .
		O -> Ps | P .
		P -> eye | leg | horn | snout | eye-spot .
		Y -> yes | no .
		L -> (0, 0) .
		I -> imagejpeg | image2jpeg .
		H -> present | absent .\n'''

