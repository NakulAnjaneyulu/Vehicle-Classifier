import cv
import numpy as np
import time

class Detector:
    def __init__(self, imagePath, configPath, modelPath, classPath):
        self.imagePath = imagePath
        self.configPath = configPath
        self.classPath = self.classPath

        self.net = cv.dnn_DetectionModel(self.modelPath, self.configPath)
        self.net.setInputSize(320,320)
        self.net.setInputScale(1.0/127.5)
        self.net.setInputMean((127.5, 127.5, 127.5))
        self.net.setInputSwap(True)

        self.readClasses()

    def readclasses(self):
        with open(self.classesPath, 'r') as f:
            self.classesList = f.read().splitlines()

        print(self.classesList)