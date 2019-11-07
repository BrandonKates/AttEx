import numpy as np
import torch
import torchvision

from ActiveLearning import ActiveLearning
from model import Model
from matplotlib import pyplot as plt

IMAGES_DIR = "/phoenix/S5a/ukm4/datasets/CUB/CUB_200_2011/images"
CUB_DATASET_DIR = "/phoenix/S5a/ukm4/1920projects/attriment/src/AWA/zeroshot/data/features_list_cub.pkl"


def train(images, known_classes, unknown_classes, active_learner):
    # need a set of known classes (not sure about known images)
    # need a set of unknown images/classes --> train on these
    train_image, train_class = active_learner.learn(images, unknown_classes)

    # true label is train_class
    prediction = model.predict(train_image)  # or model.predict(train_class)

    if prediction == train_class:
        continue
    return None


def trainRecognition():
    # recognition task
    return None


def trainGrammar():
    return None


active_learner = ActiveLearning(learning_framework='random')
model = Model()


# Pipeline
