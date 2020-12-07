import yaml
import requests

shelters = None

with open('shelters.yaml', 'r') as stream:
    try:
        shelters = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)

# Make sure all values are strings
shelters = [{k: str(v) for k, v in shelter.items()} for shelter in shelters]

for shelter in shelters:
    print(shelter)
    print(f'Adding {shelter["name"]}...')
    try:
        r = requests.post('http://127.0.0.1:5000/shelter', data=shelter)
        print(r.text)
    except Exception as e:
        print(f'Could not add shelter\n\n{shelter}\n\n{e}')
