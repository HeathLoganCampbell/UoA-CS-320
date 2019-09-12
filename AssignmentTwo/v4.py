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
  # print(depth)
  point_count = len(sortedByX)
  #  BASE CASE
  if(point_count <= 3):  
        return bruteForce(sortedByX)
  middle_index = point_count // 2 #L

  left = sortedByX[:middle_index]
  right = sortedByX[middle_index:]


  # if point_count == 2:
  #   return dist(sortedByX[0], sortedByX[1])
  # if point_count == 1 or point_count == 0:
  #   return sys.maxsize

  middle_point = sortedByX[middle_index]

  # Divide problem space into left and right 
  # left = []
  # right = []
  # for item in sortedByX:
  #   if(item[0] >= middle_point[0]):
  #     right.append(item)
  #   else:
  #     left.append(item)
  
  leftY = sortedByY[:middle_index]
  rightY = sortedByY[middle_index + 1:]
  # leftY = list()
  # rightY = list()
  # for item in sortedByY:
  #   if(item[0] <= middle_point[0]):
  #     rightY.append(item)
  #   else:
  #     leftY.append(item) 

  smallest_distance_left = splitPoints(left, leftY, current_smallest_distance, depth + 1)
  smallest_distance_right = splitPoints(right, rightY, current_smallest_distance, depth + 1)

  smallest_distance = min(smallest_distance_left, smallest_distance_right)

  # O(n) Merge them back together
  # start_time_merge = datetime.now() 
  middle_boundery = smallest_distance
  neg_boundery = middle_point[0] - middle_boundery
  pos_boundery = middle_point[0] + middle_boundery
  stripe_points = [x for x in sortedByY if neg_boundery <= x[0] <= pos_boundery]


  # time_elapsed_merge = datetime.now() - start_time_merge 
  # print('Merge (ms) {}'.format(time_elapsed_merge))
  # print("smallest distance ", smallest_distance)
  # print(stripe_points)
  
  # print("Smallest distance is ", smallest_distance, " WITH ", len(stripe_points), " points in stripe out of ", point_count)
  # print(middle_point)
  # print(stripe_points)
  # O(n) Check stripe

  # stripe_count = len(stripe_points)
  # for i in range(stripe_count - 1):
  #   for j in range((i + 1), min(i + 7, stripe_count)):
  #     current_distance = dist(stripe_points[i], stripe_points[j])
  #     if( smallest_distance > current_distance ):
  #       smallest_distance = current_distance
  # return smallest_distance
  stripe_count = len(stripe_points)
  for i in range(stripe_count - 1):
    for j in range((i + 1), min(i + 7, stripe_count)):
      current_distance = dist(stripe_points[i], stripe_points[j])
      if( smallest_distance > current_distance ):
        smallest_distance = current_distance
  return smallest_distance

  # stripe_count = len(stripe_points)
  # for i in range(stripe_count - 1):
  #   for j in range(i + 1, min(i + 10, stripe_count)):
  #     if(i + j < stripe_count):
  #       stripe_distance = dist(stripe_points[i + j], stripe_points[i])
  #       if(stripe_distance < smallest_distance):
  #         smallest_distance = min(smallest_distance, dist(stripe_points[i], stripe_points[i+j]))
  #         print(stripe_points[i + j], stripe_points[i], stripe_distance)
  # return smallest_distance



points = []

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    cord_pair = list(map(int, predecessor.split()))
    points.append((cord_pair[0], cord_pair[1]))

sortedByX = sorted(points, key=lambda x: x[0])
sortedByY = sorted(points, key=lambda x: x[1])

print(splitPoints(sortedByX, sortedByY, sys.maxsize, 0))