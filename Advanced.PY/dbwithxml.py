from bs4.element import SoupStrainer
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "Vignesh26@" ,autocommit=True, database = "company" )

with open("db.xml") as fp:

    soup =BeautifulSoup(fp,'xml')

    data2 = soup.find_all('student')
    for i in (data2):
        name = (i.find('name').text)
        id = (i.find('id').text)
        department = (i.find('department').text)
        data = "insert into student (name,id,department) values (%s,%s,%s)"

        c = mydb.cursor()
        c.execute(data, (name,id,department))
       

        print(f'students {name} stored')