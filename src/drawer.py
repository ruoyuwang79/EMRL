import numpy as np
import matplotlib.pyplot as plt
from building import *

class Drawer:
	def __init__(self, building):
		booleanMap = np.array(building.grid.grid)
		self.blueprint = np.zeros(booleanMap.shape)
		
		for i in range(len(booleanMap)):
			for j in range(len(booleanMap[i])):
				self.blueprint[i][j] = 255
				if booleanMap[i][j]:
					self.blueprint[i][j] = 0
		for i in building.exits:
			self.blueprint[i.x][i.y] = 80
		for i in building.danger_sources:
			for j in i.danger_area:
				self.blueprint[j.x][j.y] = 180
		for i in building.agents:
			self.blueprint[i.x][i.y] = 60

	def draw(self):
		plt.imshow(self.blueprint, cmap = 'gist_ncar')
		plt.show()