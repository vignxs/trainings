import csv 
import pandas as pd

columns = ["name","from","age"]
rows=[["vignesh","porayar",'19'],
["dhanush","keelkatlai","20"],
['mahesh','velachery','30']]

with open('info1.csv',"w") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(rows)

df = pd.read_csv("info.csv")
print(df)