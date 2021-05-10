import sys

#hydrophobocity of aminos...first identify them
#get all the sequences...well the name and length of all sequences
#then you ge the hydrophobocity of each region

def kd(seq): #	WHAT IS THIS	what does the kd stand for ...don't you have to 
#assign each score for each aa and then each region will have to do it
# is 



	return 1.0

ids= []
proteins=[]

with open(sys.argv[1]) as fp:
	seq=[]
	for line in fp.readlines():
		line =line.rstrip()
		#print(line)
		if line.startswith('>'): #if the length of the sequence is not = 0 then...
			words=line.split()
			#s=words[0]
			ids.append(words[0][1:])
			if len(seq)>0: proteins.append(''.join(seq))
			seq=[]

		else: 
			seq.append(line)
	proteins.append(''.join(seq))
print(len(ids),len(proteins))
#look for hydrophobic regions in all sequences

w=11
for id,seq in zip(ids,protiens):
	print(id, len(seq))
 	for i in range(len(seq)-w+1):
 		print(i, kd (seq[i:i+w]))