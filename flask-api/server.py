import os
import json
import numpy as np

from flask import Flask, request
from flask_restful import Resource, Api

from flask_cors import CORS
from flask import send_file
from PIL import Image

#from app.settings import *


data = []
app = Flask(__name__)
CORS(app)
api = Api(app)

static_dir = "app/static/images/"

images = [{
    'image': 'data:image/jpeg;base64,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'
  },
  {  
    'image': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAHkAtQMBIgACEQEDEQH/xAAcAAABBAMBAAAAAAAAAAAAAAAEAwUGBwABAgj/xABDEAACAQMDAQUFBQQHBwUAAAABAgMABBEFEiExBhNBUWEHIjJxgRQjkcHwM0KhsRU0cnOy0eEWNVJiksLxJCV0gqL/xAAYAQADAQEAAAAAAAAAAAAAAAAAAQIDBP/EACERAQEAAgICAwADAAAAAAAAAAABAhEhMRJBAyIyIzNx/9oADAMBAAIRAxEAPwCnJFDNljisWD7piG4rT43JnpXcsm/3Qu1cdKmn7bQfdqD9K0kcjy7Y1yB4+FcRsOFPWtqZe8KqTjypD0Njs5BKryMCp8BSksOwnGNtBPdSIwjHjxRC7zj3sr481OqJ2RQfecnx6UdpZ7q7XA5ZxkUJErGU+77uetGFTa3yjPIYNTvRzvazexPcRarGJS6o28jb5kgcnwHhTzrxcyuod45DBKyqrcM68HqP+Y0waDazahpc0sWxC9uyrIzYCtnIz4jnHNPuuG3uNIsdSiZSsLiYMF3ZRVbcPmU3DPyzVD3RVhPJFoEVxdqYjaRGXaF+EhWyB4+flXeoxyXOk2clvJ3YW8inUoMHHB/A5A+tFSSIumSSKilH733SOCME5b8OaSso5r3s3DuQCU25LhOcNtzwPQ0qFJ+0KIr2y1hFHBuSwx5EA/nTNbWzlWJ4GPGpP7T3P+2N86cCRYX9Qe6TNRuOWWd+6OWOOABTlTe0o02WG77O3MDxI0lvDgMByw/QqO/atrKUj7sYx0p00CRorXUIZHKkwnIxTLEp7yMSEkZxmox4tXnfrEh13TJIuz1jfyXO8XPCqARs4qP6ciGVInHLP1zViWlpb6h2KkjuNSgaGyk71Q3xdOlQGW4jkvQsKqqbxtYeFTjbzKymVt5C3cXc30qscgMQKkfZvRra/wBEvbl5wZY0OyLPT1qO3yn7URuLDcfe86fOyV0tvZ6gp5LREBT41eW7ivx3bIj3dd1FulA97pWpAO7Q+FdSTtKuHUADislH/pl+eKZRx06dDzWq4TJFZRobKuAcbvCtcFgR4ClJEGFz40oAozgA8UxbyBQZmX50ag7tyeuaHfKsCFA5rcjEPnPQUDW46eLfOCeBRUUYGQScDxFCPJ94rHpiiFmZYkX/AI25NP0NclEMYkYEtkdKKjuYkmWSaISZGCGoFm2ykdM0qQxOSAVHU1OzsWt2DucKYmTFuo3owb1PUHw6c+lGdhlN32YtVBJEczA4fn944PzVq57FjS5Wtbe1nE7wW7mRl4KMSvHr1NHdnbWKwsdQksosMhZMjJyyDrzSxtva8pJ0UuIns7RraW92WFuUUTXUvMoKFGDZ9SOp5zToJWTQr2QHu+7gkkOwfu7DyD+FNN28uoez0XbWrSXEljCzQk87gu7j5kCiNUdLXsJrEgBEf2RyoHLYK/o06mKK1W+n1GcXd0FMrKinaD+6oUfwFJ6beS2c7yQxqrkcOw5FZhneNVK58TSU0oNwQPAUcXgr+hdnM0ck8gcs0qHcT1oeA7m46g8UnbPySPKstAXlYBtoU7i/kM4/GnIN8Jg2gzxdkprq4jlQTY2t4D51D1jeKRUaM/Fw2OD8qnGm659p0yfSmklkieLkEls4HJ/kf/NA3dwJdMgBh2xQnarbOtY5W4ZaZ22Zcoxex7Lkxt1VgRReiM6vcLGmXIIHGazXJoRqbPGMqQuD9KdewapPr22UDBzxj0rS/l0fHP5NIo/MjIcAhuaWC7rfYOcNRN9ZqNWvUMip3crD3vHmtKuIXMZBIcYp74Rr7abhsY8bZw0bjwZcZrKPjurmZmGoze+gAXPlWVF8keNNMo3RLlug4pKEs52g8+da3Foj6UgrlG4yDWh64Kyb1AU+fWlhtO0EZNJSZdwAeAMg1kpI2kdaQha6WM+h9KSUfByeDWM/3WTzXKHIzTE7Eyhe/TPTFKSvtcR54Yjik5lO6LbRxtlN1ZFPfZmUkH0IpKqzeztn9l1mfR7gpIVt1aN0wq4DK3I6knI/6af7KJh2amMeBJNvK4PC72OPwz/CmCxvmbtNpE7W+0y2soPHxDHB/wDzUpuLgWGhibZ3kkHdfdKvxHK+79Tx9aJNKt2Knt5Y9DuYSYwVgwEQ8gAHpx68VF9TuHsvZrqVq2XmjgEbHOccqnJpBvaRp8N3JaXSSOyju5ZVXGGHkPTJp20SOPVbfVIoIzNYXNyJY2VCykYUn+IIxT1tO0H7Lez3VNTjEzCOKKVdokJyY+Ou354+lT3SPZN2csQWvFkvXOCTK3Tnw8qUm1LtZbOtpofZgx2qHZFNcsqBvUjIKr/H0qR6OupwafGur3cNxd8mV4Y9i+gAz/Gq8ZOUewCdgux8bo40e1DgAZxwfpQep+zrsxcpJ3NnHASMnuztOfpUglf3zzjjyoefIIdSePHzrPLLTSY7VfqXYO97Py99ojGeGTHfB8F1X5/j+FMnay7ksdGjhwiPcT4245UAVeKSJLE25cDAzxVa+1Dsd9tgOo6cjNcQDLoOsi+P1FZTWWW6Wfx87VTqqx9+vdfDtU/WnjsPP3faGNwucnkCh9X0+0TTra4+0FZtmGjrjsk5i1+AJ1LCtd7xqvju/khDtEwfW73A2qZiRmk7SRTBKEH7Mg/OjO2tsbbtFeIW3ZcH8RQelxM6ThUJLIcACnPyVn3rq8aWZIZZcpvUlc+IrK67id8Jc7l7tQqgjoPKso0zNsLbgeK24EwGAFI4rtIwm7byKTSQI+dm4g01emMrbsDyrcwwinxFLPGSAwPhzSU2O7FAjlxmEY8a0mdpFKk/ccccdaPjkW6t07y22qq43p1NF4BCUe7Eac7AFbuCYsvuyLtXzNNV3jul2k4B4z1qX9gey192kuEMSutnC+Z5z8I9B5miTasj1b/a/wDaXQ4kMk4ijeI4U8Lz5eGDj6VNtXjuWitLf7NIYjOhlJGNijJz+IHFSTS0ttKHc28YiQDknksfU0TNIs7ZG0nHlmlnlJCxlteeO13ZPUU129msrZ2tZZS6NjHxcn+NTP2La5f2aXejXCnu1dXQP0XOc4+ozVmvb2kq7JkAz/y0Fa9lrIXy3kBG4AgEcGnhlKMpoXetPNIkluy94PiycHFQvUfaHpthfSWV1MRKhw+yNmCnPTgVLL2VtN/axsQSfeBrzvfWUk2oGAjEjTkMrDByT+dXvaZHoWyv0uot64weRjpiicf8Q3CmXS7T+j4IoCQzKijI8cDBp5jCmIuxKD1rnyjSF41RDubHHhWp0Vos5yvgMjJqLds9fbQ9KNxkFM7BwTzzj6cVUsPtJ7QW0veJcxuhbcI5EDAenXOKUwuXR2yJD7Vexc+nw/0pYqz2DvumCpzET6eVQXQZ4odXt2G8nIq6vZ57QYe2He6Xq1nFHcbP3TuSYePB6H05qCe0TsJL2a1Yajp6/wDtcsowqjmDjx9M1r60jGaylN3b3YNbkkVFBeFHDUx6de3Ed+DDNhthwcDinPtmAJ7dg2c2wzzUc0yQpeRuR7vSiflWX9gqGK9vFabLyMznc3mayi9M1G5tLZoopkjTvWYBl58P8qypvltndbMsD5XB+tcbSztiuoQO8BI48jSkaMsjkHirP00pZUAJPka7uVAjO05rJl3ICuDzWtjmJietBxxC424xninGGVpIlhiYbiPhFBQxb1xtIejo447LTBcLIv2lyVAJ5THjRZtNZBYG6uYbae6t7QM4DSzPgRjxY/KvQ+lLZ6JoFpYaCY2tETcJVIbvCerEjqSa8vyys7lmYsT1J8alPYHtfc9n9RWFyZ7C4ISWBiSFyfiUeB/nVdQXle8VyZUJce9nx/Ki7WMwsJtxBJ6UAtsovDIh3KOQp8M0dPLti6NjoM+PNZ+O+1+WjzEyyqCQCaUQYzjimy2lLRB0YEfyo2OcOAOh+dVxEiLiCO5haOVAysMc1Xes2dvo2qJ9vijZW5jlZMmrFifvcADGKF1nS7PWLQ218nuggq44ZD5g0ssdzg8bq8mazmjuCkgVQSPoTz+QpR5RG5CnhhtbPKkjyqN3UcvZ68ayaYt4xvjG4foGuhrEQde8k7x5DkKpHvkcHH1rPV9q/wAI9p9IF/oNz3rgrGPdQ9Of9a8/XULx3EqlSMMfAjjNei7qK/u7eTvUMdngjCckgkAZ/XrTVa9nbW3umS/tYLhXYsBJGDz40TK43o/HcRX2L9n746r/AEsw7u2ClAccsf0KuvUbWLUrOS1nAdZFxhhwD8qAtXtrSBY4VSFAOFUYAom2vrdmGyVG+TCnLbdputKA9odlNYXcVtMv7NWjB8WA8ai9lIPtluABgOKuX22adBfaZFqVrKrTW5xIu4ZKnx+lUvZSdxdRSNGHVXBKnxrTXBW7som/TF1MOn3jHFZUxkHZ3VJ3bVydPuIwB9z8Mgx1rdZ+Z5Y8oPtRgGU+NbUHkUNHIqsOTjPSiXIY84AP8K00zIuMRnAIrpWJiABoyKzD27PI+PIE0MsWD1FOVWyEUjq4wx+tPiaDeTdkW10oe4S6MQHiw8W+QPFNVpZPcXaRRdT8RAztHiauTs5rel31gmjWMCw29sndC3c5JHiT55ySavHHabdKTni9wOoyM8+lOvZfSP6Q1G374lYRIMsB5c1YGr6Bo9pc97HZRjJ5XJ2f9PSiNE06GGNpFKiAk44+E54qM+FTVTzT33Rt5DOBnp4flRF3+yxnO30qP6DfGYbTgMj4/H/Wnm8kdovdTPGfKiXZUrZ3KLlZNwBGFJ4pxVwI+PLiq51TXZ9KkaSVPuVJ3E9R+VO+gdqbPUYiYJldQByMnHPlRYaTap2hOi6BeajHbG4e2jLiItt3c4pk7K+02y7QTQW01sbW5lGCxYFQfSng2Vvq1jPBK4Ec6FHb0IxVeQ+zLXdC1uwe0MVzbd8u+eNgvdqPNSfTqM1UhJB7ZUuV0dLmxXE8L4L5+FfH+FVFpWv31pOJ3VJ32bQzjJUk9RVue1y6STs9LJCsTncNu8Z6eQINURK8ndZYoMt7yqR/IUtGlTdtu0BtFtPt20KjLuQDcfr4/OmdNY1ON2ZNQuGkIIZzKxJB8OaaikrhmySoPTypZA2R3mcY658KNEcZdb1aT3ft05IGcF8fr5UJb3d0hyl1OmfKQj86TmG1SwyQTjJ86yMvneGBK85xyPnRqDZ6tL24kDxtM7LKhSQO2cg1GZy0blSMbWx+FPNtJtkVpApxgnb1x/nWa/aJEkN+0ReG8yUbOOV4IxRQ41Zx38bsnLxKeflWV3fzydxZy91GVeEbeM4ArKmLvNMUYUPk84olyG246Uh3bNjA4PXFKOpBQDwpohY+6oG448q4hikuZxHCMsfNsAfM11IjbBknpTpYQw2Vk814wR252+J8R9KeMAu3is9OtXVX3EDMs553egHQD0qMz3kv237RDIysp91xwaWvLv7U2yEMkQ5GerepodFRc7sZ6/OqoOcnai+nRY7nDhR1HBPzqYdiu0P2u0mspOZYxuXdzuX1+VV68aHIOc+VatZ5bC5SaFiCODg9R5VIXL2elA1QAMFVn5NWL3cbRKDkZ8SOSP1iqU0HWllkhni4PGRnoatu0vEltY3jZW2ruJUkZ/08zU70diqvbA3dapbWVvcO0YQyHIxgk4A/n+NNPs5sY5e1UMDTMsckTM+PIevzxUz9pOl2+qQRXVsyJKoGMjqPWon2YsZdJvmu+/3SlduAOAKq5QtVbOmgQ3IjkkBRTgqfEfwqb2kiz2pXOBjHyqqtMvgzobkndn3Wz19DT7qPbbTtBtC086mVRuEAOXIHp5VfCVee1e7vNPnbSJmljiByWzu74dcgeXzNVqrk4xkgetWV7Wbu6vI9Ku7yIx3ctvvkROkaliVU8fFg1XKW8rHJU+LD1HpUKhRZwGOAcZIMZOPpnxo6RIysqIjBkw48coRyPmODTbHG+9XOGDHOacrd2WRCqhgyAcge75geRBHBpgnN3UHxJ3kTYK54JHjg/nQygg+/kqfHpS80LrsClmif4HCnHPUdOcHAP8KGnUq2AT7vQ4wD+vypAoz7B3e/cu7wOTVn6X2Zuta9lFxDcxDvoma6sifiyM/zFVbZQtPewQkElnA4HrXpns3EttpUFsgOxUC8ilacnDzo00cun2iPu3xhgRjpzWVI+3ukjs1rckccZa2uWaaI55GTyPoa1SXtGnCQglccHFD4kmbcq8D0pWT9750bZf1VqbNxG0dqn2iYDCD3VPiabpt13L3lyWwccZ8PypfWvht/141zafE39h/8JqgDaMLyB1OQPSkeSeh8sUVP8RoZPjX50B1K+8e8xJHj4mkiCQT1x4UpPXI6tQGWV5LZSbojx4irE7K9s4LaVROQFYqH3HjGeny4/XFVqev0ru2+NPn/AJVNmzlXh2jmtbi3VreRWAiSRWB67slvTgkfoVBpdYgjfKvsdTwR40Jbf7pX6f4TUXf9sfrUeKvJYidorW4tPfcxOMMrgYHXGfTkYrWiWehWtxHql5IbmZyXjSaU++w4BbPXmolF/u2f+za/yajLT9jafP8AMVcSM7T6w2u3kt3PHlzuZTkYGBwOR1HoenhTXGJIrUSyo4EQBDYHKsq5XP8A9fp9a3J+1m/vn/wx0pafAv8Aej+a0yBfdwNKrbSjM0JPQjIzuNHWDid1jbCzoyYfr3oyQykH97BHTyFNt/1f+/X/AL64T+tr/eJ+VMHWQRJdTj3395lUp+8cEsCPAg4yOR1xTaZ0nkYhVywGcLwD6Yru/wD67c//AC5v50jH+1HyoCYdhtFW81Zbl42EcXKqT0+tXhaL3cKr1x4mq69m39SP9o1ZC/u1lk09GzWtFtdWeJrlFJjBAJAPX51lOp6VlVEP/9k='
  }]

