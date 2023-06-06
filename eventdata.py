from utils import *

import matplotlib.pyplot as plt
import numpy as np
import math

class SpacePoint:
    def __init__(self, layer_num, radius, phi, z):
        self.layer_num = layer_num
        self.radius = radius
        self.phi = phi
        self.z = z

class EventData:
    def __init__(self, event_num):
        self.event_num = event_num
        self.spacePoints = dict()

    def appendPoint(self, layer_num, SpacePoint:SpacePoint):
        appendToDict(self.spacePoints, layer_num, SpacePoint)
    
    def retrieveNumLayer(self, num_layers):
        self.num_layers = num_layers

    """
    Produces `nPhiSlices` wedge data with straight line boundaries.
    """
    
    def produceWedgeData(self, nPhiSlices):
        wedges = dict()
        for ptsPerLayer in self.spacePoints.values():
            ptsPerLayer = np.array(ptsPerLayer)
            for pt in ptsPerLayer:
                angle_wrt_org = math.degrees(pt.phi) % 360
                sector_num = int(angle_wrt_org / (360 / nPhiSlices)) + 1
                appendToDict(wedges, sector_num, (pt.layer_num, pt.radius, pt.phi, pt.z))
        
        filename = f'output/{nPhiSlices}_wedges_event_{self.event_num}.txt'
        with open(filename, 'w') as f:
            for i in range(1, nPhiSlices + 1):
                line_to_write = str(wedges[i]).replace('[', '').replace(']', '')
                f.write(line_to_write + '\n')
    
    def produceCurvedWedgeData(self, nPhiSlices, p, B):
        wedges = dict() # to store wedge data later
        wedgeBoundPts = np.ndarray(shape = (5, nPhiSlices), dtype = float)
    
    """
    Methods designed to print or return number of SpacePoints per layer in an event.
    """

    def printNumPts(self):
        prt_string = ""
        for i in range(1, self.num_layers + 1):
            if i != self.num_layers:
                prt_string = prt_string + str(len(self.spacePoints[i])) + ", "
            else:
                prt_string += str(len(self.spacePoints[i]))
        print(f"{prt_string} \n")
    
    def returnPtsPerLayer(self):
        ptsPerLayer = np.zeros(self.num_layers)
        for i in range(1, self.num_layers + 1):
            ptsPerLayer[i - 1] = len(self.spacePoints[i])
        
        return ptsPerLayer

    """
    Methods below are designed for visualization.
    """

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
        fig, ax = plt.subplots()
        ax.set_box_aspect(1)
        for i in range(1, self.num_layers + 1):
            x_arr = [(x.radius * math.cos(x.phi)) for x in self.spacePoints[i]]
            y_arr = [(x.radius * math.sin(x.phi)) for x in self.spacePoints[i]]
            ax.scatter(x_arr, y_arr, s = 2, c = "b")

        plt.title(f'Distribution of All SpacePoints in Event {self.event_num}')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.show()
    
    def nSlicePoints(self, nPhiSlices):
        fig, ax = plt.subplots()
        ax.set_box_aspect(1)

        plt.title(f'Distribution of All SpacePoints in Event {self.event_num}, Sliced in {nPhiSlices} Sectors')
        plt.ylabel('y')
        plt.xlabel('x')

        for i in range(1, self.num_layers + 1):
            for point in self.spacePoints[i]:
                x = point.radius * math.cos(point.phi)
                y = point.radius * math.sin(point.phi)

                angle_wrt_org = math.degrees(point.phi) % 360
                sector_num = int(angle_wrt_org / (360 / nPhiSlices))

                ax.plot(x, y, marker = 'o', markersize = 2, color = colorList[sector_num % 128])
        
        plt.show()