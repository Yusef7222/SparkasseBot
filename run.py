from source.main import Sparkasse

import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    token = data['token']

Sparkasse.execute_client(token)