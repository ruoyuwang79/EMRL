import os, sys
import numpy as np 
import matplotlib.image as mpimg 
import building, drawer

file_object = open('../img.csv')
blueprint = file_object.read().split('\n')
blueprint = [i.split(',') for i in blueprint]
# print(blueprint)
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
exits = [(5, 5)]
danger_sources = [(1, 1)]
agents = [(2, 2)]

def main(): 
	testBuilding = building.Building(tempBlueprint, exits, danger_sources, agents)
	testDrawer = drawer.Drawer(testBuilding)
	testDrawer.draw()

if __name__ == '__main__': 
	main()