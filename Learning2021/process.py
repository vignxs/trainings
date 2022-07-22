import psutil


for proc in psutil.process_iter():
    print(f"{proc.name} {proc.pid}")
    

# import wmi
# f = wmi.WMI()

# print('pid   and  process name')

# for process in f.Win32_Process():

#     print(f"{process.ProcessID:<10}{process.name}")

# # import requests
# # page = requests.get("https://about-vignxs.herokuapp.com")

# # print(page.status_code)

# # import os

# # # Running the aforementioned command and saving its output
# # output = os.popen('wmic process get description, processid').read()

# # Displaying the output
# # print(output)

# # import module

# # import ping3
# # import subprocess

# # resp = ping()






# # traverse the software list
# Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
# a = str(Data)
# # try block
# # arrange the string
# try:
# 	for i in range(len(a)):
# 		print(a.split("\\r\\r\\n")[i])
# except IndexError as e:
# 	print("All Done")


# import platform
# import psutil
# import subprocess
# def myping():
#     hostsfile=open("hosts.txt", "r")

#     lines=hostsfile.readlines()

#     parameter = '-n' if platform.system().lower()=='windows' else '-c'
#     for line in lines:
#         command = ['ping', parameter, '1', line]
        
#         response = subprocess.call(command)
#         if response == 0:
#             print( f"{line} is Up and Running")
            
#             for proc in psutil.process_iter():
                
#                 if proc:
#                     print('and Processes are Running')
            
#         else:
#             print( "Not Running")
            
# print(myping())