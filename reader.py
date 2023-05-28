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

            for tuple in tuples:
                newSpacePoint = SpacePoint(tuple[0], tuple[1], tuple[2], tuple[3])
                event.appendPoint(newSpacePoint)
            
            events.append(event)
            # event.printFivePts()
            idx += 1
    print(f"Time Taken:{time.time() - start}")

    return events

events = readFile("eventHits.txt")