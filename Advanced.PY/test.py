# import re

# def hi():

#     e =['2020-07-03 12:45:00' ,'2020-07-03 12:50:00' ,'00:02:00:']
#     sntnce = "select \'$1\' and  \'$2\' from \'$3\' "
#     for i in range(1,len(e) + 1):
#         print(i)
#         print(sntnce)
#         sntnce = re.sub('\$' + str(i), str(e[i-1]), sntnce)
#     return sntnce

# print(hi())


test =  [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

t = []
for i in test:
    t.append(i[1])

x = []
for i in sorted(t):
    if i not in x :
        x.append(i)
x = x[1]

for i in test:
    if x==i[1]:
        print(i[0])


