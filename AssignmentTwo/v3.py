import sys
import math
from datetime import datetime 

def distX(a, b):
  return a[0] - b[0]

def distY(a, b):
  return a[1] - b[1]

def dist(a, b):
  return distX(a, b) ** 2  + distY(a, b) ** 2 

def min(a, b):
  if (a < b):
    return a
  return b


def bruteForce(points):
  smallest_dist = 1000000000000
  for i in range(len(points)):
    for j in range((i + 1),len(points)):
      current_distance = dist(points[i], points[j])
      if( smallest_dist > current_distance ):
        smallest_dist = current_distance
  return smallest_dist

def splitPoints(sortedByX, sortedByY, current_smallest_distance, depth):
  # print("new depth ", depth)
  point_count = len(sortedByX)
  middle_index = point_count // 2 #L
  middle_point = sortedByX[middle_index]

  #  BASE CASE
  if(point_count == 2):
    return bruteForce(sortedByX)

  if point_count == 2:
        return dist(sortedByX[0], sortedByX[1])
  if point_count == 1 or point_count == 0:
      return sys.maxsize

  # Divide problem space into left and right 
  left = sortedByX[:middle_index]
  right = sortedByX[middle_index:]

  leftY = sortedByY[:middle_index]
  rightY = sortedByY[middle_index:]

  smallest_distance_left = splitPoints(left, leftY, current_smallest_distance, depth + 1)
  smallest_distance = min(smallest_distance_left, current_smallest_distance)
  smallest_distance_right = splitPoints(right, rightY, smallest_distance, depth + 1)

  smallest_distance = min(smallest_distance, smallest_distance_right)
  # if(smallest_distance == 0):
  #   # print(smallest_distance, smallest_distance_right, smallest_distance_left, current_smallest_distance)
  #   sys.exit()

  # O(n) Merge them back together
  # start_time_merge = datetime.now() 
  middle_boundery = smallest_distance

  stripe_points = [x for x in sortedByY if abs(x[0] - middle_point[0]) < middle_boundery]

  # time_elapsed_merge = datetime.now() - start_time_merge 
  # print('Merge (ms) {}'.format(time_elapsed_merge))
  # print("smallest distance ", smallest_distance)
  # print(stripe_points)
  
  # print("Smallest distance is ", smallest_distance, " WITH ", len(stripe_points), " points in stripe out of ", point_count)
  # print(middle_point)
  # print(stripe_points)
  # O(n) Check stripe
  for i in range(len(stripe_points)):
    start_time = datetime.now() 
    for j in range(i + 1, min(i + 7, len(stripe_points))):
      if(i + j < len(stripe_points)):
        stripe_distance = stripe_points[i + j][1] - stripe_points[i][1]
        if(stripe_distance < smallest_distance):
          smallest_distance = min(smallest_distance, dist(stripe_points[i], stripe_points[i+j]))
    time_elapsed = datetime.now() - start_time 
    # print('Stripe check (ms) {}'.format(time_elapsed))
  return smallest_distance



points = []

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    cord_pair = list(map(int, predecessor.split()))
    points.append(cord_pair)

sortedByX = sorted(points, key=lambda x: x[0])
sortedByY = sorted(points, key=lambda x: x[1])

print(splitPoints(sortedByX, sortedByY, sys.maxsize, 0))