from reader import *
from converter import convertToDataset

events = readFile("input/Wedge_Data.txt")

firstWedge = convertToDataset(events[0])
firstWedge.plot(show_lines=True)

"""
firstEvent = events[0]
nPhiSlices = 128
p = 10
B = 2

firstEvent.locateWedgeBound(nPhiSlices, p, B)
firstEvent.produceWedgeData_(nPhiSlices)
"""

# events[0].calculateWedgeOverlap(128)

# events[0].plotCylindrical()
# events[0].plotCartesian()
# events[0].nSlicePoints(128)