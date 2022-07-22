f_l = {'sarah':'python','vik':'python','dhi':'c',"aka":"c++"}
f_l['san'] ='java'
print(f_l)
for l in set(f_l.values()):
	print(l)
hi={"hi","hi"}
print(hi)
 
skil = {
	'set':'delete duplicate values',
	'get':'get values of deleted key'
	}
for i,v in skil.items():
	print(f"{i} is used to {v}")

rvr ={'kaveri':'karnataka','vaigai':'TN',"nile":'egypt'}
for r,v in rvr.items():
	print(f"{r} is in {v}")
for i in rvr.keys():
	print(i)
for i in rvr.values():
	print(i)

hi={
	'sarah':'python',
	'vik':'python',
	'san':'c',
	'dhi':'c++',
	}
frnds = ['vik','aad']
for f in frnds:
	if f in hi.keys():
		print('thanks  for responding')
	else:
		print("attend thee poll")