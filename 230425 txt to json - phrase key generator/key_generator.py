"""
Author : Jin Choi
GitHub : https://github.com/JinCoreana
Date : 25th April 2023
Description: This python project converts txt data to JSON data.
Example: text.message.example -> {"text":{"message":{"example":"EnterYourKey"}}}
"""

import json

# read input file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# create dictionary to hold the data
data = {}

# loop through each line in the file
for line in lines:
    # split the line into keys
    keys = line.strip().split('.')
    # get the last key as the value
    value = keys.pop()
    # create nested dictionaries for each key
    current = data
    for key in keys:
        if key not in current:
            current[key] = {}
        current = current[key]
    # add the value to the final nested dictionary
    current[value] = 'EnterYourKey'

# output the JSON data to a file
with open('output.json', 'w') as f:
    json.dump(data, f)
