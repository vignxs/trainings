p = {
	'name' : 'vik',
	'town':'pyr',
	"scl":"tnhs",
	}
print(f"hi im {p['name']},im am from {p['town']},and i studied in {p['scl']}")

hi = [1,2,3]
hi.insert(0,"hii")
print(hi)

m = {'insert':"its used to add things to the list"}
print("insert :")
print(f"\t  {m['insert']}")

print(p)
for v,k in p.items():
	print(f"\nkey = {v}")
	print(f"Value = {k}")

for k in p.keys():
	print(k.title())

for k in p.items():
	print(f"my all info {k}")

hi={
	'sarah':'c',
	'vik' : 'python',
	'you' : 'java',
	}
frnds =['sarah','phil','you']
for i in hi.keys():
	print(f"Hi {i}")

	if i in frnds:
		l = hi[i].title()
		print(f"{i.title()},i see you loving {l}")
hi['san']='python'
print(hi)

if 'me' not in hi.keys():
	print("me tell")

for i in sorted(hi.keys()):

	print(f"{i.title()}, thanks for telling ")

for i in hi.values():
	print(i)