import ast
import time
from utils import *

def readFile(filepath):
    events = []

    start = time.time()
    with open(filepath) as f:
        for line in f:
            idx = 0
            event = EventData(idx)
            tuples = ast.literal_eval(line)
            num_layer = 0

            for tuple in tuples:
                newSpacePoint = SpacePoint(tuple[1], tuple[2], tuple[3])
                event.appendPoint(tuple[0], newSpacePoint)
                num_layer = max(num_layer, tuple[0])
            
            event.retrieveNumLayer(num_layer)
            events.append(event)
            # event.printFivePts()
            idx += 1
    print(f"Time Taken:{time.time() - start}")

    return events

events = readFile("eventHits.txt")