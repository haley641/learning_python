
import sys
import random

#variables needed
genome_size= int(sys.argv[1])
read_number=int(sys.argv[2])
read_len= int(sys.argv[3])


#create an empty genome

#1st way
counts=[]
for i in range(genome_size):
	counts.append(0)
#print(counts)
#create random reads

for i in range(read_number):
	start= random.randint(0, genome_size-read_len)
	end= start + read_len

	for j in range(start, end):
		counts[j]+=1
	#print(start,end)
#print(counts)


min=counts[read_len]
max=counts[read_len]
total=0

for i in range(read_len, genome_size-read_len):
	if counts[i]<min:
		min=counts[i]
	elif counts[i]>max:
		max=counts[i]
	total+=counts[i]


print(min, max, total/(genome_size-2*read_len))

	#print(i, counts[i])



"""
#2nd
counts=[0]*genome_size


#3rd
cou




#create random reads
	#choose a starting point
	#then extend the ending position
	#change count


#look at data to find min, max, and average
"""
