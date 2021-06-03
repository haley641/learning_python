#!/usr/bin/env python3

import argparse
import mcb185

#how do you kknow which open readhing frame is a start codon]

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?






#generate random genome of specified size
# setup
parser = argparse.ArgumentParser(description='reading frame.')
# required arguments

# optional arguments with default parameters
parser.add_argument('--size', required=False, type=int, default=4500000,
	metavar='<str>', help='genome size [%(default)s]')
parser.add_argument('--orfmin', required=False, type=int, default=100,
	metavar='<int>', help='min [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=0.5,
	metavar='<float>', help='gc fraction [%(default).3f]')
# switches
parser.add_argument('--info', action='store_true',
	help='on/off switch')
# switches
parser.add_argument('--seed', action='store_true',
	help='fix seed')
# finalization
arg = parser.parse_args()

#

if arg.seed:random.seed(1)
if arg.info: print(arg.size, arg.orfmin, arg.gc)

#generate genome of specified size

seq= mcb185.randseq(arg.size, arg.gc)
#print(seq)


#look for ATG

lengths = []





for i in range(len(seq)-2):
	start= None
	stop = None 
	if seq[i:i+3]=='ATG':
		start =i
		for j in range(i, len(seq)-2,3):
			codon =seq[j:j+3]
			if codon =="TAA" or codon == 'TGA' or codon =="TAG":
				stop =j
				break
		if stop !=None: 
			lengths.append((stop-start)//3)
print(lengths)

#hist
hist= [0] * (max(lengths)+1)
for n in lengths:
	hist[n]+=1



print(hist)

count= 0


for i in range(len(hist)):
	if i > arg.orfmin:
		count+=hist[i]
	print(i,hist[i])
print(count)


















"""
#hist
histogram = [0] * (max(length)+1)
for x in lengths:
	histogram[x]+=1
print (histogram)



"""





