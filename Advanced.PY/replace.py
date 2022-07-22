import yaml
import re

with open('replace1.yaml') as file:
    try:
        data = yaml.safe_load(file)   
    except yaml.YAMLError as exc:
        print(exc)

test = "vignesh"

for x in data.values():
    changes = re.sub('name',test,x)
    print(changes)   