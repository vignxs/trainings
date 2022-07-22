def user(name):
	print(f'Hello {name.title()}')
user('vignesh')
user("dhi")

def book(title):
	print(f"my favorite book is {title.title()} and its first chapter was literaly so good ")

book('rich dad poor dad')

def f(g,e='dog'):
	print(f'{e} and {g}')

f(g='hi')
f(g='hi',e='cat')

def hi(m='ilp'):
	print(m)
hi()


def candc(c,c1='india'):
	print(f'i love {c} in {c1}')
candc(c='tn',c1='tamil')
candc(c='hii')


def n(f_n,l_n):
	f = f"{f_n} {l_n}"
	return (f)
m= n('vik','ky')
print(m)
n('vi','ky')




def name(f_n,l_n,m_n=""):
	if m_n:
		f=f"{f_n} {m_n} {l_n}"
	else:
		f=f"{f_n} {l_n}"
	return (f.title())
hi = name("dhi",'vik','nesh')
print(hi)




def name1(f_n,l_n,age=None):
	d={'name':f_n,'lname':l_n}
	if age:
		d['age']=age
	return (d)
hi=name1('vik','khy',24)
print(hi)

def hi(f,n):
	a={"hi":f,'bye':n}
	return a
b =hi('v','n')
print(b)		

def get_formatted_name(first_name, last_name):

	full_name={}
	full_name[first_name] = last_name
	for i , v in full_name.items():
		hi=(f"your fav album is {i} and the songs are {v}")

	return hi

	
formatted_name = get_formatted_name('peace', 'popstar')
print(f"\nHello, {formatted_name}!")


def fullname(first,last):
	name = f"{first} {last}"
	return name.title()

print(fullname("vignesh","sivakumar"))