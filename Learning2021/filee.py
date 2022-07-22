def count(filename):
    try :
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError :
        pass
        #print("file is missing or misspelled")
    else:
        word = content
        print(word)

file =["cat.txt","py.txt","dog.txt"]
for filename in file:
    print(count(filename))