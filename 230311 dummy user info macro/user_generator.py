"""
Author : Jin Choi
GitHub : https://github.com/JinCoreana
Date : 11th March 2023
Description: This is my first python project generating a specific number of dummy user data in JSON format.
"""
import random
import requests
import json
import sys
import string
import time

# Run this file via 'python3 user_generator.py 20' the number of users can be specified as suffix
if len(sys.argv) > 1:
    num_users = int(sys.argv[1])
else:
    num_users = 1000

print(f"Generating {num_users} no. dummy users...")

start_time = time.time()

try:
    # Make a request to the API to get Spanish users
    response = requests.get(f'https://randomuser.me/api/?nat=es&results={num_users}')
    # Load the JSON data from the response
    data = json.loads(response.text)

except requests.exceptions.RequestException as e:
    # Handle network errors to avoid the process gets frozen due to API error
    print("Error: ", e)
    sys.exit(1)

users=[]
# Random string generated here mixing alphabets and numbers
user_id = string.ascii_letters + string.digits 

for i in range(num_users):
    for user in data['results']:
        first_name = user['name']['first']
        father_surname = user['name']['last']
        mother_surname = user['name']['last']
        # May not need this as some people have twin surnames but just to practice :)
        while mother_surname == father_surname:
            response = requests.get('https://randomuser.me/api/?nat=es&results=1')
            data = json.loads(response.text)
            mother_surname = data['results'][0]['name']['last']


        # "ñ" and "á" 🥲 
        first_name = first_name.encode('utf-8').decode('ascii', 'ignore')
        father_surname = father_surname.encode('utf-8').decode('ascii', 'ignore')
        mother_surname = mother_surname.encode('utf-8').decode('ascii', 'ignore')
        
        users.append({'name': f'{first_name} {father_surname} {mother_surname}', 'user_id':''.join(random.choice(user_id) for i in range(8))})

# Save the list of users as a JSON file
with open(f'result/{num_users}_users.json', 'w') as f:
    json.dump({'users': users}, f, indent=4)

end_time = time.time()
print(f"{num_users} no. dummy users successfully created in {end_time - start_time} seconds.")
