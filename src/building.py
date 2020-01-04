from rule import *

class Position:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __add__(self, other):
		return Position(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Position(abs(self.x - other.x), abs(self.y - other.y))

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

class Agent(Position):
	def update(self, action):
		self.x += action.x
		self.y += action.y
	def move(self, action):
		return self + action

class Actions:
	NORTHWEST = Position(-1, 1)
	NORTH = Position(0, 1)
	NORTHEAST = Position(1, 1)
	WEST = Position(-1, 0)
	STOP = Position(0, 0)
	EAST = Position(1, 0)
	SOUTHWEST = Position(-1, -1)
	SOUTH = Position(0, -1)
	SOUTHEAST = Position(1, -1)

	directions = [NORTHWEST, NORTH, NORTHEAST, WEST, STOP, EAST, SOUTHWEST, SOUTH, SOUTHEAST]

class ExitDoor:
	def __init__(self, pos, size):
		self.pos = pos
		self.size = size
	# may add more attributes for further congestion calculation

class Grid:
	def __init__(self, blueprint):
		# blueprint should be a boolean 2-dim array
		self.grid = self.decrease_dim(blueprint)

	def decrease_dim(self, blueprint):
		# if blueprint is high dimension, need to find a method to decrease dimension
		return blueprint

	def isWall(self, position):
		return self.grid[position.x][position.y]

	def getDirections(self, position):
		return [direction for direction in Actions.directions if not self.isWall(position + direction)]

class Danger_Source:
	def __init__(self, danger_center, danger_type = 'fire'):
		self.danger_center = Position(danger_center[0], danger_center[1])
		self.danger_type = danger_type
		self.danger_area = [self.danger_center]
		self.extension_function = self.get_function(danger_type)

	def get_function(self, danger_type):
		# maybe different danger_source have different function
		pass

	def danger_extension(self, grid):
		# will be called in the building periodically
		# use grid.getDirections(somePosition) to get available direction (in list)
		pass

class Building:
	def __init__(self, blueprint, exits, danger_centers, agents):
		# the blueprint of the building, should not be changed
		self.grid = Grid(blueprint)
		self.exits = list(ExitDoor(Position(exit[0], exit[1]), exit[2]) for exit in exits)

		# need to update, the period can be determined by the main
		self.danger_sources = list(Danger_Source(danger) for danger in danger_centers)
		self.agents = list(Agent(agent[0], agent[1]) for agent in agents)

	def update(self):
		for danger_source in self.danger_sources:
			danger_source.danger_extension(self.grid)
		# how to update agents states
		for agent in self.agents:
			agent.update()


	def evaluation(self):
		print(congestion(self))
		print(distance_to_exit(self))
		print(distance_to_danger(self))
		print(agents_position(self, [Actions.SOUTHEAST]))

		return 0
		# use all agents information to get a global programming

	def takeActions(self):
		pass
		# based on evalution, choose an action
