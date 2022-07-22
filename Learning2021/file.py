#filepath = "D:\\m\\pi.txt"
#with open(filepath) as word:
	#contents = word.read()
#print(contents.strip())
	#for line in word:
		#print(line.strip())

filepath = "C:\\Users\\ELCOT\\Documents\\PCC Source\\ehmatthes-pcc_2e-078318e\\chapter_10\\pi_million_digits.txt"
with open(filepath) as text:
	lines = text.readlines()
pis = ''
for line in lines:	
	pis += line.strip()

print(f"{pis[:52]}...")
print(len(pis))

birthday = ""#input("Enter your birthday, in the form mmddyy: ")
if birthday in pis: 	
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.") 

with open("C:\\Users\\ELCOT\\Documents\\python_work\\texts\\pi.txt","r+") as objects:
	
	#lines = objects.readlines()
#pi_s = ""
	#for line in objects:
		#print(line.strip())
#for line in lines:
	#pi_s += line.strip()
#pi_s.replace("pyr","vignxs")
#print(f"{pi_s}")
	content = objects.read()
#print(content)


#file = "fil.txt"
#with open(file,"a") as fob:
	#fob.write("i hate you . ")
	#fob.write("vishwa is Good a Boy")
try:
	with open("gfil.txt") as ob:
		for line in ob:
			print(line)
except FileNotFoundError:
	print("file Name IS INcorrect or i Can't Find it ")
	

try:
	print(5/0)
except ZeroDivisionError:
	print("You Can't Divide By Zero")

def count_words(filename):
	try:
		with open(filename) as f:
			content = f.read()
	except FileNotFoundError:
		pass#print("i Can't Find This File")
	else:
		words = content.split()
		num = len(words)
		print(num)
ff = ["fil.txt","py.txt","fil.txt"]
for filename in ff:
	count_words(filename)

def count(filename):
    try :
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError :
        #pass
        print("file is missing or misspelled")
    else:
     
        print(f"{content} \n")

file =["cat.txt","py.txt","dog.txt"]
for filename in file:
    print(count(filename))

with open("fil.txt") as ff:
    #for line in ff :
   	   #print(line.count("hi"))
   	c = ff.read()
print(c.lower().count("then"))


import json
filename = "foods.json"
with open(filename) as f:
    food = json.load(f)
    print(food)


#idk
import json

file = "user.json"
with open(file) as f:
	name = json.load(f)
	print(f"I Remember You {name}")

filename= "fav_num.json"
with open(filename) as f:
	name = json.load(f)
	print(f"I Know Your Favorite Number {name}")