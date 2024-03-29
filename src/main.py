import os, sys
import numpy as np 
import matplotlib.image as mpimg 
import building, drawer, initial
import rule
import random

file_object = open('img.csv')
blueprint = file_object.read().split('\n')
file_object.close()
blueprint = [i.split(',') for i in blueprint]
tempBlueprint = [[False for j in range(len(blueprint[i]))] for i in range(len(blueprint))]

for i in range(len(blueprint)):
	for j in range(len(blueprint[i])):
		if int(blueprint[i][j]) == 0:
			tempBlueprint[i][j] = True



# tempBlueprint = [[False, False, True, True, True, True], 
# 				 [False, True, True, True, True, True],
# 				 [False, True, True, True, True, True],
# 				 [False, True, True, True, True, True],
# 				 [False, True, True, True, True, True],
# 				 [False, True, True, True, True, True]]


exits = [(67, 88), (62, 118), (63, 118), (64, 118), (101, 72), (101, 73), (101, 74), 
		 (132, 158), (132, 159), (132, 160), (132, 161), (132, 162), (132, 163), (132, 164),
		 (70, 181), (71, 181), (72, 181), (73, 181), (6, 146), (6, 147), (53, 57), (54, 57),
		 (37, 26), (38, 26), (39, 26), (35, 85)]
danger_sources = [(100, 100)]


#agents = [(2,2)]
#agents = initial.lpos(agents,tempBlueprint)
agents = random.sample([i for i in initial.agents_pos if i not in exits], 100)



def main():
	numTrain = 10
	testBuilding = building.Building(tempBlueprint, exits, danger_sources, agents)
	testDrawer = drawer.Drawer(testBuilding)
	testDrawer.draw()

if __name__ == '__main__': 
	main()