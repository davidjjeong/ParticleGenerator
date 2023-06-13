from reader import *

events = readFile("input/eventHits.txt")

for event in events:
    event.printNumPts()
    # event.produceWedgeData(128)


# events[0].locateWedgeBound(128, 10, 2)
# events[0].calculateWedgeOverlap(128)

# events[0].plotCylindrical()
# events[0].plotCartesian()
# events[0].nSlicePoints(128)