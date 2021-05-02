#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

from math import sqrt


stats = [3,1,4,1,5]
n = len(stats)




  
thissum = sum(stats)
mean = thissum / n





print("min: ",stats[1])
print("max: ",stats[4])
print("Mean: " + str(mean))
print("count: ",n)

"""

stats = []
n = len(stats)





python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""