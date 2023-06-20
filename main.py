from reader import *
from converter import convertToDataset

events = readFile("input/Wedge_Data.txt")

firstWedge = convertToDataset(events[0])
firstWedge.plot(show_lines = True)

"""
for event in events:
    event.printNumPts()
    # event.produceWedgeData(128)
"""

# events[0].locateWedgeBound(128, 10, 2)
# events[0].calculateWedgeOverlap(128)

# events[0].plotCylindrical()
# events[0].plotCartesian()
# events[0].nSlicePoints(128)