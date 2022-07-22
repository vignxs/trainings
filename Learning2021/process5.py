
import platform
import psutil
import subprocess


runningproc = {}        #dictionary to store running processes
hostsfile=open("hosts.txt", "r") 
lines=hostsfile.readlines()
parameter = '-n' if platform.system().lower()=='windows' else '-c'  

for line in lines:
    command = ['ping', parameter, '1', line]
    
    response = subprocess.call(command)

    if response == 0:
        print(f"{line} is Reachable")
        for proc in psutil.process_iter():
            runningproc[proc.pid] = proc.name
            
        if runningproc:
            
            print (f"\n{len(runningproc)} Processes are Running")
        else:
            print("Server is Reachable but No Processes are Running")
    else:
        print( "Not Reachable")