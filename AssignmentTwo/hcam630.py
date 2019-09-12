'''
UPI: HCAM630
NAME: HEATH LOGAN CAMPBELL

'''
import sys
from functools import cmp_to_key
from datetime import datetime 


def distX(a, b):
  return a[0] - b[0]

def distY(a, b):
  return a[1] - b[1]

def dist(a, b):
  return distX(a, b) * distX(a, b) + distY(a, b) * distY(a, b) 

'''
takes a min point
'''
def min(a, b):
  if (a < b):
    return a
  return b

'''
Brute forces all the points to find the closest
'''
def brute(ax):
    minDist = dist(ax[0], ax[1])
    ln_ax = len(ax)
    if ln_ax == 2:
        return minDist
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < minDist:  # Update min_dist and points
                    minDist = d
    return minDist

def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)  # store length - quicker
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  # assign best value to delta
    ln_y = len(s_y)  # store length of subarray for quickness
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

def closest_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Qx = ax[:mid]  # Two-part split
    Rx = ax[mid:]
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]  
    Qy = list()
    Ry = list()
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)
    # Call recursively both arrays after split
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

points = []

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    cord_pair = list(map(int, predecessor.split()))
    points.append(cord_pair)

start_time = datetime.now() 

ax = sorted(points, key=lambda x: x[0])
ay = sorted(points, key=lambda x: x[1])
p1, p2, mi = closest_pair(ax, ay)
print(mi)

time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))