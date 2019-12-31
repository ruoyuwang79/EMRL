import numpy as np 
import matplotlib.pyplot as plt 
import drawfirst, income, rule, initialpedestrian, data 

def run(): 
	plt.figure(figsize=(8, 8)) 
	evacuation_time = 0 
	time_after_step = 0 
	allPeople = initialpedestrian.creatPeople() 
	drawfirst.draw_main(allPeople,time_after_step) 

	while data.FLAG: 
		for p in allPeople: 
			rule.InExit(p,allPeople) 
			direcetion = income.Priority(p,allPeople) 
			rule.PeopleMove(p, allPeople, direcetion) 
		drawfirst.draw_main(allPeople,time_after_step) 

		if len(allPeople) == 0: 
			data.FLAG = False 
		evacuation_time += 1 
		time_after_step += 1 

	print(evacuation_time) 

if __name__ == '__main__': run()