n = int(input('im gonna Reverse : '))
rev = 0
while n > 0:
    reminder = n % 10
    print(reminder)

    rev = (rev * 10) + reminder 
    print(rev)
    n=n//10

print(rev)