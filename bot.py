import requests
import json
from munch import DefaultMunch


class ChatBot:
    
    def __init__(self):
        global setup
        setup = self.read_setup()
        print(setup)
        
    def read_setup(self):
        with open('setup.json', 'r') as data:
            return DefaultMunch.fromDict(json.load(data))
        
    
    def proccess_message(self,sender_phone,message):
        # if message.lower() == 'hola':
            # print('work')
        self.send_message_text(sender_phone,'Hello')
            
        # if message.startswith('!'):
            
    
    def send_message_text(self,sender_phone,message):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "template",
            "template": {
            "name": "hello_world",
            "language": {
            "code": "en_US"
            },
            }
            }
        data = json.dumps(data)
        print(data)
        url = f'https://graph.facebook.com/{setup.version}/{setup.phoneNumberClient}/messages'
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {setup.token}'}
        response = requests.post(url=url, data=data, headers=headers,)
        print(response.text)
