import csv

# columns = ['emp_id',
# 'first_name',
# 'last_name',
# 'birth_day',
# 'sex',
# 'salary',
# 'branch_id']


# rows =[ ['100',	'David',	'Wallace',	'1967-11-17',	'M',	'250000',		'1'],
# ['101',	'Jan',	'Levinson',	'1961-05-11',	'F',	'110000',		'1'],
# ['103',	'Angela',	'Martin',	'1971-06-25',	'F',	'63000',		'2'],
# ['104',	'Kelly',	'Kapoor',	'1980-02-05',	'F',	'55000',	'3'],
# ['105',	'Stanley',	'Hudson',	'1958-02-19',	'M',	'69000',		'3']
# ]

# filename = 'employees.csv'
# with open(filename,'w', newline='') as csvf:
#     csvwriter = csv.writer(csvf)

#     csvwriter.writerow(columns)
#     for i in rows:
#         csvwriter.writerow(i)



# column = ['branch_id',
# 'branch_name',
# 'emp_id']
# row =[['1',	'Corporate',	'100'],
# ['2','vegas',  '101'],
# ['3',	'Stanford',	'103']]

# filename1 = "branch.csv"
# with open(filename1,"w", newline='') as csvf2:
#     csvwrite = csv.writer(csvf2)
#     csvwrite.writerow(column)
#     csvwrite.writerows(row)

from weatherScrap import weather

print(weather())