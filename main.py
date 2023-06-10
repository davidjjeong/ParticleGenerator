from reader import *

events = readFile("input/eventHits.txt")
"""
for event in events:
    event.produceWedgeData(128)
"""

events[0].produceCurvedWedgeData(8, 10, 2)

# events[0].plotCylindrical()
# events[0].plotCartesian()
# events[0].nSlicePoints(128)