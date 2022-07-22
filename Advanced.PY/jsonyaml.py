""" Reading Json  """
# import json
# try:
#     f = open('user.json',)
#     data = json.load(f)
# except FileNotFoundError:
#     print("File not presence in the specified location")
#else:
    #for i in data['emp_details']:
        #print(i)
    #f.close()  

""" Reading Yaml """
import yaml
with open('config.yaml') as file:
    try:
        data = yaml.safe_load(file)
        for k, v in data.items():
            print(k, ":", v)   
    except yaml.YAMLError as exc:
        print(exc)





    

   