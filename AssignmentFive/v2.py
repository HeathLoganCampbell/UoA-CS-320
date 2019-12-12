import sys
'''
Will return largest possible value
'''
def big_select_pearls(stream_pearls): 
  used_pearls, other_pearls = (0, 0)
  for pearl_value in stream_pearls: 
    largest_other = max(other_pearls, used_pearls)
    used_pearls = other_pearls + pearl_value 
    other_pearls = largest_other 
  return max(other_pearls, used_pearls)

while(True):
    predecessor = (sys.stdin.readline().rstrip("\n"))
    if(predecessor == ''):
      break
    stream_pearls = list(map(int, predecessor.split()))
    # there are no pearls
    if(len(stream_pearls) == 0):
      other_child = 0
    elif(len(stream_pearls) <= 3):
      # 1 1 1
      other_child = max(stream_pearls)
    else:
      other_child = max(big_select_pearls(stream_pearls[1:]), big_select_pearls(stream_pearls[:-1]))
    print(str(other_child) + " " + str(sum(stream_pearls) - other_child))