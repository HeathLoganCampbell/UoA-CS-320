'''
THIS PROGRAM WILL GENERATE A RANDOM INPUT FOR
THE QUESTION OF ASSIGNMENT ONE. 

YOU CAN RUN THE FILE WITH, WHICH WILL OUTPUT
THE FILE TO ./test/sample-answer.txt
RUN: Python ./gen.py > ./test/sample-answer.txt

Height Width
(0,0) (0,1) (0,2) .. (0, width)
(1,0) (1,1) (1,2) .. (1, width)
...
(height,0) (height,1) (height,2) .. (height, width)
'''
import random

height = 400
width = 400

for y in range(height):
  line = []
  for x in range(width):
    line.append(str(random.randint(1,101)))
  print(str(height), ' ', str(width))
  print(' '.join(line))