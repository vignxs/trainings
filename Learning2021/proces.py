import psutil
import os

""" we have all the hostname  in the file called hosts.txt """
hostsfile=open("hosts.txt", "r")

lines=hostsfile.readlines()

for line in lines:
    response=os.system("ping -c 1 " + line)
    
    if (response == 0):
        status = line.rstrip() + " is Reachable"
        print(status)

        for proc in psutil.process_iter():
            if proc:
                print('and Processes are Running')
    else:
        status = line + " is Not reachable"



