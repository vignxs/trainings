from bs4 import BeautifulSoup

with open('test.xml', 'r') as f:
    data = f.read()

bsdata= BeautifulSoup(data, "xml")
b_unique = bsdata.findAll('food',{'class':'hi'})
 
print(b_unique)

 