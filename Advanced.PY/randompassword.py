import random
import string

c, n = " "

for i in string.ascii_lowercase:
    c += i

s = c.upper()

for x in range(1, 11):
    n += str(x)

passlen = 10  # int(input('Enter the lenth of the password ! '))
p = "".join(random.sample(s + n + c, passlen))

print(p)
