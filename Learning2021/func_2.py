def name(names):
	for i in names:
		msg =(f"Hello ,{i.title()}")
		print(msg)
v=['viky','dhi','san']
name(v)


def show(unprinted,completed):
	while unprinted:
		current=unprinted.pop()
		print(f"work going on {current}")
		completed.append(current)

def show2(completed):
	print("the following items are created")
	for i in completed:
		print(i)

unprinted=['cases','robos','bottle']
completed=[]

show(unprinted[:],completed)
show2(completed) 

print('\n')

def msg(list1):
	for x in list1:
		hi1=(f"\n your msgs {x}")
		print(hi1)
def s_m(list1):
	hi4=[]
	while list1:
		hi2=list1.pop()
		print(hi2)
		hi4.append(hi2)
	print(hi4)



def a_m(list1):
	hi5=[]
	while list1:
		hi5.append(list1)
	print(hi5)
hi = ['work hard','hard work','get shit done','now or never']
msg(hi[:])
s_m(hi[:])
a_m(hi[])