import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from building import *

class Drawer:
	def __init__(self, building):
		booleanMap = np.array(building.grid.grid)
		self.blueprint = np.zeros(booleanMap.shape)
		for i in range(len(booleanMap)):
			for j in range(len(booleanMap[i])):
				if booleanMap[i][j]:
					self.blueprint[i][j] = 255
		self.blueprint = self.blueprint

	def draw(self):
		plt.imshow(self.blueprint)
		plt.show()