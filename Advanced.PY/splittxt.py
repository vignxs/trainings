with open("test.txt",'r') as f:
    start=0
    op =""
    cntr=1
    for i in f.read().split():
        if i == '******':
            if start==1:
                with open(str(cntr)+'.txt','w') as f1:
                    f1.write(op)
                    f1.close()
                    op=""
                    cntr+=1
            else:
                start = 1
        else:
            op = op + f'\
                n {i}'