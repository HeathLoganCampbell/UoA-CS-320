# first n is how many lines (n <= 1000)
# 
import sys
import heapq 


def problemTwo(span_time):
  d = 0
  rooms = []
  for x in range(len(span_time)):
    start = span_time[x][0]
    end = span_time[x][1]
    distance = span_time[x][2]

    if(len(rooms) == 0):
      heapq.heappush(rooms, end)
    else:
      cur = heapq.nsmallest(1, rooms) #Peek
      if(cur[0] >= start):
         heapq.heappush(rooms, end)
      else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
  print(len(rooms))


def getKey(elem):
    return elem[0]

predecessor = (sys.stdin.readline().rstrip("\n"))
test_cases = int(predecessor)

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    # if line is blank, we leave
    if(predecessor == ''):
        break
    if(test_cases == 0):
        break
    cord_pair = list(map(int, predecessor.split()))
    span_time = []
    for x in range(len(cord_pair) // 2):
      start = (cord_pair[(x*2)])
      end = (cord_pair[(x*2)+1])
      distance = end - start
      span_time.append((start, end, distance))
    span_time = sorted(span_time, key = getKey)
    problemTwo(span_time)
    test_cases -= 1

