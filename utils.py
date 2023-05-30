import matplotlib.pyplot as plt
import numpy as np
import math

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

    def plotCylindrical(self):
        for i in range(1, self.num_layers + 1):
            z_arr = [x.z for x in self.spacePoints[i]]
            r_arr = self.spacePoints[i][0].radius * np.ones(len(z_arr)) 
            plt.scatter(z_arr, r_arr, s = 2, c = "b")
        
        plt.yticks(np.arange(0, self.spacePoints[self.num_layers][0].radius + 1, self.num_layers))
        plt.title(f'Distribution of All SpacePoints in Event {self.event_num}')
        plt.ylabel('Radius')
        plt.xlabel('z-coordinate')
        plt.show()
    
    def plotCartesian(self):
        for i in range(1, self.num_layers + 1):
            x_arr = [(x.radius * math.cos(x.phi)) for x in self.spacePoints[i]]
            y_arr = [(x.radius * math.sin(x.phi)) for x in self.spacePoints[i]]
            plt.scatter(x_arr, y_arr, s = 2, c = "b")
        
        # plt.yticks(np.arange(0, self.spacePoints[self.num_layers][0].radius + 1, self.num_layers))
        plt.title(f'Distribution of All SpacePoints in Event {self.event_num}')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.show()