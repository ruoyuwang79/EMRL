import os, sys
import numpy as np 
import matplotlib.image as mpimg 
import building, drawer, initial
import rule

file_object = open('img.csv')
blueprint = file_object.read().split('\n')
file_object.close()
blueprint = [i.split(',') for i in blueprint]
tempBlueprint = [[False for j in range(len(blueprint[i]))] for i in range(len(blueprint))]

for i in range(len(blueprint)):
	for j in range(len(blueprint[i])):
		if int(blueprint[i][j]) == 0:
			tempBlueprint[i][j] = True

tempBlueprint[94][92] = False
tempBlueprint[71][93] = False
tempBlueprint[71][94] = False
tempBlueprint[99][88] = False
tempBlueprint[120][161] = False
tempBlueprint[75][89] = True
tempBlueprint[92][59] = True
tempBlueprint[90][58] = True
tempBlueprint[85][54] = True

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
<<<<<<< HEAD
agents = [(21, 55),(22,122)]
=======
agents = [(21, 55)]
>>>>>>> 3df23727bcaedb9b8d25fb71bfa2d20fd9bada64
# agents = initial.lpos(agents,tempBlueprint)

def main():
	numTrain = 10
	testBuilding = building.Building(tempBlueprint, exits, danger_sources, agents)
	testDrawer = drawer.Drawer(testBuilding)
	testDrawer.draw()

if __name__ == '__main__': 
	main()