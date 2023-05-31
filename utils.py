import matplotlib.pyplot as plt
import numpy as np
import math

colorList = [
    "#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
    "#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
    "#5A0007", "#809693", "#FEFFE6", "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
    "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
    "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
    "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
    "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
    "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",
    "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
    "#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
    "#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
    "#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
    "#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C",
    "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6", "#A3A489", "#806C66", "#222800",
    "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4", "#1E0200", "#5B4E51",
    "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379", "#012C58"
]

class SpacePoint:
    def __init__(self, layer_num, radius, phi, z):
        self.layer_num = layer_num
        self.radius = radius
        self.phi = phi
        self.z = z

def appendToDict(d:dict, key, value:SpacePoint):
    if key not in d:
        d[key] = value
    elif type(d[key]) == list:
        d[key].append(value)
    else:
        d[key] = [d[key], value]

class EventData:
    def __init__(self, event_num):
        self.event_num = event_num
        self.spacePoints = dict()

    def appendPoint(self, layer_num, SpacePoint:SpacePoint):
        appendToDict(self.spacePoints, layer_num, SpacePoint)
    
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

    def produceWedgeData(self, nPhiSlices):
        wedges = dict()
        for ptsPerLayer in self.spacePoints.values():
            ptsPerLayer = np.array(ptsPerLayer)
            for pt in ptsPerLayer:
                angle_wrt_org = math.degrees(pt.phi) % 360
                sector_num = int(angle_wrt_org / (360 / nPhiSlices)) + 1
                appendToDict(wedges, sector_num, (pt.layer_num, pt.radius, pt.phi, pt.z))
        
        filename = f'{nPhiSlices}_wedges_event{self.event_num}.txt'
        with open(filename, 'w') as f:
            for i in range(1, nPhiSlices + 1):
                line_to_write = str(wedges[i]).replace('[', '').replace(']', '')
                f.write(line_to_write + '\n')

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
