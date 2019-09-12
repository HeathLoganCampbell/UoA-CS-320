# first n is how many lines (n <= 1000)
# 
import sys

def problemOne(span_time):
  period = []
  newStart = -1
  lastStart = -1
  for x in range(len(span_time)):
    start = span_time[x][0]
    end = span_time[x][1]
    distance = span_time[x][2]

    if(newStart < start):
      newStart = end
      lastStart = start
      newDist = (end - start)
      period.append((start, end, newDist))
  print((period))
  


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
    problemOne(span_time)
    test_cases -= 1

