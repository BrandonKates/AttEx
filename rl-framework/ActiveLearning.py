import numpy as np
import torch, torchvision

class ActiveLearning():
	def __init__(self, learning_framework = 'random'):
		self.learning_framework = learning_framework
		#self.

	def random(self, images, known_classes, unknown_classes):
		# unimplemented: select a random unknown image/class
		return None
	def coreset(self):
		# unimplemented: create the core set algorithm for selecting a new image/class
		return None


	def learn(self, images, known_classes, unknown_classes):
		if self.learning_framework == 'random':
			return self.random(images, known_classes, unknown_classes)