import matplotlib.pyplot as plt

class SpacePoint:
    def __init__(self, radius, phi, z):
        self.radius = radius
        self.phi = phi
        self.z = z

class EventData:
    def __init__(self, event_num):
        self.event_num = event_num
        self.spacePoints = dict()

    def appendPoint(self, layer_num, SpacePoint:SpacePoint):
        if layer_num not in self.spacePoints:
            self.spacePoints[layer_num] = SpacePoint
        elif type(self.spacePoints[layer_num]) == list:
            self.spacePoints[layer_num].append(SpacePoint)
        else:
            self.spacePoints[layer_num] = [self.spacePoints[layer_num], SpacePoint]
    
    def retrieveNumLayer(self, num_layers):
        self.num_layers = num_layers
    
    def printNumPts(self):
        prt_string = ""
        for i in range(1, self.num_layers + 1):
            if i != self.num_layers:
                prt_string = prt_string + str(len(self.spacePoints[i])) + ", "
            else:
                prt_string += str(len(self.spacePoints[i]))
        print(f"{prt_string} \n")