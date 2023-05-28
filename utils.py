import numpy as np

class SpacePoint:
    def __init__(self, layer_num, radius, phi, z):
        self.layer_num = layer_num
        self.radius = radius
        self.phi = phi
        self.z = z

class EventData:
    def __init__(self, event_num):
        self.event_num = event_num
        self.spacePoints = []

    def appendPoint(self, SpacePoint:SpacePoint):
        self.spacePoints.append(SpacePoint)
    
    def printFivePts(self):
        for i in range(0, 5):
            print(f"{self.spacePoints[i].layer_num}, {self.spacePoints[i].radius}, \
            {self.spacePoints[i].phi}, {self.spacePoints[i].z}")