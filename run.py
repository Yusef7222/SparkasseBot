from source.main import Sparkasse

import json

with open('authorization_data.json', 'r') as json_file:
    data = json.load(json_file)
    token = data['token']

    


Sparkasse.setup_intents(True)
Sparkasse.execute_client(token)