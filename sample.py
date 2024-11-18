import os
import json
print('Sample file')

with open('config.json', 'r') as input_file:
    data = json.load(input_file)
    print(data)