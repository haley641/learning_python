#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is


import sys
import random
print(sys.argv)
assert(len(sys.argv) == 4) #saying that we have to make sure this is qual to 4
trials = int(sys.argv[1])# convert str to int
days = int(sys.argv[2])
people =int(sys.argv[3])

print((trials,days, people))
collisions =0

for t in range(trials) :
		#create an empty calendar
		calendar = []
		for i in range(days): 
			calendar.append(0)
		print(calendar)


		#for random days

		for i in range(people):
			bd =random.randint(0,days-1)
			calendar[bd] += 1 #so the number has to increase each thime
		#print (calendar)
		found = False
		for v in calendar:# will give you the number
			if v>1:
				found =True
				break
				#	wHAT IS V

		if found : collisions +=1
print(collisions/trials)
#why are collisions greater than one? and are collisions just so that the dates don't overlap
#WHAT do they have to do with 1
		# empty list
		#fill with random birthdays
		#look for any collisions
		#add one if we find any collision

#print(collisions/trials)









"""
import random
ppl=25
days=365
trial=10
dup=0
for i in range(trial):
#repeat empty cal of 0s
	calendar =[]
	for j in range (days):
		calendar.append(0)
	#print(calendar)
#fill with rando bdays



	for j in range (ppl):
		bday=random.randint(0, days-1)
		calendar[bday] +=1


	for day in calendar:
		if day>1:
			dup+=1
print(dup, trial, dup/trial)



import random

month= ['January', 'Febuary', 'March', 'April', 'May', 'June', "July", "August", "September", "October", "November", "December"]
person=[1+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"11"+"12"+"13"+"14"+"15"+"16"+"17"+"18"+"19"+"20"+"21"+"22"+"23"]

for (month, person) in zip(month, person):
	print(month, person)


names = ('Nigel', 'David', 'Derek') # tuple
ages = [52, 53, 49, 1, 2, 3]        # list

for (name, age) in zip(names, ages):
	print(name, age)



tup = 1, 2.0, 'three' # no parentheses
print(tup)
tup = (1, 2.0, 'three') # same thing with or without parentheses
print(tup)


python3 birthday.py
0.571
"""