test_recognition = {
	'images' : images[0],
  	'classLabel' : 'dog',
}

test_get_choose = {
	'images': images,
	'adverb': 'more',
	'adjective': 'chubby',
}

test_get_grammar = {
	
}

test_get_click = {
	'images': images[1],
	'attribute' : 'snout',
}

class RecognitionTask(Resource):
	def get(self):
		# get Image and Class to Display for that image
		return test_recognition

	def post(self):
		# receive the image, objectClass, and answer 
		# {	'data': 
		# 	images: {'image': 'string'},
		#	objectClass: 'string',
		# 	choice: 'boolean',
		#	}
		#
		data = json.loads(request.data)
		image = data['images']
		classLabel = data['classLabel']
		choice = data['choice']
		post = {'image': image, 'classLabel': classLabel, 'choice': choice}
		print(post)

		with open("recognitionResult.json", "w") as out:
			out.write(json.dumps(post))
		return post, 200

class GrammarTask(Resource):
	def get(self):
		return test_get_grammar

	def post(self):
		return None

class ClickTask(Resource):
	def get(self):
		return test_get_click

	def post(self):
		data = json.loads(request.data)
		images = data['images']
		attribute = data['attribute']
		choice = data['choice']
		point = data['point']
		post = {
			'image' : images,
			'attribute': attribute,
			'choice': choice,
			'point': point,
		}
		print(post)

		with open('clickTaskResult.json', 'w') as out:
			out.write(json.dumps(post))
		return post, 200

