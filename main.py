from reader import *

events = readFile("eventHits.txt")

for event in events:
    event.printNumPts()

# events[0].plotCylindrical()
# events[0].plotCartesian()
# events[0].nSlicePoints(128)
events[0].produceWedgeData(128)