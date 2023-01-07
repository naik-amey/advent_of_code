from collections import defaultdict, deque
import re

#filename, yint = 'input_sample.txt', 10
filename, yint = 'input.txt', 2000000

def mandist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

becon_set = set()
sb_dict = {}

with open(filename, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        signal_becon = [int(s) for s in re.findall(r"-?\d+", line)]
        sx,sy = signal_becon[:2]
        bx,by = signal_becon[2:]
        sb_dict[(sx,sy)] = mandist(sx,sy,bx,by)
        becon_set.add((bx,by))

'''
                        .                           .
                       ...                         ...
                      .....                       .....
                     .......     .          .      ...
              .     .........   ...        ...      .
             ...     .......   .....      .....
            .....     .....   .......    .......
y=200000:  #######     ###     #####    #########
            .....       .       ...    ...........
             ...             .   .      .........
              .             ...          .......
                           .....          .....
                            ...            ...
                             .              .
'''
def diamond_segment(sx, sy, r):
    dist = abs(yint - sy)

    if dist <= r:
        return (sx - (r - dist), sx + (r - dist))
    return None

segments = []
for sensor_loc, r in sb_dict.items():
    ret_val = diamond_segment(*sensor_loc,r)
    if ret_val:
        segments.append(ret_val)

# now sort the segments, and merge the overlapping segments.
segments = sorted(segments)

it = iter(segments)
cs, ce = next(it) #current start and current end
total = 0

for ns, ne in it:
    if ns <= ce:
        ce = max(ce, ne)
    else:
        #it is detached
        total += (ce - cs + 1)
        cs, ce = ns, ne

total += (ce - cs + 1)

# not remove the becons from the total value
beacons_on_target = sum(by==yint for bx,by in becon_set)
total -= beacons_on_target

print(f'Solution to Part 1: {total}')

'''
idea 1: I have a loop that goes from 0 to 4 million and builds the ranges for all of the rows, and then I check the ranges for each row individually and see if a row has more than 1 range, if that's the case that means that there's a hole, which is the position of the distress beacon.

idea 2:  iterated every sensor's perimeter. To be more clear, the perimeter immediately outside the sensor's range.
First I calculated the "radius" as manhattan_dist(sensor, beacon) + 1.
Then for every point in the perimeter, if it is outside EVERY sensor's range, it means we found or distress beacon, so we just calculate the frequency and break the loop.
'''

# idea 1:



## idea 2
#def getpointsonperimeter(sensor):
#    pass # list
#
#for sensor_loc,_ in sb_dict:
#    for peri_pts in getpointsonperimeter(sensor_loc):
#        if not(checkagainstallsensors(peri_pt)):
#            print(f'solution part 2: {peri_pts}')
#            break
#
