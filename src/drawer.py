import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from building import *

class Drawer:
	def __init__(self, building):
		self.building = building
		self.blueprint = None

	def update(self):
		booleanMap = np.array(self.building.grid.grid)
		self.blueprint = np.zeros(booleanMap.shape)
		
		for i in range(len(booleanMap)):
			for j in range(len(booleanMap[i])):
				self.blueprint[i][j] = 255
				if booleanMap[i][j]:
					self.blueprint[i][j] = 0
		for i in self.building.exits:
			self.blueprint[i.x][i.y] = 80
		for i in self.building.danger_sources:
			for j in i.danger_area:
				self.blueprint[j.x][j.y] = 180
		# for i in self.building.agents:
		# 	self.blueprint[i.x][i.y] = 60

	def draw(self):
		fig = plt.figure()

		ims = []
		for i in range(50):
			self.building.update()
			self.update()
			im = plt.imshow(self.blueprint, cmap = 'gist_ncar', animated = True)

			txt = plt.text(0,0,i)
			ims.append([im,txt])

		ani = animation.ArtistAnimation(fig, ims, interval = 2000, repeat_delay = 30)
		plt.show()
