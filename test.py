"""
Tests whether the universal reader function works correctly.
"""
from reader import *

wedge_data = readFile("input/Wedge_Data.txt")

event_pts = 0
i = 0
total_unique_pts = set()
for wedge in wedge_data:
    unique_pts = wedge.returnUniquePoints()
    total_unique_pts = total_unique_pts.union(unique_pts)
    i += 1
    if i % 128 == 0:
        print(f'Total # of SpacePoints in Event {int(i / 128)}: {len(total_unique_pts)}')
        total_unique_pts = set()

"""
Tests whether produceWedgeData() works correctly.
"""

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