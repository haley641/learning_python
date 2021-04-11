#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations


n=5
sum=0
fac=1
for i in range(1,n+1):
	sum=sum+i
	fac=fac*i
print(sum,fac)
"""

total=0
for number in [1,2,3,4,5]:
	total =total+number

print("done", total)


total=0
for number in range(0,6):
	total =total+number

print("done", total)

#factorial 
n = int(input("enter number:"))
result = 1
for i in range(n,0,-1):
	result=result*i

print("factorial is", result)




n = 5

class solution:
	def runningSum(self, nums):
		n=0
		lst=[]
		for i in nums:
			n=i+a 
			lst.append(a)
		return(lst)

"""