class ChooseTask(Resource):
	def get(self):
		return test_get_choose

	def post(self):
		data = json.loads(request.data)
		images = data['images']
		adverb = data['adverb']
		adjective = data['adjective']
		choice = data['choice'] # which image did they choose (image0 or image1)
		post = {
			'images': images,
			'adverb': adverb,
			'adjective': adjective,
			'choice': choice,
		}
		print(post)
		with open("chooseTaskResult.json", "w") as out:
			out.write(json.dumps(post))
		return post, 200


api.add_resource(RecognitionTask, 	'/recognitionTask')
api.add_resource(GrammarTask, 	  	'/grammarTask')
api.add_resource(ClickTask, 		'/clickTask')
api.add_resource(ChooseTask, 		'/chooseTask')





'''


@app.route('/images/<int:id>/', methods=['GET'])
def getImage(id):
	static_dir = "static"+os.sep+"images"+os.sep
	filename = static_dir + str(id) + ".jpg"
	return send_file(filename)


@app.route('/grabcut/', methods=['POST'])
def getCut():
	post = json.loads(request.data)
	imurl = static_dir + rect['imurl']
	img = np.array(Image.open(imurl))
	startX = rect['startX']
	startY = rect['startY']
	w = rect['w']
	h = rect['h']
	print('ready to process')
	rect = startX, startY, w, h
	data = initGrabCut(img, rect)
	print('finished processing')

	res = {
		'Success': True,
		'value': data  # .tolist()
	}
	return json.dumps(res), 200


@app.route('/dextr/', methods=['POST'])
def getDex():
	# data = {imurl: '', extremePoints}
	print(request.data)
	post = json.loads(request.data)
	imurl = static_dir + post['imurl']
	img = np.array(Image.open(imurl))
	extPts = post['extremePts'];
	data = initDextr(img, extPts, model=dextr_net, gpu_id = gpu_id, pad=pad, thresh=thresh)

	res = {
		'Success': True,
		'value': data
	}
	print(res)
	return json.dumps(res), 200


@app.route('/brush/', methods=['POST'])
def getPath():
	# method, points to remove, points to add, polygon if necessary, foreground + background
	# data = {imurl: '', method: '', poly: {}, rect: {}, fgPts: [], bgPts: [], extremePts: {}}
	post = json.loads(request.data)
	print("JSON_DATA: ", post)

	fgPts = post['fgPts']
	bgPts = post['bgPts']

	method = post['method']

	polygons = post['polygon']
	imurl = static_dir + post['imurl']
	img = np.array(Image.open(imurl))

	if method == "grabcut":
		rect = post['rect']
		startX = rect['startX']
		startY = rect['startY']
		w = rect['w']
		h = rect['h']
		rect = startX, startY, w, h
		data = updateGrabCut(
			img, polygons, fgPts, bgPts, rect)

	elif method == "dextr":
		extPts = np.int_(post['extremePts']);
		data = updateDextr(
			img, polygons, fgPts, bgPts, extPts)

	elif method in ["hand", "handupdate", "handremove"]:
		data = updatePolygons(
			img, polygons, fgPts, bgPts)
	res = {
		'Success': True,
		'value': data
	}
	print("BRUSH RES: ", res)
	return json.dumps(res), 200


@app.route('/hand/', methods=['POST'])
def getHand():
	# data = {imurl: '', poly: {}}
	post = json.loads(request.data)
	print(post)
	#imurl = static_dir + post['imurl']
	#img = np.array(Image.open(imurl))
	polys = post['polygon']
	data = getPolygons(polys)
	res = {
		'Success': True,
		'value': data
	}
	return json.dumps(res), 200

@app.route('/handupdate/', methods=['POST'])
def getHandUpdate():
	#data = {imurl: {}, poly: {}, oldPoly: {}}
	post = json.loads(request.data)
	print(post)
	imurl = static_dir + post['imurl']
	img = np.array(Image.open(imurl))
	newPolys = post['polygon']
	oldPolys = post['oldPoly']

	data = mergePolygons(img, oldPolys, newPolys)
	res = {
		'Success': True,
		'value': data
	}
	return json.dumps(res), 200

@app.route('/handremove/', methods=['POST'])
def getHandRemove():
	#data = {imurl: {}, poly: {}, oldPoly: {}}
	post = json.loads(request.data)
	imurl = static_dir + post['imurl']
	img = np.array(Image.open(imurl))
	polysToRemove = post['polygon']
	polys = post['oldPoly']
	data = removePolygons(img, polys, polysToRemove)
	res = {
		'Success': True,
		'value': data
	}
	return json.dumps(res), 200

@app.route('/submit/', methods=['POST'])
def getSubmit():
	post = json.loads(request.form['ans'])
	print(post)

	# updateResult(post, imageSize, canvasSize) # Updates in place, no need to assign to variable

	with open("result.json", "w") as jfile:
		jfile.write(json.dumps(post))

	return render_template('feedback.html')

'''



if __name__ == "__main__":
    app.run(debug=True)
