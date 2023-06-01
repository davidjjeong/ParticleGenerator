"""
This file has been simply created for the purpose of testing whether produceWedgeData() works correctly.
"""

from reader import *

nPhiSlices = 128
wedges = readFile('output/128_wedges_event_0.txt')
num_layers = wedges[0].num_layers

numPtsPerLayer = np.zeros(num_layers)
for i in range(0, nPhiSlices):
    ptsPerLayer = wedges[i].returnPtsPerLayer()
    print(ptsPerLayer) # Print number of pts per layer for each wedge
    for j in range(0, num_layers):
        numPtsPerLayer[j] += ptsPerLayer[j]

# Print the sum of SpacePoints per layer over the wedges to check with input
prt_string = ""
for i in range(0, num_layers):
    if i != (num_layers - 1):
        prt_string = prt_string + str(int(numPtsPerLayer[i])) + ", "
    else:
        prt_string += str(int(numPtsPerLayer[i]))
print(f"{prt_string} \n")