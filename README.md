# Particle Generator

This project forms the basis of the particle cover algorithm we intend to develop during Summer 2023 research with Dr. Ashutosh Kotwal, Fritz London Professor of Physics at Duke University. Given a text file (in our case, 'eventHits.txt') of tuples separated by comma, containing information about the points in 3-D (`layer_num`, `radius`, `phi`, `z`), we have developed a reader function to read in the data and store each data point into an instance of class `SpacePoint`.

`SpacePoint` has 4 instance variables:

- `layer_num`: which layer the `SpacePoint` is in
- `radius`: Distance from the `SpacePoint` to $r = 0$
- `phi`: Radial distance of the `SpacePoint`
- `z`: $z$-coordinate of the `SpacePoint`

Then, each `SpacePoint` is appended as a value into the dictionary of the instance of class `EventData`, with the key being the corresponding `layer_num` the `SpacePoint` is in. Conceptually, `EventData` represents the set of all `SpacePoint`s for an event, which is given as a sequence of tuples in one line of the given text file 'eventHits.txt' (Note that there may be multiple events given in the .txt file).

While there are many methods implemented in the class `EventData`, one method that should not be overlooked is the method `produceWedgeData`, which has one parameter - `nPhiSlices`representing the number of equal wedges the `SpacePoint`s in an event should be broken into. Currently in `main.py`, we use the value of 128, so the `SpacePoint`s will be divided into 128 equal wedges.

The aim of `produceWedgeData`is to write `nPhiSlices`-equally sliced wedges consisting of `SpacePoint`s to be written out into a .txt file, with each wedge represented by a sequence of tuples separated by a comma in one line. This is identical to the format of 'eventHits.txt'.

Below shows a visual of how the `SpacePoint`s in an event can be equally sliced into 128 wedges:
![alt text](/images/128_wedge_event_0.png)