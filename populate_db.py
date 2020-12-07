import yaml

with open('shelters.yaml', 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as e:
        print(e)