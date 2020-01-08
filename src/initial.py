import numpy as np

global legal_pos
legal_pos = []


def extend(poslist,tempBlueprint,useless):

	tmp = [i for i in poslist if i not in useless]
	useful = 0

	for pos in tmp:

		around = [(pos[0], pos[1] + 1),  (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)] 
		for p in around:

			if p not in tmp:

				if p[0] >= 0 and p[1]>=0 and p[0] <= 140 and p[1]<= 191:
					
					if tempBlueprint[p[0]][p[1]] == False :

						tmp.append(p)

						useful = 1

	if useful == 0:
		useless.append(pos)

	return tmp

def lpos(agents,tempBlueprint):

	for i in range(2):
		useless = []
		agents = extend(agents,tempBlueprint,useless )


	return agents





