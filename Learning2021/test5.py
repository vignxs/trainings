from typing import Match


for k,v in enumerate(["wake",'brush','workout','bath','work','eat','work','eat','sleep']):
    print(k,v) 
print('==============================================================================================')

for k,v in enumerate(["wake",'brush','workout','bath','work','eat','work','eat','sleep']):
    print(v,end='  ') 

print('==============================================================================================')

d = { "geeks" : "for", "only" : "geeks" }
print ("The key value pair using items is : ")
for i,j in d.items():
	print (i,j)
print('==============================================================================================')

routine = ["wake",'brush','workout','bath','work','eat','work','eat','sleep']
for i in sorted(set(routine)):
    print(i)

print('==============================================================================================')

routine = ["wake",'brush','workout','bath','work','eat','work','eat','sleep']
for i in reversed(routine):
    print(i, end='-')

print('==============================================================================================')


c = (3+4j)
print(c.real)

print('==============================================================================================')

import re
routine1 = ('wake brush workout bath work eat work eat sleep')
match = re.search('wake',routine)
print(match.end(),match.start())

print('==============================================================================================')

