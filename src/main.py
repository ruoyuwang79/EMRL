import os, sys
import numpy as np 
import matplotlib.pyplot as plt 
import building 

tempBlueprint = [[False, False, True, True, True, True], 
				 [False, True, True, True, True, True],
				 [False, True, True, True, True, True],
				 [False, True, True, True, True, True],
				 [False, True, True, True, True, True],
				 [False, True, True, True, True, True]]
exits = [(5, 5)]
danger_sources = [(1, 1)]
agents = [(2, 2)]


def main(): 
	testBuilding = building.Building(tempBlueprint, exits, danger_sources, agents)
	testBuilding.evaluation()

if __name__ == '__main__': 
	main()