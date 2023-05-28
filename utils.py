import numpy as np

class SpacePoint:
    def __init__(self, layer_num, radius, phi, z):
        self.layer_num = layer_num
        self.radius = radius
        self.phi = phi
        self.z = z

class EventData:
    def __init__(self, event_num, layer_num):
        self.event_num = event_num
        self.layer_num = layer_num
        self.spacePoints = np.array([])

    def appendPoint(self, SpacePoint:SpacePoint):
        self.spacePoints.append(SpacePoint)