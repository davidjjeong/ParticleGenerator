from reader import *

events = readFile("eventHits.txt")

for event in events:
    event.printNumPts()

events[0].plotCylindrical()